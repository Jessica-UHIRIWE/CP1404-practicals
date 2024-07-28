"""
 Estimated Time: 45 minutes
 Current Time: 3:13pm
 Finished time: 3:45pm
 Actual time taken: 32 minutes
"""

class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name="", typing="", reflection="", year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed, otherwise False."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of a Programming Language object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
