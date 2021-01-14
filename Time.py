try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import tkinter.font as TkFont
from tkcalendar import Calendar, DateEntry
from tkinter.messagebox import showerror
# class quitButton(Button):
#     def __init__(self, parent):
#         Button.__init__(self, parent)
#         self['text'] = 'Good Bye'
#         # Command to close the window (the destory method)
#         self['command'] = parent.destroy
#         self.pack(side=BOTTOM)


class Time:
    def __init__(self, app):
        self.master = app
        self.date_since = "2019-12-27"
        self.date_untill = "2020-01-27"
        self.var_since = StringVar()
        self.var_since.set(self.date_since)
        self.var_untill = StringVar()
        self.var_untill.set(self.date_untill)
        self.hour_since = "12"
        self.var_hour_since = StringVar()
        self.var_hour_since.set(self.hour_since)
        self.hour_untill = "12"
        self.var_hour_untill = StringVar()
        self.var_hour_untill.set(self.hour_untill)
        self.font_butt = TkFont.Font(
            family='Helvetica', size=10, weight=TkFont.BOLD)

    def set_since(self):
        self.date_since = self.cal_since.selection_get()
        self.var_since.set(self.date_since)
        # print("data since", self.date_since)

# working hirr

    def set_untill(self):
        self.date_untill = self.cal_untill.selection_get()
        self.var_untill.set(self.date_untill)
        # self.cal_untill.quit()

    def ft_calendar_since(self):
        top = Toplevel(self.master)
        self.cal_since = Calendar(
            top, font="Arial 14", selectmode="day", year=2020, month=11, day=22)
        self.cal_since.pack()
        self.butt_cal = Button(
            self.cal_since, text="ok", command=self.set_since, bg='red', height=1, width=14)
        self.butt_cal.pack()
        # quitButton(self.cal_since)#######test

    def ft_decrement_hour_since(self):
        hour = int(self.hour_since)
        if hour > 0:
            hour -= 1
            self.hour_since = str(hour)
        if len(self.hour_since) == 1:
            self.hour_since = "0" + self.hour_since
        self.var_hour_since.set(self.hour_since)

    def ft_increment_hour_since(self):
        hour = int(self.hour_since)
        if hour < 23:
            hour += 1
            self.hour_since = str(hour)
        if len(self.hour_since) == 1:
            self.hour_since = "0" + self.hour_since
        self.var_hour_since.set(self.hour_since)

    def ft_decrement_hour_untill(self):
        hour = int(self.hour_untill)
        if hour > 0:
            hour -= 1
            self.hour_untill = str(hour)
        if len(self.hour_untill) == 1:
            self.hour_untill = "0" + self.hour_untill
        self.var_hour_untill.set(self.hour_untill)

    def ft_increment_hour_untill(self):
        hour = int(self.hour_untill)
        if hour < 23:
            hour += 1
            self.hour_untill = str(hour)
        if len(self.hour_untill) == 1:
            self.hour_untill = "0" + self.hour_untill
        self.var_hour_untill.set(self.hour_untill)
    # def close_window(self, root)
    #     root.destroy()

    def ft_calendar_untill(self):
        top = Toplevel(self.master)
        self.cal_untill = Calendar(
            top, font="Arial 14", selectmode="day", year=2020, month=11, day=22)
        self.cal_untill.pack()
        self.butt_cal = Button(self.cal_untill, text="ok", font=self.font_butt,
                               bg='red', command=self.set_untill, height=1, width=14)
        # self.butt_cal.size(height=10, width=100)
        self.butt_cal.pack()

    def clear_all(self):
        pass

    def get_all(self):  # "2019-07-01 00:00:00"
        valuer_date_since = str(self.date_since) + " " + \
            self.hour_since + ":00:00"
        valuer_date_untill = str(self.date_untill) + \
            " " + self.hour_untill + ":00:00"
        print("data until",  valuer_date_untill)
        print("data since",  valuer_date_since)
        return [valuer_date_since, valuer_date_untill]

    def main(self):
        self.fram = LabelFrame(self.master, text=" Enter Details On Date :",  fg="red",
                               font=("Courier", 26, "italic"))
        self.fram.grid(row=0, columnspan=8, sticky='W',
                       padx=0, pady=0, ipadx=0, ipady=4)
        self.fram.configure(background="#091833")

        self.butt = Button(self.fram, text="date since", font=self.font_butt,
                           command=self.ft_calendar_since, bg="red")
        self.butt.grid(row=0, column=2,  padx=5, pady=1, ipadx=5, ipady=5)
        # self.butt.configure(background="#091833")
        Label(self.fram, textvariable=self.var_since, bg="#f2a343", font=(
            "Courier", 15, "italic")).grid(row=0, column=4,  padx=5, pady=1, ipadx=5, ipady=5)

        self.butt_inc = Button(self.fram, text="increment hour     ",
                               font=self.font_butt, command=self.ft_increment_hour_since, bg="red")
        self.butt_inc.grid(row=0, column=5,  padx=5, pady=1, ipadx=5, ipady=5)

        self.butt_dec = Button(self.fram, text="decrement hour     ",
                               font=self.font_butt, command=self.ft_decrement_hour_since, bg="red")
        self.butt_dec.grid(row=0, column=6,  padx=5, pady=1, ipadx=5, ipady=5)
        Label(self.fram, textvariable=self.var_hour_since, bg="#f2a343", font=(
            "Courier", 15, "italic")).grid(row=0, column=8,  padx=5, pady=1, ipadx=5, ipady=5)
        Label(self.fram, text="hour_since", bg="#091833", fg="snow", font=(
            "Courier", 15, "italic")).grid(row=0, column=10,  padx=5, pady=1, ipadx=5, ipady=5)

        self.butt = Button(self.fram, text="date until ",
                           font=self.font_butt, command=self.ft_calendar_untill, bg="red")
        self.butt.grid(row=1, column=2, padx=5, pady=1, ipadx=5, ipady=5)

        Label(self.fram, textvariable=self.var_untill, bg="#f2a343", font=(
            "Courier", 15, "italic")).grid(row=1, column=4,  padx=5, pady=1, ipadx=5, ipady=5)

        self.butt_inc_mn = Button(self.fram, text="increment hour     ",
                                  font=self.font_butt, command=self.ft_increment_hour_untill, bg="red")
        self.butt_inc_mn.grid(row=1, column=5,  padx=5,
                              pady=1, ipadx=5, ipady=5)
        self.butt_dec_mn = Button(self.fram, text="decrement hour     ",
                                  font=self.font_butt, command=self.ft_decrement_hour_untill, bg="red")
        self.butt_dec_mn.grid(row=1, column=6,  padx=5,
                              pady=1, ipadx=5, ipady=5)

        Label(self.fram, textvariable=self.var_hour_untill, bg="#f2a343", font=(
            "Courier", 15, "italic")).grid(row=1, column=8,  padx=5, pady=1, ipadx=5, ipady=5)
        Label(self.fram, text="hour_until", bg="#091833",  fg="snow", font=(
            "Courier", 15, "italic")).grid(row=1, column=10,  padx=5, pady=1, ipadx=5, ipady=5)
