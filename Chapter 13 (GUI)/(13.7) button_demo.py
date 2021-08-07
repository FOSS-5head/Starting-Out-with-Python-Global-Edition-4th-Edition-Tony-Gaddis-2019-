# Эта программа демонстрирует элемент интерфейса Button.
# Когда пользователь нажимает кнопку Button,
# на экран выводится информационное диалоговое окно.

import tkinter
import tkinter.messagebox


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.my_button = tkinter.Button(self.main_window,
                                        text='Нажми меня!',
                                        command=self.do_something)

        self.my_button.pack()
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Реакция',
                                    'Благодарю, что нажали кнопку')


my_gui = MyGui()
