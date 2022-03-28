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


def getDay(day):
    global year, month
    popup = Tk()
    try:
        with open(f'{year},{month},{day}.csv', 'r') as f:
            events = f.readlines()
        for event in events:
            print(f'{event}')
    except:
        print('no data found')

    a = Combobox(popup, width=8)
    a['values'] = ('event', 'task', 'reminder')
    a.grid(row=1, column=0)
    Entry(popup).grid(row=1, column=1)
    Entry(popup).grid(row=1, column=2)

    a = Combobox(popup, width=8)
    a['values'] = ('event', 'task', 'reminder')
    a.grid(row=2, column=0)
    Entry(popup).grid(row=2, column=1)
    Entry(popup).grid(row=2, column=2)

    a = Combobox(popup, width=8)
    a['values'] = ('event', 'task', 'reminder')
    a.grid(row=3, column=0)
    Entry(popup).grid(row=3, column=1)
    Entry(popup).grid(row=3, column=2)

    a = Combobox(popup, width=8)
    a['values'] = ('event', 'task', 'reminder')
    a.grid(row=4, column=0)
    Entry(popup).grid(row=4, column=1)
    Entry(popup).grid(row=4, column=2)

    a = Combobox(popup, width=8)
    a['values'] = ('event', 'task', 'reminder')
    a.grid(row=5, column=0)
    Entry(popup).grid(row=5, column=1)
    Entry(popup).grid(row=5, column=2)

    a = Combobox(popup, width=8)
    a['values'] = ('event', 'task', 'reminder')
    a.grid(row=6, column=0)
    Entry(popup).grid(row=6, column=1)
    Entry(popup).grid(row=6, column=2)

    a = Combobox(popup, width=8)
    a['values'] = ('event', 'task', 'reminder')
    a.grid(row=7, column=0)
    Entry(popup).grid(row=7, column=1)
    Entry(popup).grid(row=7, column=2)

    a = Combobox(popup, width=8)
    a['values'] = ('event', 'task', 'reminder')
    a.grid(row=8, column=0)
    Entry(popup).grid(row=8, column=1)
    Entry(popup).grid(row=8, column=2)

    a = Combobox(popup, width=8)
    a['values'] = ('event', 'task', 'reminder')
    a.grid(row=9, column=0)
    Entry(popup).grid(row=9, column=1)
    Entry(popup).grid(row=9, column=2)

    popup.wm_title(f'{day} of {getMonthName(month)}, {year}')
    Label(popup, text=day, ).grid(row=0, column=0, columnspan=3)
    Button(popup, text="save", command=popup.destroy).grid(row=10, column=0, columnspan=3)
    popup.mainloop()


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
    Month = getMonthName(month)
    labelDate.set(f'{Month} {str(year)}')
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
    Month = getMonthName(month)
    labelDate.set(f'{Month} {str(year)}')
    DaysOfTheMonth()
    return year, month


def getMonthName(Input):
    global output
    if Input == 1:
        output = 'January'
    elif Input == 2:
        output = 'February'
    elif Input == 3:
        output = 'March'
    elif Input == 4:
        output = 'April'
    elif Input == 5:
        output = 'may'
    elif Input == 6:
        output = 'June'
    elif Input == 7:
        output = 'July'
    elif Input == 8:
        output = 'August'
    elif Input == 9:
        output = 'september'
    elif Input == 10:
        output = 'October'
    elif Input == 11:
        output = 'November'
    elif Input == 12:
        output = 'December'
    else:
        logging.error('bad data (getMonthName) L42')
    return output


