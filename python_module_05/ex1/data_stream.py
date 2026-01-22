#!/usr/bin/env python3
"""
Code Nexus - Polymorphic Stream System (Exercise 1).

This module implements an advanced polymorphic data streaming system
with batch processing, filtering, and statistical analysis capabilities.

Architecture:
    - DataStream: Abstract base class for stream processing
    - SensorStream: Handles environmental sensor data
    - TransactionStream: Handles financial transaction data
    - EventStream: Handles system event data
    - StreamProcessor: Orchestrates multiple stream types

Key Features:
    - Batch processing for efficient data handling
    - Configurable filtering with optional criteria
    - Statistical tracking and aggregation
    - Polymorphic stream management
    - Type-specific processing logic

Design Patterns:
    - Template Method: filter_data() and get_stats() provide defaults
    - Strategy: Each stream implements custom processing logic
    - Composition: StreamProcessor contains multiple streams

Type System:
    - Optional parameters for flexible filtering
    - Complex return types (Dict[str, Union[str, int, float]])
    - List processing for batch operations

Standards:
    - Python 3.10+
    - flake8 compliant
    - Comprehensive type annotations
    - Exception handling for stream failures

Author: gagulhon
date: 2025-01-18
Version: 1.0
"""

from abc import ABC, abstractmethod
from typing import Any


class DataStream(ABC):
    """
    Abstract base class for data streams.

    Defines the interface for stream processing with batch operations,
    filtering, and statistical analysis. Provides default implementations
    for filter_data() and get_stats() that can be optionally overridden.

    Attributes:
        _stream_id: Unique identifier for the stream
        _batches_processed: Number of batches processed
        _total_items: Total items processed across all batches

    Abstract Methods:
        process_batch: Process a batch of data

    Concrete Methods:
        filter_data: Filter data based on criteria (can override)
        get_stats: Return stream statistics (can override)

    Note:
        Subclasses must provide stream_id during initialization and
        implement process_batch() with stream-specific logic.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize the data stream.

        Args:
            stream_id: Unique identifier for this stream

        Raises:
            ValueError: If stream_id is empty
        """
        if not stream_id:
            raise ValueError("stream_id cannot be empty")
        self._stream_id: str = stream_id
        self._batches_processed: int = 0
        self._total_items: int = 0

    @abstractmethod
    def process_batch(self, data_batch: list[Any]) -> str:
        """
        Process a batch of data.

        Args:
            data_batch: List of data items to process

        Returns:
            str: Formatted processing result

        Raises:
            ValueError: If data_batch is invalid
        """
        pass

    def filter_data(
        self, data_batch: list[Any], criteria: str | None = None
    ) -> list[Any]:
        """
        Filter data batch based on optional criteria.

        Provides default implementation that returns all data if no
        criteria is specified. Subclasses can override for custom
        filtering logic.

        Args:
            data_batch: List of data items to filter
            criteria: Optional filtering criteria

        Returns:
            List[Any]: Filtered data items
        """
        if criteria is None:
            return data_batch

        return [d for d in data_batch if self._matches_criteria(d, criteria)]

    def _matches_criteria(self, data: Any, criteria: str) -> bool:
        """
        Check if data matches the given criteria.

        Default implementation to be overridden by subclasses.

        Args:
            data: Single data item to check
            criteria: Filtering criteria

        Returns:
            bool: True if data matches criteria
        """
        return True

    def get_stats(self) -> dict[str, str | int | float]:
        """
        Get stream processing statistics.

        Provides basic statistics. Subclasses should override to add
        stream-specific statistics.

        Returns:
            Dict with stream statistics including:
                - stream_id: Stream identifier
                - batches_processed: Number of batches
                - total_items: Total items processed
        """
        return {
            "stream_id": self._stream_id,
            "batches_processed": self._batches_processed,
            "total_items": self._total_items,
        }


