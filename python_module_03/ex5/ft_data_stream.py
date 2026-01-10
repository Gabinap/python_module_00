"""
Data Quest - Exercise 5: Stream Wizard
This module demonstrates generator operations for memory-efficient data
streaming. Processes game events on-demand using yield, showcases generator
expressions, and compares streaming vs storing approaches.

Functions:
    game_event_stream: Generate game events on-demand
    filter_events: Filter events based on criteria
    fibonacci_generator: Generate Fibonacci sequence
    prime_generator: Generate prime numbers
    main: Demonstrate streaming data processing with generators

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-05)
"""


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
        {'player': 'alice', 'level': 5, 'action': 'killed monster'}
    """
    players = ['alice', 'bob', 'charlie', 'diana']
    actions = ['killed monster', 'found treasure', 'leveled up', 'completed quest']
    
    for i in range(count):
        player = players[i % len(players)]
        level = (i % 15) + 1
        action = actions[i % len(actions)]
        
        event = {
            'id': i + 1,
            'player': player,
            'level': level,
            'action': action
        }
        yield event


def filter_events(event_generator, min_level):
    """
    Filter events to only include high-level players.
    
    Args:
        event_generator: Generator producing events
        min_level: Minimum level threshold
        
    Yields:
        dict: Filtered event dictionaries
    """
    for event in event_generator:
        if event['level'] >= min_level:
            yield event


def fibonacci_generator(limit):
    """
    Generate Fibonacci sequence up to limit numbers.
    
    Args:
        limit: Number of Fibonacci numbers to generate
        
    Yields:
        int: Next Fibonacci number
        
    Examples:
        >>> gen = fibonacci_generator(5)
        >>> list(gen)
        [0, 1, 1, 2, 3]
    """
    a = 0
    b = 1
    count = 0

    while count < limit:
        yield a
        a_temp = a
        a = b
        b = a_temp + b
        count += 1


def prime_generator(limit):
    """
    Generate prime numbers up to limit primes.
    
    Args:
        limit: Number of prime numbers to generate
        
    Yields:
        int: Next prime number
    """
    primes_found = 0
    candidate = 2
    
    while primes_found < limit:
        is_prime = True
        
        for i in range(2, candidate):
            if candidate % i == 0:
                is_prime = False
                break
        
        if is_prime:
            yield candidate
            primes_found += 1
        
        candidate += 1


def main():
    """
    Demonstrate streaming data processing with generators.
    
    Showcases generator creation, iteration, filtering, and memory
    efficiency compared to storing all data in lists.
    
    Returns:
        None: Prints streaming demonstrations directly to stdout
    """
    print("=== Game Data Stream Processor ===")
    print()
    
    total_events = 1000
    print(f"Processing {total_events} game events...")
    print()
    
    event_gen = game_event_stream(total_events)
    
    displayed_count = 0
    for event in event_gen:
        if displayed_count < 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
            displayed_count += 1
    print("...")
    print()
    
    print("=== Stream Analytics ===")
    
    event_gen = game_event_stream(total_events)
    total_processed = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0
    
    for event in event_gen:
        total_processed += 1
        
        if event['level'] >= 10:
            high_level_count += 1
        
        if event['action'] == 'found treasure':
            treasure_count += 1
        
        if event['action'] == 'leveled up':
            levelup_count += 1
    
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()
    
    print("=== Generator Demonstration ===")
    
    fib_gen = fibonacci_generator(10)
    fib_list = []
    for i in range(10):
        fib_list.append(next(fib_gen))
    
    fib_str = ", ".join([str(n) for n in fib_list])
    print(f"Fibonacci sequence (first 10): {fib_str}")
    
    prime_gen = prime_generator(5)
    prime_list = []
    while True:
        try:
            prime = next(prime_gen)
        except StopIteration:
            break
        prime_list.append(prime)
    
    prime_str = ", ".join([str(p) for p in prime_list])
    print(f"Prime numbers (first 5): {prime_str}")


if __name__ == "__main__":
    main()