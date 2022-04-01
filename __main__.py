from calendar import monthrange
from tkinter import BOTH, HORIZONTAL, StringVar, Tk
from datetime import date
from tkinter.ttk import Combobox, Style, Entry, Button, Label, Frame, Separator

root = Tk()
style = Style()
root.tk.call("source", "proxttk-dark.tcl")
style.theme_use("proxttk-dark")
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



def AddEntry(Day):
    global year, month

    for i in root.grid_slaves():
        i.destroy()
    
    Label(text=f'{MonthNameDict[month]} {Day}').grid(row=0, column=1, columnspan=2)

    Label(text='title', width=15).grid(row=1, column=0)


    Button(text='save', width=30).grid(row=4, column=1, padx=5, pady=5)
    Button(text='back', command=lambda:GetDay(Day), width=30).grid(row=4, column=2, padx=5, pady=5)


def GetDay(Day):
    global year, month
    try:
        with open(f'{year},{month},{Day}.csv', 'r') as f:
            events = f.readlines()
        for event in events:
            print(f'{event}')
    except:
        print('no data found')

    for i in root.grid_slaves():
        i.destroy()

    Label(text= f'{MonthNameDict[month]} {Day}', anchor='center', width=15).grid(row=0, column=0)
    Label(text= '', anchor='center', width=105).grid(row=0, column=1, columnspan=3)
    
    a=1

    for i in range(1,25):
        Label(text= i, anchor='center', width=15).grid(row=a, column=0)
        a += 1
        Separator(orient=HORIZONTAL).grid(row=a, column=0, columnspan=4, sticky='ew')
        a += 1

    Button(text="close", command=DaysOfTheMonth).grid(row=50, column=0, columnspan=2)
    Button(text='Data Entry', command=lambda: AddEntry(Day)).grid(row=50, column=2, columnspan=2)


def lastMonth():
    global year, month
    if month == 1:
        month = 12
        year -= 1
    else:
        month -= 1
    DaysOfTheMonth()
    return year, month


def nextMonth():
    global year, month
    if month == 12:
        month = 1
        year += 1
    else:
        month +=1
    DaysOfTheMonth()
    return year, month

def DaysOfTheMonth():
    global month, year
    column = (-1 + int(date(year, month, 1).isoweekday()))
    for i in root.grid_slaves():
        i.destroy()
    labelDate.set(f'{MonthNameDict[month]} {str(year)}')
    Button(root, text='last month', command=lastMonth).grid(row=0, column=2, padx=5, pady=5)
    Label(root, textvariable=labelDate).grid(row=0, column=3)
    Button(root, text='next month', command=nextMonth).grid(row=0, column=4, padx=5, pady=5)

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
                Button(text='', width=15).grid(row=2, column=i, ipady=20, padx=5, pady=5)

    row = 2
    for i in range(1, monthrange(year, month)[1] + 1):
        if (i + date(year, month, 1).isoweekday()) % 7 == 1:
            row += 1
            column = 0
        else:
            column += 1

        Button(text=i, command=lambda day=i: GetDay(day), width=15).grid(row=row, column=column, ipady=20, padx=5, pady=5)

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
                Button(text='', width=15).grid(row=row, column=i, ipady=20, padx=5, pady=5)


def main():
    DaysOfTheMonth()

    root.title('Calender')
    root.geometry('870x600')
    root.mainloop()


if __name__ == '__main__':
    main()
