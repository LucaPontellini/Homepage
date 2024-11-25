```mermaid

classDiagram

    class Doctor {
        +String: name
        +String: surname
        +String: specialization
    }
    class Drugs {
        +String: name
        +Float: dose
    }
    class Hospital {
        +String: name
        +String: address
        +List<department>: departments
    }
    class Department {
        +String: name
        +List<doctor>: doctors
        +List<patient>: patients 
    }
    class Patients {
        +String: name
        +String: surname
        +Int: date_of_birth
    }
    class Nurses {
        +String: name
        +String: surname
        +String: work_shift
    }
    class Medical_record {
        +List<medical_examination>: medical_examinations
    }
    class Medical_examination {
        +String:
    }