class SensorStream(DataStream):
    """
    Stream processor for environmental sensor data.

    Handles sensor readings with temperature, humidity, and pressure
    measurements. Tracks readings and calculates averages.

    Attributes:
        _stream_id: Stream identifier
        _batches_processed: Number of batches processed
        _total_items: Total readings processed
        _total_readings: Alias for total_items (sensor-specific)
        _temperature_sum: Sum of all temperature readings
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize sensor stream.

        Args:
            stream_id: Unique identifier for this sensor stream
        """
        super().__init__(stream_id)
        self._total_readings: int = 0
        self._temperature_sum: float = 0.0

    def process_batch(self, data_batch: list[Any]) -> str:
        """
        Process a batch of sensor readings.

        Args:
            data_batch: List of sensor reading dictionaries

        Returns:
            str: Formatted analysis of sensor readings

        Raises:
            ValueError: If data format is invalid
        """
        try:
            if not data_batch:
                return "No sensor data to process"

            print(f"Processing sensor batch: {data_batch}")

            readings_count = len(data_batch)
            self._batches_processed += 1
            self._total_items += readings_count
            self._total_readings += readings_count

            temps = []
            for reading in data_batch:
                if isinstance(reading, dict) and "temp" in reading:
                    temp = reading["temp"]
                    temps.append(temp)
                    self._temperature_sum += temp

            avg_temp = sum(temps) / len(temps) if temps else 0

            result = (
                f"Sensor analysis: {readings_count} readings "
                f"processed, avg temp: {avg_temp:.1f}°C"
            )
            return result

        except Exception as e:
            return f"Error processing sensor batch: {e}"

    def _matches_criteria(self, data: Any, criteria: str) -> bool:
        """
        Check if sensor reading matches criteria.

        Args:
            data: Sensor reading data
            criteria: Filtering criteria ("high", "critical", etc.)

        Returns:
            bool: True if reading matches criteria
        """
        if not isinstance(data, dict):
            return False

        if criteria == "high" and data.get("temp", 0) > 30:
            return True
        if criteria == "critical" and data.get("temp", 0) > 40:
            return True

        return False

    def get_stats(self) -> dict[str, str | int | float]:
        """
        Get sensor stream statistics.

        Returns:
            Dict with sensor-specific statistics including average
            temperature and total readings
        """
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        stats["total_readings"] = self._total_readings

        if self._total_readings > 0:
            stats["avg_temp"] = self._temperature_sum / self._total_readings

        return stats


class TransactionStream(DataStream):
    """
    Stream processor for financial transaction data.

    Handles financial transactions with buy/sell operations.
    Tracks operations and calculates net flow.

    Attributes:
        _stream_id: Stream identifier
        _batches_processed: Number of batches processed
        _total_items: Total transactions processed
        _total_operations: Total financial operations
        _net_flow: Net flow of transactions (positive = net buy)
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize transaction stream.

        Args:
            stream_id: Unique identifier for this transaction stream
        """
        super().__init__(stream_id)
        self._total_operations: int = 0
        self._net_flow: int = 0

    def process_batch(self, data_batch: list[Any]) -> str:
        """
        Process a batch of financial transactions.

        Args:
            data_batch: List of transaction dictionaries

        Returns:
            str: Formatted analysis of transactions

        Raises:
            ValueError: If data format is invalid
        """
        try:
            if not data_batch:
                return "No transaction data to process"

            print(f"Processing transaction batch: {data_batch}")

            operations_count = len(data_batch)
            self._batches_processed += 1
            self._total_items += operations_count
            self._total_operations += operations_count

            batch_flow = 0
            for transaction in data_batch:
                if isinstance(transaction, dict):
                    if "buy" in transaction:
                        batch_flow += transaction["buy"]
                    if "sell" in transaction:
                        batch_flow -= transaction["sell"]

            self._net_flow += batch_flow

            result = (
                f"Transaction analysis: {operations_count} operations, "
                f"net flow: {batch_flow:+d} units"
            )
            return result

        except Exception as e:
            return f"Error processing transaction batch: {e}"

    def _matches_criteria(self, data: Any, criteria: str) -> bool:
        """
        Check if transaction matches criteria.

        Args:
            data: Transaction data
            criteria: Filtering criteria ("large", "high-value", etc.)

        Returns:
            bool: True if transaction matches criteria
        """
        if not isinstance(data, dict):
            return False

        if criteria == "large":
            buy_val = data.get("buy", 0)
            sell_val = data.get("sell", 0)
            return max(buy_val, sell_val) > 100

        return False

    def get_stats(self) -> dict[str, str | int | float]:
        """
        Get transaction stream statistics.

        Returns:
            Dict with transaction-specific statistics including net flow
            and total operations
        """
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        stats["total_operations"] = self._total_operations
        stats["net_flow"] = self._net_flow
        return stats


class EventStream(DataStream):
    """
    Stream processor for system event data.

    Handles system events such as logins, logouts, and errors.
    Tracks events and counts errors.

    Attributes:
        _stream_id: Stream identifier
        _batches_processed: Number of batches processed
        _total_items: Total events processed
        _total_events: Alias for total_items
        _error_count: Number of error events detected
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize event stream.

        Args:
            stream_id: Unique identifier for this event stream
        """
        super().__init__(stream_id)
        self._total_events: int = 0
        self._error_count: int = 0

    def process_batch(self, data_batch: list[Any]) -> str:
        """
        Process a batch of system events.

        Args:
            data_batch: List of event data

        Returns:
            str: Formatted analysis of events

        Raises:
            ValueError: If data format is invalid
        """
        try:
            if not data_batch:
                return "No event data to process"

            print(f"Processing event batch: {data_batch}")

            events_count = len(data_batch)
            self._batches_processed += 1
            self._total_items += events_count
            self._total_events += events_count

            batch_errors = 0
            for event in data_batch:
                if isinstance(event, str) and "error" in event.lower():
                    batch_errors += 1
                    self._error_count += 1

            error_text = (
                f"{batch_errors} error detected"
                if batch_errors == 1
                else f"{batch_errors} errors detected"
            )

            if batch_errors > 0:
                result = f"Event analysis: {events_count} events, {error_text}"
            else:
                result = f"Event analysis: {events_count} events processed"

            return result

        except Exception as e:
            return f"Error processing event batch: {e}"

    def _matches_criteria(self, data: Any, criteria: str) -> bool:
        """
        Check if event matches criteria.

        Args:
            data: Event data
            criteria: Filtering criteria ("error", "critical", etc.)

        Returns:
            bool: True if event matches criteria
        """
        if criteria == "error" and isinstance(data, str):
            return "error" in data.lower()

        return False

    def get_stats(self) -> dict[str, str | int | float]:
        """
        Get event stream statistics.

        Returns:
            Dict with event-specific statistics including error count
        """
        stats = super().get_stats()
        stats["type"] = "System Events"
        stats["total_events"] = self._total_events
        stats["error_count"] = self._error_count
        return stats


