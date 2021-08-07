# Эта программа конвертирует расстояния в километрах 1
# в мили. Полученный результат выводится
# в элемент Label в главном окне. 1
import tkinter
import tkinter.messagebox


class KiloConverterGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Введите расстояние в километрах:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Преобразовать в мили:')

        self.value = tkinter.StringVar()

        self.miles_lavel = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)

        self.descr_label.pack(side='left')
        self.miles_lavel.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Преобразовать',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                          command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214

        self.value.set(miles)


kilo_conv = KiloConverterGUI()
