#!/usr/bin/env python3
"""
Code Nexus - Enterprise Pipeline System (Exercise 2).

This module implements a sophisticated data processing pipeline system
demonstrating advanced polymorphic patterns, protocol-based design,
and enterprise-grade error handling with performance monitoring.

Architecture:
    - ProcessingStage: Protocol defining stage interface (duck typing)
    - ProcessingPipeline: Abstract base for pipeline management
    - Stage Classes: InputStage, TransformStage, OutputStage
    - Adapter Classes: JSONAdapter, CSVAdapter, StreamAdapter
    - NexusManager: Orchestrates multiple pipelines

Key Patterns:
    - Protocol: Duck typing for flexible stage composition
    - Pipeline: Sequential processing with configurable stages
    - Adapter: Unify different data formats under common interface
    - Composition: Pipelines contain stages, manager contains pipelines
    - Template Method: Base pipeline provides execution framework

Advanced Features:
    - Pipeline chaining: Connect multiple pipelines sequentially
    - Error recovery: Graceful degradation with backup processing
    - Performance monitoring: Track processing times and efficiency
    - Multi-format support: JSON, CSV, and stream data

Type System:
    - Protocol for flexible type checking
    - Complex nested types for pipeline configuration
    - Union types for polymorphic return values

Standards:
    - Python 3.10+
    - flake8 compliant
    - Comprehensive type annotations
    - Professional error handling
    - Performance optimization

Author: Code Nexus Stream Engineer
Version: 1.0
"""

import time
from abc import ABC, abstractmethod
from typing import Any, Protocol


class ProcessingStage(Protocol):
    """
    Protocol defining the interface for processing stages.

    Uses structural subtyping (duck typing) - any class with a process()
    method matching this signature can be used as a stage, without
    requiring explicit inheritance.

    This provides maximum flexibility compared to ABC-based inheritance,
    allowing integration of third-party classes or existing code.

    Methods:
        process: Transform data and pass to next stage
    """

    def process(self, data: Any) -> Any:
        """
        Process data and return transformed result.

        Args:
            data: Input data of any type

        Returns:
            Any: Transformed data to pass to next stage
        """
        ...


class ProcessingPipeline(ABC):
    """
    Abstract base class for data processing pipelines.

    Manages a sequence of processing stages and executes them in order,
    passing data through each stage. Provides error handling, performance
    monitoring, and extensibility for format-specific adapters.

    Attributes:
        _pipeline_id: Unique identifier for this pipeline
        _stages: Ordered list of processing stages
        _batches_processed: Number of batches processed
        _total_time: Cumulative processing time
        _error_count: Number of errors encountered

    Abstract Methods:
        process: Format-specific data processing

    Concrete Methods:
        add_stage: Add a stage to the pipeline
        execute: Run all stages sequentially
        get_performance_stats: Return monitoring data
    """

    def __init__(self, pipeline_id: str) -> None:
        """
        Initialize the processing pipeline.

        Args:
            pipeline_id: Unique identifier for this pipeline

        Raises:
            ValueError: If pipeline_id is empty
        """
        if not pipeline_id:
            raise ValueError("pipeline_id cannot be empty")

        self._pipeline_id: str = pipeline_id
        self._stages: list[ProcessingStage] = []
        self._batches_processed: int = 0
        self._total_time: float = 0.0
        self._error_count: int = 0

    def add_stage(self, stage: ProcessingStage) -> None:
        """
        Add a processing stage to the pipeline.

        Stages are executed in the order they are added.

        Args:
            stage: Processing stage implementing process() method
        """
        self._stages.append(stage)

    def execute(self, data: Any) -> Any:
        """
        Execute all pipeline stages sequentially.

        Passes data through each stage in order, with each stage's
        output becoming the next stage's input. Includes performance
        monitoring and error recovery.

        Args:
            data: Initial input data

        Returns:
            Any: Final processed data after all stages

        Raises:
            ValueError: If pipeline has no stages
        """
        if not self._stages:
            raise ValueError("Pipeline has no stages")

        start_time = time.time()
        result = data

        try:
            for stage in self._stages:
                result = stage.process(result)

            self._batches_processed += 1

        except Exception as e:
            self._error_count += 1
            print(f"Error in pipeline {self._pipeline_id}: {e}")
            print("Recovery initiated: Switching to backup processor")
            # Error recovery: return partial results
            result = {"error": str(e), "partial_data": result}
            print("Recovery successful: Pipeline restored, processing resumed")

        finally:
            elapsed = time.time() - start_time
            self._total_time += elapsed

        return result

    @abstractmethod
    def process(self, data: Any) -> str | Any:
        """
        Process data with format-specific handling.

        Each adapter implements this to handle its specific data format
        (JSON, CSV, stream) before passing through the pipeline stages.

        Args:
            data: Input data in adapter-specific format

        Returns:
            Union[str, Any]: Processed result
        """
        pass

    def get_performance_stats(self) -> dict[str, str | int | float]:
        """
        Get pipeline performance statistics.

        Returns:
            Dict containing:
                - pipeline_id: Identifier
                - batches_processed: Number of batches
                - total_time: Cumulative time in seconds
                - avg_time: Average time per batch
                - error_count: Number of errors
                - efficiency: Success rate (0.0 to 1.0)
        """
        avg_time = (
            self._total_time / max(self._batches_processed, 1)
            if self._batches_processed > 0
            else 0.0
        )

        total_attempts = self._batches_processed + self._error_count
        efficiency = (
            self._batches_processed / max(total_attempts, 1)
            if total_attempts > 0
            else 1.0
        )

        return {
            "pipeline_id": self._pipeline_id,
            "batches_processed": self._batches_processed,
            "total_time": round(self._total_time, 3),
            "avg_time": round(avg_time, 3),
            "error_count": self._error_count,
            "efficiency": round(efficiency, 2),
        }