class StreamProcessor:
    """
    Orchestrates processing of multiple stream types.

    Manages a collection of DataStream instances and processes them
    polymorphically through their common interface. Demonstrates
    composition pattern.

    Attributes:
        _streams: List of managed streams
    """

    def __init__(self) -> None:
        """Initialize the stream processor with empty stream list."""
        self._streams: list[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """
        Add a stream to be managed.

        Args:
            stream: DataStream instance to add
        """
        self._streams.append(stream)

    def process_all(self, data_map: dict[str, list[Any]]) -> dict[str, str]:
        """
        Process data for all managed streams.

        Args:
            data_map: Dictionary mapping stream IDs to data batches

        Returns:
            Dict mapping stream IDs to processing results
        """
        results = {}

        for stream in self._streams:
            stream_data = data_map.get(stream._stream_id, [])
            if stream_data:
                result = stream.process_batch(stream_data)
                results[stream._stream_id] = result

        return results

    def get_all_stats(self) -> list[dict[str, str | int | float]]:
        """
        Get statistics for all managed streams.

        Returns:
            List of statistics dictionaries for each stream
        """
        return [stream.get_stats() for stream in self._streams]


def demonstrate_polymorphism() -> None:
    """
    Demonstrate polymorphic stream processing.

    Creates multiple stream types and processes them through a unified
    interface, showcasing how different streams handle their data while
    maintaining interface consistency.

    Demonstrates:
        - Polymorphic batch processing
        - Stream-specific filtering
        - Statistical aggregation
    """
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    # Create individual streams
    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    # Add them to processor for polymorphic handling
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    # Prepare data for all streams
    data_map = {
        "SENSOR_001": [
            {"temp": 22.5, "humidity": 65},
            {"temp": 23.0, "humidity": 64},
        ],
        "TRANS_001": [{"buy": 100}, {"sell": 150}, {"buy": 75}, {"buy": 50}],
        "EVENT_001": ["login", "logout", "data_update"],
    }

    # Process all streams polymorphically - ONE CALL!
    results = processor.process_all(data_map)

    # Display results using direct stream references
    print("\nBatch 1 Results:")
    print(f"- Sensor data: {sensor._total_items} readings processed")
    print(
        f"- Transaction data: {transaction._total_items} operations processed"
    )
    print(f"- Event data: {event._total_items} events processed")

    # Demonstrate filtering capability
    print("\nStream filtering active: High-priority data only")
    high_temp_data = [
        {"temp": 35.0, "humidity": 70},
        {"temp": 22.0, "humidity": 65},
    ]
    filtered = sensor.filter_data(high_temp_data, criteria="high")
    print(f"Filtered results: {len(filtered)} critical sensor alerts")


def main() -> None:
    """
    Main entry point for polymorphic stream system demonstration.

    Demonstrates:
        1. Individual stream initialization and processing
        2. Batch processing with different data types
        3. Stream-specific analysis
        4. Polymorphic processing through common interface
        5. Filtering capabilities

    The output showcases how different streams handle their respective
    data types while maintaining a consistent processing interface.
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    sensor = SensorStream("SENSOR_001")
    sensor_result = sensor.process_batch(
        [{"temp": 22.5, "humidity": 65, "pressure": 1013}]
    )
    print(sensor_result)

    print("\nInitializing Transaction Stream...")
    print("Stream ID: TRANS_001, Type: Financial Data")
    transaction = TransactionStream("TRANS_001")
    transaction_result = transaction.process_batch(
        [{"buy": 100}, {"sell": 150}, {"buy": 75}]
    )
    print(transaction_result)

    print("\nInitializing Event Stream...")
    print("Stream ID: EVENT_001, Type: System Events")
    event = EventStream("EVENT_001")
    event_result = event.process_batch(["login", "error", "logout"])
    print(event_result)

    demonstrate_polymorphism()

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
