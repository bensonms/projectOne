"""
Calculator module providing arithmetic operations with logging.
"""

class Calculator:
    """
    A calculator class that performs basic arithmetic operations
    and logs the operations performed.
    """
    
    def __init__(self, logger):
        """
        Initialize Calculator with a logger.
        
        Args:
            logger: An object with a log method for logging operations
        """
        self.logger = logger
        
    def add(self, a, b):
        """
        Add two numbers and log the operation.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        result = a + b
        self.logger.log(f"Added {a} and {b} to get {result}")
        return result
        
    def subtract(self, a, b):
        """
        Subtract b from a and log the operation.
        
        Args:
            a: Number to subtract from
            b: Number to subtract
            
        Returns:
            Result of a - b
        """
        result = a - b
        self.logger.log(f"Subtracted {b} from {a} to get {result}")
        return result
