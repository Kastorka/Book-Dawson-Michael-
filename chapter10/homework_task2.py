from tkinter import *
import random


class Application(Frame):
    """ GUI application that creates a story based on user input. """

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get story information and to display story. """
        # Метка с инструкцией
        self.info_lbl = Label(self, text="Компьютер загадывает число от 1 до 10.")
        self.info_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        """ Метка для информации о вводе числа """
        # Метка с инструкцией
        self.inst_lbl = Label(self, text="Введите число")
        self.inst_lbl.grid(row=2, column=0, sticky=W)

        # Создать поле для ввода пароля
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=2, column=1, sticky=W)

        """ Создаем кнопку для подтверждения ввода """
        self.submit_bttn = Button(self, text="Угадать", command=self.make_a_guess)
        self.submit_bttn.grid(row=5, column=1, columnspan=1, sticky=W)

        """Поле с результатом"""
        self.secret_txt = Text(self, width=40, height=3, wrap=WORD)
        self.secret_txt.grid(row=4, column=0, columnspan=2, sticky=W)


    def make_a_guess(self):
        """ Increase click count and display new total. """
        guess = int(str(self.guess_ent.get()))
        if guess > number:
            message = 'Число меньше'
        elif guess < number:
            message = 'Число больше'
        else:
            message = 'Вы угадали'

        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


# main
number = random.randint(1, 10)

root = Tk()
root.title("Угадай число")
root.geometry("350x150")

app = Application(root)

root.mainloop()
