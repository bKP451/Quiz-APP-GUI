from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_object: QuizBrain):
        self.quiz_object = quiz_object
        self.window = Tk()
        self.window.title("Quiz APP GUI")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text='Score:0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='',
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Here right_image will not be the attribute of the object
        right_image = PhotoImage(file='./images/true.png')

        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)
        wrong_image = PhotoImage(file='./images/false.png')
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_object.still_has_questions():
            self.score.config(text=f"Score:{self.quiz_object.score}")
            q_text = self.quiz_object.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Thanks for playing the GAME.")
            # disabling the buttons once game  is finished
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz_object.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz_object.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

