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

    class Corse {
        +String: name
        +Int: duration
    }

    class Training_Schedule {
        +List<exercise>: exercises
        +List<description>: descriptions
    }

Coach "1" -- "n" Members : train
Members "n" -- "n" Corse : enrollment
Coach "1" -- "n" Corse : holds
Members "1" -- "1" Training_Schedule : has