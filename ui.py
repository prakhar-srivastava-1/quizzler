from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        # add GUI window
        self.window = Tk()
        self.window.title("Quizzler")
        # add padding and background color
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # add score label
        self.scoreboard_label = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.scoreboard_label.grid(row=0, column=1)

        # add question canvas
        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Dummy Text question?",
                                                     font=("Arial", 16, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)  # add width to wrap text
        self.get_next_question()
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # add buttons
        # true button
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.check_true)
        self.true_btn.grid(row=2, column=0)

        # false button
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.check_false)
        self.false_btn.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            next_question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have reached the end of the quiz. "
                                        f"You got {self.quiz_brain.score} correct out of 10")

    def check_true(self):
        self.give_feedback(self.quiz_brain.check_answer("true"))

    def check_false(self):
        self.give_feedback(self.quiz_brain.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.scoreboard_label.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
