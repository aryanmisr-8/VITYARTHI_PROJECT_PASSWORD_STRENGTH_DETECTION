Project Title: Password Strength Checker in Python
Overview
This project is a simple command-line Python application designed to evaluate the strength of a user’s password. It checks for common security criteria such as length, the presence of uppercase and lowercase letters, digits, and special characters. The program provides actionable feedback for improving weak passwords and allows multiple attempts to achieve a strong password.

Features
Validates password length (minimum 8 characters)

Checks for uppercase letters (A-Z)

Checks for lowercase letters (a-z)

Checks for numeric digits (0-9)

Checks for special characters like !, @, #, $, etc.

Rates password strength as WEAK, MEDIUM, or STRONG

Provides tailored suggestions to improve password strength

Allows configurable retry attempts until a strong password is entered

Tools Used
Python 3.x: Programming language for the application

Any standard Python environment or IDE (such as VS Code, PyCharm, or command line)

Installation and Running the Project
Ensure Python 3.x is installed on your machine. You can download it from python.org.

Save the project code into a file, for example, password_strength_checker.py.

Open a terminal or command prompt.

Navigate to the directory containing the script.

Run the script by executing:

text
python password_strength_checker.py
Follow the on-screen prompts to enter a password and get strength feedback.

Instructions for Testing
Run the program.

Enter any password you want to test when prompted.

If the password is not strong, the program will ask how many attempts you want to retry.

Enter a stronger password on each retry attempt until you receive a "STRONG" rating or exhaust your attempts.

Observe the feedback messages to understand what you can improve in your password.

Test with various passwords to cover different cases (short passwords, passwords lacking uppercase letters, missing digits, etc.).