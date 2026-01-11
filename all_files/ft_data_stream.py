"""
Data Quest - Exercise 5: Stream Wizard
This module demonstrates generator operations for memory-efficient data
streaming. Processes game events on-demand using yield, showcases generator
expressions, and compares streaming vs storing approaches.

Functions:
    game_event_stream: Generate game events on-demand
    filter_high_level: Filter events for high-level players
    fibonacci_generator: Generate Fibonacci sequence
    prime_generator: Generate prime numbers
    main: Demonstrate streaming data processing with generators

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-11)
"""

import time


def game_event_stream(count):
    """
    Generate game events on-demand without storing them in memory.
    
    Args:
        count: Number of events to generate
        
    Yields:
        dict: Event dictionary with player, level, and action
        
    Examples:
        >>> gen = game_event_stream(3)
        >>> next(gen)
        {'event_id': 1, 'player': 'alice', 'level': 5, 'action': 'killed monster'}
    """
    players = ['alice', 'bob', 'charlie', 'diana']
    actions = ['killed monster', 'found treasure', 'leveled up', 'completed quest']
    
    for i in range(count):
        player_index = i % len(players)
        action_index = i % len(actions)
        level = ((i * 7) % 20) + 1
        
        event = {
            'event_id': i + 1,
            'player': players[player_index],
            'level': level,
            'action': actions[action_index]
        }
        
        yield event


def filter_high_level(event_stream, min_level):
    """
    Filter event stream for high-level players.
    
    Args:
        event_stream: Generator yielding events
        min_level: Minimum level threshold
        
    Yields:
        dict: Filtered events with level >= min_level
    """
    for event in event_stream:
        if event['level'] >= min_level:
            yield event


def fibonacci_generator(count):
    """
    Generate Fibonacci sequence.
    
    Args:
        count: Number of Fibonacci numbers to generate
        
    Yields:
        int: Next Fibonacci number
    """
    a = 0
    b = 1
    generated = 0
    
    while generated < count:
        yield a
        temp = a
        a = b
        b = temp + b
        generated += 1


def prime_generator(count):
    """
    Generate prime numbers.
    
    Args:
        count: Number of primes to generate
        
    Yields:
        int: Next prime number
    """
    primes_found = 0
    candidate = 2
    
    while primes_found < count:
        is_prime = True
        
        test_divisor = 2
        while test_divisor < candidate:
            if candidate % test_divisor == 0:
                is_prime = False
                break
            test_divisor += 1
        
        if is_prime:
            yield candidate
            primes_found += 1
        
        candidate += 1


def main():
    """
    Demonstrate streaming data processing with generators.
    
    Showcases yield, next(), iter(), for loops, and memory-efficient
    processing of large datasets without storing everything in memory.
    
    Returns:
        None: Prints streaming demonstrations directly to stdout
    """
    print("=== Game Data Stream Processor ===")
    print()
    
    total_events = 1000
    print(f"Processing {total_events} game events...")
    print()
    
    event_stream = game_event_stream(total_events)
    event_iterator = iter(event_stream)
    
    event1 = next(event_iterator)
    print(f"Event {event1['event_id']}: Player {event1['player']} "
          f"(level {event1['level']}) {event1['action']}")
    
    event2 = next(event_iterator)
    print(f"Event {event2['event_id']}: Player {event2['player']} "
          f"(level {event2['level']}) {event2['action']}")
    
    event3 = next(event_iterator)
    print(f"Event {event3['event_id']}: Player {event3['player']} "
          f"(level {event3['level']}) {event3['action']}")
    
    print("...")
    print()
    
    print("=== Stream Analytics ===")
    
    start_time = time.time()
    
    analytics_stream = game_event_stream(total_events)
    
    total_processed = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0
    
    for event in analytics_stream:
        total_processed += 1
        
        if event['level'] >= 10:
            high_level_count += 1
        
        if event['action'] == 'found treasure':
            treasure_count += 1
        
        if event['action'] == 'leveled up':
            levelup_count += 1
    
    end_time = time.time()
    processing_time = end_time - start_time
    
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")
    print()
    
    print("=== Generator Demonstration ===")
    
    fib_stream = fibonacci_generator(10)
    fib_numbers = []

    while True:
        try:
            fib_num = next(fib_stream)
            fib_numbers.append(str(fib_num))
        except StopIteration:
            break

    fib_output = ", ".join(fib_numbers)
    
    print(f"Fibonacci sequence (first {len(fib_numbers)}): {fib_output}")
    
    prime_stream = prime_generator(5)
    prime_iterator = iter(prime_stream)
    
    prime_numbers = []
    prime1 = next(prime_iterator)
    prime_numbers.append(prime1)
    
    prime2 = next(prime_iterator)
    prime_numbers.append(prime2)
    
    prime3 = next(prime_iterator)
    prime_numbers.append(prime3)
    
    prime4 = next(prime_iterator)
    prime_numbers.append(prime4)
    
    prime5 = next(prime_iterator)
    prime_numbers.append(prime5)
    
    prime_strings = []
    for prime in prime_numbers:
        prime_strings.append(str(prime))
    prime_output = ", ".join(prime_strings)
    
    print(f"Prime numbers (first {len(prime_numbers)}): {prime_output}")


if __name__ == "__main__":
    main()
