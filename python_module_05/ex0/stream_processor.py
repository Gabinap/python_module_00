#!/usr/bin/env python3
"""
Code Nexus - Data Processor Foundation (Exercise 0).

This module implements a polymorphic data processing system demonstrating
method overriding and subtype polymorphism through specialized processors.

Architecture:
    - DataProcessor: Abstract base class defining the processing interface
    - NumericProcessor: Handles numeric data (lists of numbers)
    - TextProcessor: Handles text data (strings)
    - LogProcessor: Handles log entries with custom formatting

Key Concepts Demonstrated:
    - Abstract Base Classes (ABC) for interface definition
    - Method overriding for behavioral specialization
    - Template Method pattern (format_output can be overridden)
    - Polymorphic processing through common interfaces
    - Dynamic dispatch without isinstance checks

Type Hints:
    All functions use comprehensive type annotations from the typing module
    including Any for polymorphic data handling and List for collections.

Standards:
    - Python 3.10+
    - flake8 compliant
    - Comprehensive type annotations
    - Exception handling for data validation

Author: gagulhon
Version: 1.0
"""

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    Abstract base class for data processors.

    Defines the common interface that all data processors must implement.
    Uses the Template Method pattern where format_output() provides a
    default implementation that can be optionally overridden.

    Abstract Methods:
        process: Process data and return formatted result string
        validate: Validate if data is appropriate for this processor

    Concrete Methods:
        format_output: Format the output string (can be overridden)

    Note:
        Cannot be instantiated directly. Subclasses must implement all
        abstract methods.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the given data and return a formatted result.

        Args:
            data: Input data of any type to be processed

        Returns:
            str: Formatted processing result

        Raises:
            ValueError: If data fails validation
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate if the data is appropriate for this processor.

        Args:
            data: Input data to validate

        Returns:
            bool: True if data is valid for this processor, False otherwise
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Format the output string with default formatting.

        This method provides a default implementation but can be overridden
        by subclasses that require specialized formatting.

        Args:
            result: The result string to format

        Returns:
            str: Formatted output string with "Output: " prefix
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Processor specialized for numeric data.

    Handles lists of numeric values (int or float) and provides
    statistical analysis including sum and average calculations.

    Attributes:
        _processed_count: Number of data batches processed
    """

    def __init__(self) -> None:
        """Initialize the numeric processor."""
        self._processed_count: int = 0

    def validate(self, data: Any) -> bool:
        """
        Validate that data is a list containing only numeric values.

        Args:
            data: Data to validate

        Returns:
            bool: True if data is a list of numbers, False otherwise
        """
        if not isinstance(data, list):
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        """
        Process numeric data and calculate statistics.

        Calculates the sum and average of the numeric values and
        returns a formatted result string.

        Args:
            data: List of numeric values to process

        Returns:
            str: Formatted processing result with statistics

        Raises:
            ValueError: If data validation fails
        """
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")

            print(f"Processing data: {data}")
            print("Validation: Numeric data verified")

            total = sum(data)
            avg = total / len(data) if len(data) > 0 else 0
            self._processed_count += 1

            result = (
                f"Processed {len(data)} numeric values, sum={total}, avg={avg}"
            )
            return self.format_output(result)

        except Exception as e:
            return f"Error processing numeric data: {e}"


class TextProcessor(DataProcessor):
    """
    Processor specialized for text data.

    Handles string data and provides text analysis including
    character count and word count.

    Attributes:
        _processed_count: Number of text entries processed
    """

    def __init__(self) -> None:
        """Initialize the text processor."""
        self._processed_count: int = 0

    def validate(self, data: Any) -> bool:
        """
        Validate that data is a string.

        Args:
            data: Data to validate

        Returns:
            bool: True if data is a string, False otherwise
        """
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        """
        Process text data and analyze content.

        Analyzes the text by counting characters and words,
        then returns a formatted result string.

        Args:
            data: String to process

        Returns:
            str: Formatted processing result with text statistics

        Raises:
            ValueError: If data validation fails
        """
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")

            print(f'Processing data: "{data}"')
            print("Validation: Text data verified")

            char_count = len(data)
            word_count = len(data.split())
            self._processed_count += 1

            result = (
                f"Processed text: {char_count} characters, {word_count} words"
            )
            return self.format_output(result)

        except Exception as e:
            return f"Error processing text data: {e}"


class LogProcessor(DataProcessor):
    """
    Processor specialized for log entries.

    Handles log message strings, extracts log levels (ERROR, WARNING,
    INFO, DEBUG), and provides custom formatting with severity prefixes.

    Attributes:
        _processed_count: Number of log entries processed
        _log_levels: Valid log level identifiers

    Note:
        Overrides format_output() to provide custom log formatting with
        severity-based prefixes like [ALERT], [WARN], [INFO].
    """

    def __init__(self) -> None:
        """Initialize the log processor."""
        self._processed_count: int = 0
        self._log_levels: list[str] = ["ERROR", "INFO", "WARNING", "DEBUG"]

    def validate(self, data: Any) -> bool:
        """
        Validate that data is a string containing a valid log level.

        Args:
            data: Data to validate

        Returns:
            bool: True if data is a valid log entry, False otherwise
        """
        if not isinstance(data, str):
            return False
        return any(level in data.upper() for level in self._log_levels)

    def process(self, data: Any) -> str:
        """
        Process log entry and extract level information.

        Parses the log message to extract the log level and message
        content, then returns a formatted result with appropriate
        severity prefix.

        Args:
            data: Log entry string to process

        Returns:
            str: Formatted log processing result with severity prefix

        Raises:
            ValueError: If data validation fails
        """
        try:
            if not self.validate(data):
                raise ValueError("Invalid log entry")

            print(f'Processing data: "{data}"')
            print("Validation: Log entry verified")

            data_upper = data.upper()
            if "ERROR" in data_upper:
                level = "ERROR"
            elif "WARNING" in data_upper:
                level = "WARNING"
            elif "INFO" in data_upper:
                level = "INFO"
            else:
                level = "DEBUG"

            message_part = data.split(":", 1)
            message = message_part[-1].strip() if ":" in data else data

            self._processed_count += 1
            result = f"{level} level detected: {message}"
            return self.format_output(result)

        except Exception as e:
            return f"Error processing log data: {e}"

    def format_output(self, result: str) -> str:
        """
        Format log output with severity-based prefix.

        Overrides the base class method to provide custom formatting
        with brackets and severity indicators.

        Args:
            result: The result string to format

        Returns:
            str: Formatted output with severity prefix
                ([ALERT], [WARN], or [INFO])
        """
        if "ERROR" in result:
            prefix = "[ALERT]"
        elif "WARNING" in result:
            prefix = "[WARN]"
        else:
            prefix = "[INFO]"

        return f"Output: {prefix} {result}"


def demonstrate_polymorphism() -> None:
    """
    Demonstrate polymorphic processing with multiple processor types.

    Creates instances of different processor types and processes
    various data through a unified interface, showcasing subtype
    polymorphism where the same method call produces different
    behaviors based on the concrete type.

    The function illustrates:
        - Dynamic dispatch without type checking
        - Interface consistency across different implementations
        - Behavioral specialization through method overriding
    """
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    test_data: list[Any] = [[1, 2, 3], "Hello World", "INFO: System ready"]

    for i, (processor, data) in enumerate(
        zip(processors, test_data), 1
    ):
        result = processor.process(data)
        print(f"Result {i}: {result.split('Output: ')[1]}")


def main() -> None:
    """
    Main entry point for the data processor foundation demonstration.

    Demonstrates the following:
        1. Individual processor initialization and testing
        2. Validation and processing of type-specific data
        3. Polymorphic processing through common interface
        4. Method overriding for behavioral specialization

    The output shows how different processors handle their respective
    data types while maintaining interface consistency.
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numeric_proc = NumericProcessor()
    print(numeric_proc.process([1, 2, 3, 4, 5]))

    print("\nInitializing Text Processor...")
    text_proc = TextProcessor()
    print(text_proc.process("Hello Nexus World"))

    print("\nInitializing Log Processor...")
    log_proc = LogProcessor()
    print(log_proc.process("ERROR: Connection timeout"))

    demonstrate_polymorphism()

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
