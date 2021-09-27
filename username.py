from tkinter import *
import sqlite3
import global_imports


def main():
    root = Tk()
    root.geometry("760x820")

    root.config(bg='black')
    font = ('8-BIT WONDER.TTF', 15)
    Username = StringVar()
    Username.set('Username')

    def cleare(event):
        if Username.get() == 'Username':
            Username.set('')

    def gg():
        global_imports.running = True
        global_imports.User=Username.get()
        database()
        conn = sqlite3.connect('Scores.db')
        c = conn.cursor()

        c.execute("""SELECT *, oid FROM Highscore""")
        all = c.fetchall()
        for i in all:
            global_imports.Userid=i [-1]
            #print(i[-1])

        conn.commit()
        #print(all[-1])



        root.quit()


    def database():
        conn = sqlite3.connect('Scores.db')
        c = conn.cursor()
        try:
            c.execute("""CREATE TABLE Highscore (Username text,
            Highscore text)""")
            c.execute("INSERT INTO Highscore VALUES (:Uname, :Hscore)",
                      {
                          'Uname': Username.get(),
                          'Hscore': global_imports.Highscore
                      })
            conn.commit()

        except:
            c.execute("INSERT INTO Highscore VALUES (:Uname, :Hscore)",
                      {
                          'Uname': Username.get(),
                          'Hscore': global_imports.Highscore
                      })
            conn.commit()

    e = Entry(root, font=font, text=Username)
    e.place(x=300, y=410)
    e.bind('<Button-1>', cleare)
    Button(root, text='Submit', font=font, command=gg).place(x=320, y=500)

    mainloop()
