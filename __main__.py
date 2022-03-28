import logging
from calendar import monthrange
from tkinter import StringVar, Tk
from datetime import date
from tkinter.ttk import Combobox, Style, Entry, Button, Label, Frame

root = Tk()
style = Style()
style.theme_use('default')
Frame(root).grid(row=0, column=0, rowspan=7, columnspan=7)
currentDay = str(date.today().day)
currentMonth = int(date.today().month)
currentYear = int(date.today().year)
month = currentMonth
year = currentYear
labelDate = StringVar()

MonthNameDict = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'may',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'september',
    10 : 'October',
    11 : 'November',
    12 : 'December'}


def getDay(day):
    global year, month
    try:
        with open(f'{year},{month},{day}.csv', 'r') as f:
            events = f.readlines()
        for event in events:
            print(f'{event}')
    except:
        print('no data found')

    for i in root.grid_slaves():
        i.destroy()

    for i in range(1,10):
        a = Combobox(width=8)
        a['values'] = ('event', 'task', 'reminder')
        a.grid(row=i, column=0)
        Entry().grid(row=i, column=1)
        Entry().grid(row=i, column=2)

    
    Label(text= f'{MonthNameDict[month]} {day}' ).grid(row=0, column=0, columnspan=3)
    Button(text="save", command=DaysOfTheMonth).grid(row=10, column=0, columnspan=3)


def lastMonth():
    global year, month
    if month in {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}:
        month = month - 1
    elif month == 1:
        month = 12
        year = year - 1
    else:
        logging.error('bad data (lastMonth) L13')
        return
    labelDate.set(f'{MonthNameDict[month]} {str(year)}')
    DaysOfTheMonth()
    return year, month


def nextMonth():
    global year, month
    if month in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}:
        month = month + 1
    elif month == 12:
        month = 1
        year = year + 1
    else:
        logging.error('bad data (nextMonth) L26')
        return
    labelDate.set(f'{MonthNameDict[month]} {str(year)}')
    DaysOfTheMonth()
    return year, month

def DaysOfTheMonth():
    global month, year
    column = (-1 + int(date(year, month, 1).isoweekday()))
    for i in root.grid_slaves():
        i.destroy()
    labelDate.set(f'{MonthNameDict[month]} {str(year)}')
    Button(root, text='last month', command=lastMonth).grid(row=0, column=2)
    Label(root, textvariable=labelDate).grid(row=0, column=3)
    Button(root, text='next month', command=nextMonth).grid(row=0, column=4)

    DaysDict = {
        0 : 'Sunday',
        1 : 'Monday',
        2 : 'Tuesday',
        3 : 'Wednesday',
        4 : 'Thursday',
        5 : 'Friday',
        6 : 'Saturday'
    }

    for i in range(0,7):
        Label(root, text=DaysDict[i]).grid(row=1, column=i)

    for j in range(1,7):
        if int(date(year, month, 1).isoweekday()) == j:
            for i in range(0,j):
                Button(text='', width=15).grid(row=2, column=i, ipady=15)

    row = 2
    for i in range(1, monthrange(year, month)[1] + 1):
        if (i + date(year, month, 1).isoweekday()) % 7 == 1:
            row += 1
            column = 0
        else:
            column += 1

        Button(text=i, command=lambda day=i: getDay(day), width=15).grid(row=row, column=column, ipady=15)

    EndBlanksDict = {
        7 : (1,2,3,4,5,6),
        6 : ( ),
        5 : (6, ),
        4 : (5,6),
        3 : (4,5,6),
        2 : (3,4,5,6),
        1 : (2,3,4,5,6)
        }


    for j in range(1,8):
        if int(date(year, month, monthrange(year, month)[1]).isoweekday()) == j:
            for i in EndBlanksDict[j]:
                Button(text='', width=15).grid(row=row, column=i, ipady=15)


def main():
    DaysOfTheMonth()

    root.title('Calender')
    root.geometry('700x400')
    root.mainloop()


if __name__ == '__main__':
    main()
