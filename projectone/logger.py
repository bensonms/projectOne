"""
Logger module for logging operations.
"""

class Logger:
    """
    Logger class for storing and retrieving log messages.
    """
    
    def __init__(self):
        """Initialize an empty log storage."""
        self.logs = []
        
    def log(self, message):
        """
        Log a message.
        
        Args:
            message: The message to log
        """
        self.logs.append(message)
        
    def get_logs(self):
        """
        Get all logs.
        
        Returns:
            List of log messages
        """
        return self.logs
