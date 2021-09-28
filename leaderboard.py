from tkinter import *
import sqlite3

def main():


    def Table():

        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                e.grid(row=i, column=j)
                e.insert(END, all[i][j])
    def sort(nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
    highest_score = []
    sorted_highscore = []


    conn = sqlite3.connect('Scores.db')
    c = conn.cursor()

    c.execute("""SELECT *, oid FROM Highscore""")
    all = c.fetchall()
    for i in all:
        highest_score.append(i[1])
        Hs = max(highest_score)
    sort(highest_score)
    for i in range(len(highest_score)):
        asd = max(highest_score)
        sorted_highscore.append(asd)


    conn.commit()



    # find total number of rows and
    # columns in list
    total_rows = len(all)
    if total_rows>11:
        total_rows=11
    total_columns = len(all[0])
    if total_columns>2:
        total_columns=2
    # create root window
    root = Tk()
    Table()
    root.mainloop()