def DaysOfTheMonth():
    global month, year
    row = 2
    column = (-1 + int(date(year, month, 1).isoweekday()))
    List = root.grid_slaves()
    labelDate.set(f'{getMonthName(month)} {str(year)}')
    Button(root, text='last month', command=lastMonth).grid(row=0, column=2)
    Label(root, textvariable=labelDate).grid(row=0, column=3)
    Button(root, text='next month', command=nextMonth).grid(row=0, column=4)

    Label(root, text='Sunday').grid(row=1, column=0)
    Label(root, text='Monday').grid(row=1, column=1)
    Label(root, text='Tuesday').grid(row=1, column=2)
    Label(root, text='Wednesday').grid(row=1, column=3)
    Label(root, text='Tuesday').grid(row=1, column=4)
    Label(root, text='Friday').grid(row=1, column=5)
    Label(root, text='Saturday').grid(row=1, column=6)

    if int(date(year, month, 1).isoweekday()) == 1:
        Button(text='', width=15).grid(row=2, column=0, ipady=15)

    elif int(date(year, month, 1).isoweekday()) == 2:
        Button(text='', width=15).grid(row=2, column=0, ipady=15)
        Button(text='', width=15).grid(row=2, column=1, ipady=15)

    elif int(date(year, month, 1).isoweekday()) == 3:
        Button(text='', width=15).grid(row=2, column=0, ipady=15)
        Button(text='', width=15).grid(row=2, column=1, ipady=15)
        Button(text='', width=15).grid(row=2, column=2, ipady=15)

    elif int(date(year, month, 1).isoweekday()) == 4:
        Button(text='', width=15).grid(row=2, column=0, ipady=15)
        Button(text='', width=15).grid(row=2, column=1, ipady=15)
        Button(text='', width=15).grid(row=2, column=2, ipady=15)
        Button(text='', width=15).grid(row=2, column=3, ipady=15)

    elif int(date(year, month, 1).isoweekday()) == 5:
        Button(text='', width=15).grid(row=2, column=0, ipady=15)
        Button(text='', width=15).grid(row=2, column=1, ipady=15)
        Button(text='', width=15).grid(row=2, column=2, ipady=15)
        Button(text='', width=15).grid(row=2, column=3, ipady=15)
        Button(text='', width=15).grid(row=2, column=4, ipady=15)

    elif int(date(year, month, 1).isoweekday()) == 6:
        Button(text='', width=15).grid(row=2, column=0, ipady=15)
        Button(text='', width=15).grid(row=2, column=1, ipady=15)
        Button(text='', width=15).grid(row=2, column=2, ipady=15)
        Button(text='', width=15).grid(row=2, column=3, ipady=15)
        Button(text='', width=15).grid(row=2, column=4, ipady=15)
        Button(text='', width=15).grid(row=2, column=5, ipady=15)

    for i in List:
        i.destroy()

    command = ['']

    for i in range(1, monthrange(year, month)[1] + 1):
        if (i + date(year, month, 1).isoweekday()) % 7 == 1:
            row = row + 1
            column = 0
        else:
            column = column + 1

        command.append(i)
        if i == 1:
            Button(text=i, command=lambda: getDay(command[1]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 2:
            Button(text=i, command=lambda: getDay(command[2]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 3:
            Button(text=i, command=lambda: getDay(command[3]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 4:
            Button(text=i, command=lambda: getDay(command[4]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 5:
            Button(text=i, command=lambda: getDay(command[5]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 6:
            Button(text=i, command=lambda: getDay(command[6]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 7:
            Button(text=i, command=lambda: getDay(command[7]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 8:
            Button(text=i, command=lambda: getDay(command[8]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 9:
            Button(text=i, command=lambda: getDay(command[9]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 10:
            Button(text=i, command=lambda: getDay(command[10]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 11:
            Button(text=i, command=lambda: getDay(command[11]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 12:
            Button(text=i, command=lambda: getDay(command[12]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 13:
            Button(text=i, command=lambda: getDay(command[13]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 14:
            Button(text=i, command=lambda: getDay(command[14]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 15:
            Button(text=i, command=lambda: getDay(command[15]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 16:
            Button(text=i, command=lambda: getDay(command[16]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 17:
            Button(text=i, command=lambda: getDay(command[17]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 18:
            Button(text=i, command=lambda: getDay(command[18]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 19:
            Button(text=i, command=lambda: getDay(command[19]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 20:
            Button(text=i, command=lambda: getDay(command[20]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 21:
            Button(text=i, command=lambda: getDay(command[21]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 22:
            Button(text=i, command=lambda: getDay(command[22]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 23:
            Button(text=i, command=lambda: getDay(command[23]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 24:
            Button(text=i, command=lambda: getDay(command[24]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 25:
            Button(text=i, command=lambda: getDay(command[25]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 26:
            Button(text=i, command=lambda: getDay(command[26]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 27:
            Button(text=i, command=lambda: getDay(command[27]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 28:
            Button(text=i, command=lambda: getDay(command[28]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 29:
            Button(text=i, command=lambda: getDay(command[29]), width=15).grid(row=row, column=column, ipady=15)

        elif i == 30:
            Button(text=i, command=lambda: getDay(command[30]), width=15).grid(row=row, column=column, ipady=15)

        else:
            Button(text=i, command=lambda: getDay(command[31]), width=15).grid(row=row, column=column, ipady=15)

    if int(date(year, month, monthrange(year, month)[1]).isoweekday()) == 5:
        Button(text='', width=15).grid(row=row, column=6, ipady=15)

    elif int(date(year, month, monthrange(year, month)[1]).isoweekday()) == 4:
        Button(text='', width=15).grid(row=row, column=6, ipady=15)
        Button(text='', width=15).grid(row=row, column=5, ipady=15)

    elif int(date(year, month, monthrange(year, month)[1]).isoweekday()) == 3:
        Button(text='', width=15).grid(row=row, column=6, ipady=15)
        Button(text='', width=15).grid(row=row, column=5, ipady=15)
        Button(text='', width=15).grid(row=row, column=4, ipady=15)

    elif int(date(year, month, monthrange(year, month)[1]).isoweekday()) == 2:
        Button(text='', width=15).grid(row=row, column=6, ipady=15)
        Button(text='', width=15).grid(row=row, column=5, ipady=15)
        Button(text='', width=15).grid(row=row, column=4, ipady=15)
        Button(text='', width=15).grid(row=row, column=3, ipady=15)

    elif int(date(year, month, monthrange(year, month)[1]).isoweekday()) == 1:
        Button(text='', width=15).grid(row=row, column=6, ipady=15)
        Button(text='', width=15).grid(row=row, column=5, ipady=15)
        Button(text='', width=15).grid(row=row, column=4, ipady=15)
        Button(text='', width=15).grid(row=row, column=3, ipady=15)
        Button(text='', width=15).grid(row=row, column=2, ipady=15)

    elif int(date(year, month, monthrange(year, month)[1]).isoweekday()) == 7:
        Button(text='', width=15).grid(row=row, column=6, ipady=15)
        Button(text='', width=15).grid(row=row, column=5, ipady=15)
        Button(text='', width=15).grid(row=row, column=4, ipady=15)
        Button(text='', width=15).grid(row=row, column=3, ipady=15)
        Button(text='', width=15).grid(row=row, column=2, ipady=15)
        Button(text='', width=15).grid(row=row, column=1, ipady=15)


def main():
    DaysOfTheMonth()

    root.title('Calender')
    root.geometry()
    root.mainloop()


if __name__ == '__main__':
    main()
