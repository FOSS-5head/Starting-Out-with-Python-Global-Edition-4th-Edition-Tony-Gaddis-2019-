import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Две рамки: одна для элементов Radiobutton,
        # вторая для обычных элементов Button.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать объект IntVar для использования с элементами Radiobutton.
        self.radio_var = tkinter.IntVar()

        # Назначить объекту IntVar значение 1.
        self.radio_var.set(1)

        # Radiobutton 1
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Вариант 1',
                                       variable=self.radio_var,
                                       value=1)
        # Radiobutton 2
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Вариант 2',
                                       variable=self.radio_var,
                                       value=2)
        # Radiobutton 3
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Вариант 3',
                                       variable=self.radio_var,
                                       value=3)

        # УПАКОВАТЬ ЭЛЕМЕНТЫ Radiobutton.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Создать кнопку 'ОК' и кнопку 'Выйти'.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                          command=self.main_window.destroy)

        self.ok_button.pack()
        self.quit_button.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo('Выбор', f'Выбран вариант {str(self.radio_var.get())}')


my_gui = MyGUI()
