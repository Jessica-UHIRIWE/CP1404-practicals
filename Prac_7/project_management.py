# project_management.py

import os
from datetime import datetime
from project import Project

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion}\n")

def display_projects(projects):
    """Display projects sorted by completion status and priority."""
    incomplete_projects = sorted([p for p in projects if not p.is_complete()], key=lambda x: x.priority)
    completed_projects = sorted([p for p in projects if p.is_complete()], key=lambda x: x.priority)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

def filter_projects_by_date(projects, date):
    """Display projects that start after a given date."""
    filtered_projects = [p for p in projects if p.start_date > date]
    filtered_projects.sort(key=lambda x: x.start_date)

    for project in filtered_projects:
        print(project)

def add_new_project():
    """Add a new project based on user input."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion = input("Percent complete: ")

    return Project(name, start_date, priority, cost_estimate, completion)

def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    project = projects[project_choice]

    print(project)

    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")

    project.update(completion=new_completion or None, priority=new_priority or None)

def main():
    """Main function to manage projects."""
    FILENAME = 'project.txt'
    # If the file is not in the same directory, provide the absolute path
    # FILENAME = 'C:/Users/user/Desktop/Trimester 2/CP 1404/Prac_7/project.txt'

    try:
        projects = load_projects(FILENAME)
        print(f"Loaded {len(projects)} projects from {FILENAME}")
    except FileNotFoundError:
        print(f"Error: The file {FILENAME} was not found.")
        return

    menu = """
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    """
    choice = ''
    while choice.lower() != 'q':
        print(menu)
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Filename to load from: ")
            try:
                projects = load_projects(filename)
            except FileNotFoundError:
                print(f"Error: The file {filename} was not found.")
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.strptime(date_string, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input(f"Would you like to save to {FILENAME}? (yes/no): ").lower()
            if save_choice == 'yes':
                save_projects(FILENAME, projects)

    print("Thank you for using custom-built project management software.")

if __name__ == "__main__":
    main()
