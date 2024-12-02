```mermaid

classDiagram

    class Teacher {
        +String: name
        +String: surname
        +String: instrument
    }

    class Student {
        +String: name
        +String: surname
        +List<Course>: courses
        +Teacher: teacher
        +void: set_teacher(Teacher: teacher)
        +void: enroll_course(Course: course)
    }

    class Course {
        +String: name
        +String: duration
        +List<Student>: students
    }
    
    Teacher "1" -- "n" Student : teaches
    Student "1" -- "n" Course : enrolled in
    Course "n" -- "n" Student : includes
```