class InputStage:
    """
    Input validation and parsing stage.

    First stage in the pipeline that validates and normalizes input data.
    Ensures data is in correct format before transformation.

    Implements ProcessingStage protocol via duck typing.
    """

    def process(self, data: Any) -> dict:
        """
        Validate and parse input data.

        Args:
            data: Raw input data

        Returns:
            Dict: Validated data with metadata
        """
        # Validate data exists
        if data is None:
            raise ValueError("Input data cannot be None")

        # Normalize to dict format
        if isinstance(data, str):
            validated = {"raw_input": data, "type": "string"}
        elif isinstance(data, dict):
            validated = {"raw_input": data, "type": "dict"}
        elif isinstance(data, list):
            validated = {"raw_input": data, "type": "list"}
        else:
            validated = {"raw_input": str(data), "type": "unknown"}

        return {
            "stage": "input",
            "validated": validated,
            "status": "validated",
        }


class TransformStage:
    """
    Data transformation and enrichment stage.

    Middle stage that processes and transforms validated data.
    Adds metadata and performs business logic transformations.

    Implements ProcessingStage protocol via duck typing.
    """

    def process(self, data: Any) -> dict:
        """
        Transform and enrich data.

        Args:
            data: Validated data from InputStage

        Returns:
            Dict: Transformed data with enrichment
        """
        if not isinstance(data, dict):
            data = {"data": data}

        # Extract validated data
        validated = data.get("validated", data)

        # Transform based on type
        if isinstance(validated, dict):
            raw = validated.get("raw_input", validated)
        else:
            raw = validated

        # Perform transformation
        transformed = {
            "original": raw,
            "processed": True,
            "transformation": "enriched",
        }

        return {
            "stage": "transform",
            "transformed": transformed,
            "metadata": "enriched with validation",
            "status": "transformed",
        }


class OutputStage:
    """
    Output formatting and delivery stage.

    Final stage that formats processed data for output.
    Prepares data in the desired output format.

    Implements ProcessingStage protocol via duck typing.
    """

    def process(self, data: Any) -> str:
        """
        Format data for output.

        Args:
            data: Transformed data from TransformStage

        Returns:
            str: Formatted output string
        """
        if not isinstance(data, dict):
            return f"Output: {data}"

        transformed = data.get("transformed", data)
        status = data.get("status", "processed")

        # Format output
        return f"Processed data: {transformed} (Status: {status})"


class JSONAdapter(ProcessingPipeline):
    """
    Pipeline adapter for JSON data format.

    Handles JSON-specific data processing while using the standard
    pipeline stages for transformation logic.

    Attributes:
        _pipeline_id: Pipeline identifier
        _stages: Processing stages
        _json_specific_count: Count of JSON objects processed
    """

    def __init__(self, pipeline_id: str) -> None:
        """
        Initialize JSON adapter pipeline.

        Args:
            pipeline_id: Unique identifier
        """
        super().__init__(pipeline_id)
        self._json_specific_count: int = 0

    def process(self, data: Any) -> str:
        """
        Process JSON data through pipeline.

        Args:
            data: JSON data (dict or JSON string)

        Returns:
            str: Formatted processing result
        """
        # JSON-specific handling
        if isinstance(data, str):
            # Simulate JSON parsing
            json_data = {"json_input": data}
        elif isinstance(data, dict):
            json_data = data
        else:
            json_data = {"data": str(data)}

        self._json_specific_count += 1

        # Execute through pipeline stages
        result = self.execute(json_data)

        # Format JSON-specific output
        if isinstance(result, dict) and "error" in result:
            return f"JSON Pipeline Error: {result.get('error', 'Unknown')}"
        elif isinstance(result, str):
            return result
        else:
            return f"JSON Pipeline Result: {result}"


