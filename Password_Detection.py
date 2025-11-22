import tkinter as tk
from tkinter import messagebox
import re

class PasswordStrengthChecker:
    def __init__(self, root):
        """
        Initialize the GUI application.
        """
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("400x350") # Increased height slightly to fit the new button
        self.root.resizable(False, False)

        # --- UI COMPONENTS ---

        # Title Label
        self.title_label = tk.Label(
            root, 
            text="Check Your Password Strength", 
            font=("Helvetica", 14, "bold"),
            pady=15
        )
        self.title_label.pack()

        # Password Entry Label
        self.pass_label = tk.Label(root, text="Enter Password:")
        self.pass_label.pack()

        # Entry Box 
        # show="*" is the default, but we can change this dynamically
        self.password_entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        # --- NEW FEATURE: SHOW PASSWORD CHECKBOX ---
        self.show_pass_var = tk.IntVar() # Variable to track checkbox state (0 or 1)
        self.show_pass_check = tk.Checkbutton(
            root, 
            text="Show Password", 
            variable=self.show_pass_var, 
            command=self.toggle_password # Calls function when clicked
        )
        self.show_pass_check.pack()
        # -------------------------------------------

        # Check Button
        self.check_button = tk.Button(
            root, 
            text="Check Strength", 
            command=self.check_strength, 
            bg="#007bff", 
            fg="white", 
            font=("Arial", 10, "bold")
        )
        self.check_button.pack(pady=15)

        # Result Label 
        self.result_label = tk.Label(
            root, 
            text="", 
            font=("Helvetica", 12, "bold")
        )
        self.result_label.pack()

        # Feedback Label
        self.feedback_label = tk.Label(
            root, 
            text="", 
            fg="gray", 
            font=("Arial", 9)
        )
        self.feedback_label.pack(pady=5)

    def toggle_password(self):
        """
        Toggles the visibility of the password characters.
        """
        if self.show_pass_var.get() == 1:
            # If checkbox is checked, remove the masking character
            self.password_entry.config(show="")
        else:
            # If unchecked, mask characters with asterisk
            self.password_entry.config(show="*")

    def check_strength(self):
        """
        Logic to determine password strength.
        """
        password = self.password_entry.get()
        score = 0
        feedback_messages = []

        if len(password) >= 8:
            score += 1
        else:
            feedback_messages.append("- Make it at least 8 characters long")

        if re.search(r"[A-Z]", password):
            score += 1
        else:
            feedback_messages.append("- Add uppercase letters (A-Z)")

        if re.search(r"[a-z]", password):
            score += 1
        else:
            feedback_messages.append("- Add lowercase letters (a-z)")

        if re.search(r"[0-9]", password):
            score += 1
        else:
            feedback_messages.append("- Add numbers (0-9)")

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            feedback_messages.append("- Add special characters (@, #, $, etc.)")

        self.update_ui(score, feedback_messages, len(password))

    def update_ui(self, score, feedback, length):
        """
        Updates the result labels based on score.
        """
        if length == 0:
            self.result_label.config(text="Please enter a password", fg="black")
            self.feedback_label.config(text="")
            return

        if score == 5:
            self.result_label.config(text="STRONG PASSWORD", fg="green")
            self.feedback_label.config(text="Great job!")
        elif score >= 3:
            self.result_label.config(text="MEDIUM STRENGTH", fg="orange")
            self.feedback_label.config(text="\n".join(feedback))
        else:
            self.result_label.config(text="WEAK PASSWORD", fg="red")
            self.feedback_label.config(text="\n".join(feedback))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()