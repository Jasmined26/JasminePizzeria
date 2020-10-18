import tkinter

class JasminePizzeria:

    def __init__(self):

        # create main window
        self.main_window = tkinter.Tk()

        # Design main window
        self.main_window.title("Jasmine's Pizzeria")
        self.main_window.config(bg = 'red')


        # run mainloop
        tkinter.mainloop()





my_gui = JasminePizzeria()