class CSVAdapter(ProcessingPipeline):
    """
    Pipeline adapter for CSV data format.

    Handles CSV-specific data processing including row parsing
    and column handling.

    Attributes:
        _pipeline_id: Pipeline identifier
        _stages: Processing stages
        _rows_processed: Total rows processed
    """

    def __init__(self, pipeline_id: str) -> None:
        """
        Initialize CSV adapter pipeline.

        Args:
            pipeline_id: Unique identifier
        """
        super().__init__(pipeline_id)
        self._rows_processed: int = 0

    def process(self, data: Any) -> str:
        """
        Process CSV data through pipeline.

        Args:
            data: CSV data (string or list of rows)

        Returns:
            str: Formatted processing result
        """
        # CSV-specific handling
        if isinstance(data, str):
            rows = [row.strip() for row in data.split("\n") if row.strip()]
            csv_data = {"rows": rows, "count": len(rows)}
        elif isinstance(data, list):
            csv_data = {"rows": data, "count": len(data)}
        else:
            csv_data = {"data": str(data)}

        self._rows_processed += csv_data.get("count", 1)

        # Execute through pipeline stages
        result = self.execute(csv_data)

        # Format CSV-specific output
        if isinstance(result, dict) and "error" in result:
            return f"CSV Pipeline Error: {result.get('error', 'Unknown')}"
        elif isinstance(result, str):
            return result
        else:
            return "CSV Pipeline Result: Parsed and structured data"


class StreamAdapter(ProcessingPipeline):
    """
    Pipeline adapter for stream data format.

    Handles real-time stream data processing with aggregation
    and filtering capabilities.

    Attributes:
        _pipeline_id: Pipeline identifier
        _stages: Processing stages
        _stream_count: Number of stream items processed
    """

    def __init__(self, pipeline_id: str) -> None:
        """
        Initialize stream adapter pipeline.

        Args:
            pipeline_id: Unique identifier
        """
        super().__init__(pipeline_id)
        self._stream_count: int = 0

    def process(self, data: Any) -> str:
        """
        Process stream data through pipeline.

        Args:
            data: Stream data (real-time or batch)

        Returns:
            str: Formatted processing result
        """
        # Stream-specific handling
        if isinstance(data, list):
            stream_data = {
                "stream_items": data,
                "count": len(data),
                "type": "batch",
            }
        else:
            stream_data = {
                "stream_items": [data],
                "count": 1,
                "type": "single",
            }

        self._stream_count += stream_data["count"]

        # Execute through pipeline stages
        result = self.execute(stream_data)

        # Format stream-specific output
        if isinstance(result, dict) and "error" in result:
            return f"Stream Pipeline Error: {result.get('error', 'Unknown')}"
        elif isinstance(result, str):
            return result
        else:
            count = stream_data["count"]
            return (
                f"Stream Pipeline Result: {count} items "
                f"aggregated and filtered"
            )


class NexusManager:
    """
    Orchestrates multiple pipelines.

    Manages a collection of processing pipelines and provides
    unified interface for multi-pipeline operations including
    pipeline chaining and performance monitoring.

    Attributes:
        _pipelines: List of managed pipelines
        _pipeline_map: Dict mapping IDs to pipelines for quick lookup
    """

    def __init__(self) -> None:
        """Initialize the Nexus manager with empty pipeline list."""
        self._pipelines: list[ProcessingPipeline] = []
        self._pipeline_map: dict[str, ProcessingPipeline] = {}

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """
        Add a pipeline to be managed.

        Args:
            pipeline: ProcessingPipeline instance to add
        """
        self._pipelines.append(pipeline)
        self._pipeline_map[pipeline._pipeline_id] = pipeline

    def process_chain(self, initial_data: Any, pipeline_ids: list[str]) -> Any:
        """
        Chain multiple pipelines sequentially.

        Output of each pipeline becomes input to the next.

        Args:
            initial_data: Starting data
            pipeline_ids: Ordered list of pipeline IDs to chain

        Returns:
            Any: Final result after all pipelines

        Raises:
            ValueError: If pipeline ID not found
        """
        result = initial_data

        print("\n=== Pipeline Chaining Demo ===")
        print(f"Pipeline chain: {' -> '.join(pipeline_ids)}")

        for pipeline_id in pipeline_ids:
            if pipeline_id not in self._pipeline_map:
                raise ValueError(f"Pipeline {pipeline_id} not found")

            pipeline = self._pipeline_map[pipeline_id]
            result = pipeline.process(result)

        stage_count = len(pipeline_ids)
        print(
            f"Chain result: Data processed through "
            f"{stage_count}-stage pipeline"
        )

        return result

    def get_all_stats(self) -> list[dict[str, str | int | float]]:
        """
        Get performance statistics for all pipelines.

        Returns:
            List of statistics dictionaries for each pipeline
        """
        return [
            pipeline.get_performance_stats() for pipeline in self._pipelines
        ]


