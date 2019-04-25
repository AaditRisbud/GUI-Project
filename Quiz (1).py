from tkinter import Tk, Frame, Label, Button, Scale, HORIZONTAL, BOTTOM,DoubleVar, Radiobutton,\
    StringVar
from time import sleep

class Question:
    def __init__(self, screentype, question, answers, correctLetter):
        self.screentype = screentype
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Right!", fg="green")
            right += 1
        else:
            label = Label(view, text="Wrong!", fg="red")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))

    def updateButtonText(self,letter):
        self.btn.config(text="Your Answer = "+str(letter))


    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        if(self.screentype == "Scale"):
            var = DoubleVar()
            slider = Scale(view, from_=0, to=100, orient=HORIZONTAL, variable = var, command=self.updateButtonText)
            slider.pack()
            self.btn = Button(master=view, text="Your Answer = "+ str(slider.get()), command=lambda *args: self.check(str(slider.get()), view))
            self.btn.pack()
        elif(self.screentype == "Radio"):
            var = StringVar()

            Radiobutton(view,text=self.answers[0], value="A", variable=var, command=lambda *args: self.check(var.get(), view)).pack()
            Radiobutton(view,text=self.answers[1], value="B", variable=var, command=lambda *args: self.check(var.get(), view)).pack()
            Radiobutton(view,text=self.answers[2], value="C", variable=var, command=lambda *args: self.check(var.get(), view)).pack()
            Radiobutton(view,text=self.answers[3], value="D", variable=var, command=lambda *args: self.check(var.get(), view)).pack()
            var.set(None)

        else:
            Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
            Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
            Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
            Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

questions = []
file = open("Questions.txt", "r")
line = file.readline()
while(line != ""):
    screentype = line.rstrip()
    questionString = file.readline()
    answers = []
    if(screentype != "Scale"):
        for i in range (4):
            answers.append(file.readline())
    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(screentype, questionString, answers, correctLetter))
    line = file.readline()

file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()
window.title("Marvel Quiz")
window.geometry("400x400")
button = Button(master=window, text="Start", command=askQuestion)
button.pack(side=BOTTOM)
window.mainloop()
