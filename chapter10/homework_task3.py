# Movie Chooser
# Demonstrates check buttons

from tkinter import *

class Application(Frame):
    """ GUI Application for favorite movie types. """
    def __init__(self, master):
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets for movie type choices. """    
        # create description label
        Label(self,
              text = "Собири свой БигТейсти"
              ).grid(row = 0, column = 0, sticky = W)

        # Метра конструктора
        # Label(self,
        #       text = "Выбери столько индигриентов сколько пожелаешь"
        #       ).grid(row = 0, column = 0, sticky = W)

        # Кнопка для выбора Котлеты
        self.cutlet = BooleanVar()
        Checkbutton(self,
                    text = "Котлета - 100р",
                    variable = self.cutlet,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        # Кнопка для выбора Бекона
        self.becon = BooleanVar()
        Checkbutton(self,
                    text = "Бекон - 20р",
                    variable = self.becon,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        # Кнопка для выбора огурца
        self.pickle = BooleanVar()
        Checkbutton(self,
                    text = "Соленый огурец - 15р",
                    variable = self.pickle,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)

        # Кнопка для выбора соуса
        self.sauce = BooleanVar()
        Checkbutton(self,
                    text="Соус - 5р",
                    variable=self.sauce,
                    command=self.update_text
                    ).grid(row=2, column=2, columnspan = 2 ,sticky=W)

        # create text field to display results
        self.results_txt = Text(self, width = 40, height = 4, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """ Update text widget and display user's favorite movie types. """
        total = 0
        
        if self.cutlet.get():
            total += 100

        if self.pickle.get():
            total += 15

        if self.becon.get():
            total += 20

        if self.sauce.get():
            total += 5
      
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, 'Общая сумма: ')
        self.results_txt.insert(10.10, total)
        self.results_txt.insert(10.0, 'р.')

# main
root = Tk()
root.title("Собери свой бургер")
root.geometry("365x210")
app = Application(root)
root.mainloop()
