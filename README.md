# VITYARTHI_PROJECT_PASSWORD_STRENGTH_DETECTION

🔐 Python Password Strength Checker

This is a simple, standalone graphical application built using Python's tkinter library. It allows users to input a password and instantly assesses its strength based on a set of common security criteria, providing real-time feedback on how to improve it.

✨ Features

Real-time Assessment: Instantly checks the strength of the entered password.

Detailed Feedback: Provides actionable steps and criteria that the password is missing (e.g., "Add special characters").

Password Masking: The password input field masks the characters by default (show="*").

Visibility Toggle: Includes a "Show Password" checkbox to easily toggle character visibility for checking input accuracy.

🛠 Strength Criteria

The password is scored out of 5, with each criterion adding 1 point to the score:

Minimum Length: Must be at least 8 characters long.

Uppercase Letters: Must contain at least one uppercase letter (A-Z).

Lowercase Letters: Must contain at least one lowercase letter (a-z).

Numbers: Must contain at least one digit (0-9).

Special Characters: Must contain at least one special character (e.g., !@#$%^&*).

Strength Levels:
| Score | Status | Color |
| :---: | :---: | :---: |
| 5/5 | STRONG PASSWORD | Green |
| 3-4/5 | MEDIUM STRENGTH | Orange |
| 0-2/5 | WEAK PASSWORD | Red |

🚀 How to Run

1. Requirements

This application requires Python 3.x. The tkinter library is usually included with standard Python installations.

2. Save the Code

Save the provided Python code into a single file named password_checker.py.

3. Execution

Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script:

python password_checker.py


The graphical user interface (GUI) window will open, ready for you to test your passwords!

💡 Code Structure

The application is structured within a single class, PasswordStrengthChecker, which handles all GUI layout and logic:

__init__(self, root): Sets up the main window and all UI components (labels, entry box, checkbox, buttons).

toggle_password(self): Linked to the checkbox, it changes the show property of the entry field to hide or display the password characters.

check_strength(self): Contains the core logic, using regular expressions (re module) to evaluate the password against the five criteria and calculate the score.

update_ui(self, score, feedback, length): Responsible for updating the result and feedback labels with the appropriate text and color based on the calculated score.