# project.py

from datetime import datetime

class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)

    def __repr__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%"

    def is_complete(self):
        """Check if the project is complete."""
        return self.completion == 100

    def update(self, completion=None, priority=None):
        """Update the project's completion and/or priority."""
        if completion is not None:
            self.completion = int(completion)
        if priority is not None:
            self.priority = int(priority)
