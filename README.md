# Student Attendance Management System using Facial Recognition

This project implements a **Student Attendance Management System** leveraging **facial recognition technology** to streamline the process of tracking and managing attendance in educational institutions.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Introduction

The **Student Attendance Management System** automates the traditional attendance tracking process. By using facial recognition, the system ensures:
- **Accuracy** in identifying students.
- **Efficiency** in marking attendance.
- **Convenience** for both educators and students.

This system eliminates manual errors, reduces time consumption, and prevents proxy attendance.

---

## Features

- **Facial Recognition**: Identify and verify students using their facial data.
- **Real-time Attendance Marking**: Automatically record attendance upon face detection.
- **Database Integration**: Store attendance records securely.
- **User-friendly Interface**: Simple and intuitive GUI for students and administrators.
- **Attendance Reports**: Generate daily, weekly, or monthly attendance reports.

---

## Technologies Used

### Programming Languages and Tools:
- **Python**: Core programming language.
- **OpenCV**: For face detection and recognition.
- **Tkinter**: GUI framework for the application interface.
- **MySQL**: Database for storing attendance records.

---

## Setup and Installation

### Prerequisites:
1. Python 3.x installed on your system.
2. MySQL Server with appropriate permissions.
3. Required Python libraries:
   - OpenCV
   - PIL (Pillow)
   - Tkinter
   - MySQL Connector

### Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Drag0nSlay/Student-Attendance-Management-System.git
   cd Student-Attendance-Management-System
2. Install required dependencies:
   ```bash
   pip install opencv-python mysql-connector-python pillow
3. Set up the database:

- **Create a MySQL database and import the provided SQL script (database.sql) to set up tables.**
- **Update the database configuration in the code (db_config section) with your MySQL credentials.**

4. Run the application:
   ```bash
   python main.py
### Usage:
1. Add Students: Register students' facial data via the system interface.
2. Mark Attendance: The system detects and recognizes students as they appear before the camera.
3. View Attendance Records: Administrators can access and manage attendance logs.

### Folder Structure
```bash
Student-Attendance-Management-System/
│
├── Images/                # Folder for storing student face images
├── SQL/                   # Database setup scripts
├── main.py                # Entry point for the application
├── attendance.py          # Core logic for attendance marking
├── database.py            # Database connectivity and operations
├── gui.py                 # GUI implementation using Tkinter
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

### FUTURE IMPROVEMENTS
- **Mobile App Integration: Extend the system to mobile platforms for more convenience.**
- **Cloud Storage: Use cloud services for attendance data storage.**
- **Enhanced Security: Add multi-factor authentication for admins.**
- **Advanced Analytics: Provide insights into attendance trends using data visualization tools.**

## License

This project is licensed under the **MIT License**.

You can view the full license text in the [LICENSE](LICENSE) file in this repository.

## Contributing
Feel free to contribute to this project by raising issues or submitting pull requests. Together, we can make it even better! 😊

## Author
Drag0nSlay(Aman Kothari)<br>
Developer and creator of this project.
