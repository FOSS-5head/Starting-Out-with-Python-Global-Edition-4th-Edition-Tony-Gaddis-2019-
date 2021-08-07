# В центре внимания.
import tkinter


class TestAvg:

    def __init__(self):
        # Main function
        self.main_window = tkinter.Tk()

        # All frame
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # label 1
        self.test1_label = tkinter.Label(self.test1_frame,
                                         text='Введите оценку 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame,
                                         width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # label 2
        self.test2_label = tkinter.Label(self.test2_frame,
                                         text='Введите оценку 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame,
                                         width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        # label 3
        self.test3_label = tkinter.Label(self.test3_frame,
                                         text='Введите оценку 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame,
                                         width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        # result label
        self.result_label = tkinter.Label(self.avg_frame,
                                          text='Средний балл:')
        self.avg = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.avg_frame,
                                       textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        # calculation button
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Усреднить',
                                          command=self.calc_avg)
        # quit_button
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Выйти',
                                          command=self.main_window.destroy)

        # pack buttons
        self.calc_button.pack()
        self.quit_button.pack()

        # pack frames
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # start main loop.
        tkinter.mainloop()

    # Метод для подсчета.
    def calc_avg(self):
            self.test1 = float(self.test1_entry.get())
            self.test2 = float(self.test2_entry.get())
            self.test3 = float(self.test3_entry.get())

            self.average = (self.test1 + self.test2 + self.test3) / 3.0

            self.avg.set(self.average)


test_avg = TestAvg()
