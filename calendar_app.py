# Enter the year and calendar for that year is shown

from tkinter import *
import calendar
from functools import partial


# Function to show the calendar
def show_calendar():
    cal = Tk()
    cal.config(background='white')
    cal.geometry("550x600")
    year = int(year_field.get())
    cal.title(str(year) + " Calendar")
    cal_content = calendar.calendar(year)
    cal_year = Label(cal, text=cal_content, font="Consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20)
    cal.mainloop()


if __name__ == "__main__":
    menu = Tk()
    menu.config(background='white')
    menu.title("Calendar")
    menu.geometry("250x140")
    cal_title = Label(menu, text="Calendar", bg='white', font=("times", 28, "bold"))
    input_year = Label(menu, text="Enter year", bg='white')
    year_field = Entry(menu)
    button = Button(menu, text='Show Calendar', fg='Black', bg='White', command=show_calendar)

    cal_title.grid(row=1, column=1)
    input_year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    menu.mainloop()
