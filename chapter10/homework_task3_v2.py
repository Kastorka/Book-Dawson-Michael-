# Restaurant menu
# Simple GUI application


from tkinter import *

class Menu(Frame):
    def __init__(self, master):
        super(Menu, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "SUSHI MENU"
              ).grid(row = 0, column = 1, sticky = W)

        self.nigiri = BooleanVar()
        Label(self,
              text = "Nigiri"
              ).grid(row = 2, column = 0, sticky = W)
        Label(self,
              text = "2.45 $"
              ).grid(row = 2, column = 1, sticky = W)

        Checkbutton(self,
                    variable = self.nigiri
                    ).grid(row = 2, column = 2, sticky = W)
        Label(self,
              text = "Amount:"
              ).grid(row = 2, column = 3, sticky = W)

        self.nigiri_amount = Entry(self)
        self.nigiri_amount.grid(row = 2, column = 4, sticky = W)

        self.maki = BooleanVar()
        Label(self,
              text = "Maki"
              ).grid(row = 3, column = 0, sticky = W)
        Label(self,
              text = "4.89 $"
              ).grid(row = 3, column = 1, sticky = W)
        Checkbutton(self,
                    variable = self.maki
                    ).grid(row = 3, column = 2, sticky = W)
        Label(self,
              text = "Amount:"
              ).grid(row = 3, column = 3, sticky = W)
        self.maki_amount = Entry(self)
        self.maki_amount.grid(row = 3, column = 4, sticky = W)

        self.futomaki = BooleanVar()
        Label(self,
              text = "Futomaki"
              ).grid(row = 4, column = 0, sticky = W)
        Label(self,
              text = "12.99 $"
              ).grid(row = 4, column = 1, sticky = W)
        Checkbutton(self,
                    variable = self.futomaki
                    ).grid(row = 4, column = 2, sticky = W)
        Label(self,
              text = "Amount:"
              ).grid(row = 4, column = 3, sticky = W)
        self.futomaki_amount = Entry(self)
        self.futomaki_amount.grid(row = 4, column = 4, sticky = W)

        Button(self,
               text = "Order!",
               command = self.order,
               ).grid(row = 5, column = 0, sticky = W)

        self.yours = Text(self, width = 50, height = 10, wrap = WORD)
        self.yours.grid(row = 6, column = 0, columnspan = 5)

    def order(self):
        price = 0
        order = ""
        maki = self.maki_amount.get()
        nigiri = self.nigiri_amount.get()
        futomaki = self.futomaki_amount.get()
        if self.nigiri.get():
            price += 2.45 * int(nigiri)
            order += "nigiri, "
        if self.maki.get():
            price += 4.89 * int(maki)
            order += "maki, "
        if self.futomaki.get():
            price += 12.99 * int(futomaki)
            order += "futomaki."

        yours = "You have ordered: "
        yours += order
        yours += "\nTotal cost: "
        yours += str(price)

        self.yours.delete(0.0, END)
        self.yours.insert(0.0, yours)

root = Tk()
root.title("Menu")
app = Menu(root)
root.mainloop()