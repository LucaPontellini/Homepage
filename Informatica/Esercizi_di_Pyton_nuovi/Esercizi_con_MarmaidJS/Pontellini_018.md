```mermaid

classDiagram
    
    class Coach {
        +String: name
        +String: surname
        +String: specialization
    }

    class Members {
        +String: name
        +String: surname
        +List<course>: courses
    }

    class Course {
        +String: name
        +Int: duration
    }

    class Training_Schedule {
        +List<exercise>: exercises
        +List<description>: descriptions
    }

Coach "1" -- "n" Members : train
Members "n" -- "n" Course : enrollment
Coach "1" -- "n" Course : holds
Members "1" -- "1" Training_Schedule : has