from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz :QuizBrain):
        self.window = Tk()
        self.quiz = quiz
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_image, highlightcolor=THEME_COLOR, highlightthickness=0,command=self.correct)
        self.correct_button.grid(column=0, row=2)
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightcolor=THEME_COLOR, highlightthickness=0,command=self.wrong)
        self.wrong_button.grid(column=1, row=2)
        self.canvas_text = self.canvas.create_text(150, 125,
                                                   text="insert text",
                                                   width=280,
                                                   font=("Arial", 20, "italic"),
                                                   fill=THEME_COLOR)
        self.score_label = Label(text="score: 0", foreground="White",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def correct(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
