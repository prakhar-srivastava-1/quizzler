from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        # add padding and background color
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # add score label
        self.scoreboard_label = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.scoreboard_label.grid(row=0, column=1)

        # add question canvas
        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Dummy Text question?", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # add buttons
        # true button
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0)
        self.true_btn.grid(row=2, column=0)

        # false button
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0)
        self.false_btn.grid(row=2, column=1)



        self.window.mainloop()
