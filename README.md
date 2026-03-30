# unknownapp

This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----

## Use Case Diagram

```mermaid
graph TD
    User --> AddData
    User --> ViewData
    User --> DeleteData
    User --> Exit
```

## Flowchart of the main workflow

```mermaid
flowchart TD
    Start([Start]) --> Menu{Main Menu}
    Menu -->|1| Add["Add Data"]
    Menu -->|2| View["View Data"]
    Menu -->|3| Delete["Delete Data"]
    Menu -->|4| Exit([Exit])
    
    Add --> Menu
    View --> Menu
    Delete --> Menu
```

## Prompts

- Convert Java menu-based program to Python
- Create simple list-based data storage in Python
- Implement add and view functionality
