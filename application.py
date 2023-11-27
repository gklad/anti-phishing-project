import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random
import json
from questions import questions

class AntiPhishingApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Anti-Phishing Educator")
        ctk.set_default_color_theme("green")
        self.geometry("350x250")

        # Login screen
        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack(fill='both', expand=True)

        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Employee ID")
        self.username_entry.pack(pady=20)

        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=20)

        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.on_login)
        self.login_button.pack(pady=20)

        self.creator_label_login = ctk.CTkLabel(self.login_frame, text="Created by Grigorios Kladakis")
        self.creator_label_login.pack(side='bottom')

    def on_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "13902972" and password == "test":
            self.initialize_tool(username)
            self.geometry("700x500")
        else:
            messagebox.showerror("Login Failed", "Incorrect Employee ID or password.")

    def initialize_tool(self, username):
        self.login_frame.pack_forget()
        self.score = 0

        self.label = ctk.CTkLabel(self, text="Welcome to the Anti-Phishing Educator!", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.question_label = ctk.CTkLabel(self, text="", font=("Helvetica", 12))
        self.question_label.pack(pady=20)

        self.creator_label_app = ctk.CTkLabel(self, text="Created by Grigorios Kladakis")
        self.creator_label_app.pack(side='bottom', anchor='w')

        self.options = []
        for i in range(4):
            btn = ctk.CTkButton(self, text="", command=lambda i=i: self.check_answer(i))
            btn.pack(pady=10)
            self.options.append(btn)

        self.explanation_label = ctk.CTkLabel(self, text="", font=("Helvetica", 10))
        self.explanation_label.pack(pady=20)

        self.next_button = ctk.CTkButton(self, text="Next Question", command=self.load_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if questions:  # Ensure the questions list is not empty
            self.current_question = random.choice(questions)
            self.question_label.configure(text=self.current_question["question"])
            for i, option in enumerate(self.current_question["options"]):
                self.options[i].configure(text=option)
            self.explanation_label.configure(text="")
            self.next_button.pack_forget()

    def check_answer(self, i):
        correct = i == int(self.current_question["correct_answer"]) - 1
        if correct:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done. The explanation can be found below.")
            self.explanation_label.configure(text=self.current_question["explanation"], wraplength=500)
            self.next_button.pack(pady=20)

            if self.score == 8:
                self.complete_quiz()
        else:
            messagebox.showinfo("Incorrect", "Please read the question carefully and try again.")
            self.explanation_label.configure(text="")
            self.next_button.pack_forget()

    def complete_quiz(self):
        for widget in self.winfo_children():
            widget.pack_forget()

        self.geometry("300x150")

        completion_label = ctk.CTkLabel(self, text="Thank you for completing the daily quiz!", font=("Helvetica", 14))
        completion_label.pack(pady=20)

        exit_button = ctk.CTkButton(self, text="Exit Application", command=self.quit)
        exit_button.pack(pady=20)

if __name__ == "__main__":
    app = AntiPhishingApp()
    app.mainloop()
