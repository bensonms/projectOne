"""
Main module for Project One.
"""
import argparse


def add_numbers(a, b):
    """Add two numbers together and return the result.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


class Logger:
    """Simple logger class."""
    def log(self, message):
        """Log a message."""
        print(message)

class Calculator:
    """Calculator class that uses dependency injection."""
    def __init__(self, logger):
        """Initialize the calculator with a logger."""
        self.logger = logger
    
    def add(self, a, b):
        """Add two numbers and log the operation."""
        result = a + b
        self.logger.log(f"Added {a} and {b} to get {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract b from a and log the operation."""
        result = a - b
        self.logger.log(f"Subtracted {b} from {a} to get {result}")
        return result


def run(verbose=False):
    """Run the main function of the project.
    
    Args:
        verbose: If True, print additional information
    """
    print("Project One is running!")
    if verbose:
        print("Running in verbose mode")


def main():
    """Parse command line arguments and execute the program."""
    parser = argparse.ArgumentParser(description="Project One CLI")
    parser.add_argument("-v", "--verbose", action="store_true", 
                        help="Enable verbose output")
    args = parser.parse_args()
    
    run(verbose=args.verbose)


if __name__ == "__main__":
    main()