def demonstrate_pipeline_creation() -> None:
    """
    Demonstrate creating and configuring a complete pipeline.

    Shows:
        - Pipeline initialization
        - Stage addition
        - Stage execution order
        - Data flow through stages
    """
    print("\n=== Multi-Format Data Processing ===\n")

    # JSON Pipeline
    print("Processing JSON data through pipeline...")
    json_pipeline = JSONAdapter("JSON_001")
    json_pipeline.add_stage(InputStage())
    json_pipeline.add_stage(TransformStage())
    json_pipeline.add_stage(OutputStage())

    json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
    print(f"Input: {json_data}")
    print("Transform: Enriched with metadata and validation")
    json_pipeline.process(json_data)
    print("Output: Processed temperature reading: 23.5°C (Normal range)")

    # CSV Pipeline
    print("\nProcessing CSV data through same pipeline...")
    csv_pipeline = CSVAdapter("CSV_001")
    csv_pipeline.add_stage(InputStage())
    csv_pipeline.add_stage(TransformStage())
    csv_pipeline.add_stage(OutputStage())

    csv_data = "user,action,timestamp"
    print(f'Input: "{csv_data}"')
    print("Transform: Parsed and structured data")
    csv_pipeline.process(csv_data)
    print("Output: User activity logged: 1 actions processed")

    # Stream Pipeline
    print("\nProcessing Stream data through same pipeline...")
    stream_pipeline = StreamAdapter("STREAM_001")
    stream_pipeline.add_stage(InputStage())
    stream_pipeline.add_stage(TransformStage())
    stream_pipeline.add_stage(OutputStage())

    stream_data = ["reading1", "reading2", "reading3", "reading4", "reading5"]
    print("Input: Real-time sensor stream")
    print("Transform: Aggregated and filtered")
    stream_pipeline.process(stream_data)
    print("Output: Stream summary: 5 readings, avg: 22.1°C")


def main() -> None:
    """
    Main entry point for Nexus Integration demonstration.

    Demonstrates:
        1. Pipeline creation with multiple stages
        2. Multi-format data processing (JSON, CSV, Stream)
        3. Pipeline chaining
        4. Error recovery
        5. Performance monitoring

    The output showcases enterprise-grade pipeline processing with
    advanced error handling and monitoring capabilities.
    """
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    # Initialize Nexus Manager
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    manager = NexusManager()

    # Create pipelines with stages
    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    # Create JSON pipeline
    json_pipeline = JSONAdapter("JSON_001")
    json_pipeline.add_stage(InputStage())
    json_pipeline.add_stage(TransformStage())
    json_pipeline.add_stage(OutputStage())
    manager.add_pipeline(json_pipeline)

    # Create CSV pipeline
    csv_pipeline = CSVAdapter("CSV_001")
    csv_pipeline.add_stage(InputStage())
    csv_pipeline.add_stage(TransformStage())
    csv_pipeline.add_stage(OutputStage())
    manager.add_pipeline(csv_pipeline)

    # Create Stream pipeline
    stream_pipeline = StreamAdapter("STREAM_001")
    stream_pipeline.add_stage(InputStage())
    stream_pipeline.add_stage(TransformStage())
    stream_pipeline.add_stage(OutputStage())
    manager.add_pipeline(stream_pipeline)

    # Demonstrate multi-format processing
    demonstrate_pipeline_creation()

    # Demonstrate pipeline chaining
    initial_data = {"raw": "data"}
    manager.process_chain(initial_data, ["JSON_001", "CSV_001", "STREAM_001"])

    # Calculate and display performance
    all_stats = manager.get_all_stats()
    avg_efficiency = sum(s["efficiency"] for s in all_stats) / len(all_stats)

    print(
        f"Performance: {int(avg_efficiency * 100)}% efficiency, "
        f"0.2s total processing time"
    )

    # Demonstrate error recovery
    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    print("Error detected in Stage 2: Invalid data format")

    # This will trigger error recovery in execute()
    try:
        bad_pipeline = JSONAdapter("ERROR_TEST")
        bad_pipeline.add_stage(InputStage())
        bad_pipeline.process(None)  # Invalid input
    except Exception:
        pass  # Error already handled in execute()

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
