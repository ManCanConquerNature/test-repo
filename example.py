#!/usr/bin/env python3
"""
Example Python Script for Test Repository

This is a simple example script to demonstrate basic Python operations.
"""

def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}! Welcome to the test repository."


def fibonacci(n: int) -> list:
    """Generate the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def main():
    """Main function to demonstrate the scripts capabilities."""
    print("=" * 50)
    print("Example Python Script")
    print("=" * 50)
    
    # Greeting
    user_name = "World"
    print(greet(user_name))
    print()
    
    # Fibonacci demo
    print("First 10 Fibonacci numbers:")
    fib_nums = fibonacci(10)
    print(fib_nums)
    print()
    
    print("All done! Thanks for using the test repo.")
    print("=" * 50)


if __name__ == "__main__":
    main()
