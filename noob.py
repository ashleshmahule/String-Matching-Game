from tkinter import *
from playsound import *
import random,string,winsound
from tkinter import messagebox

class gameUI:
    # ..............................VARIABLES...................................
    chars = string.ascii_letters
    size = 12
    NO_OF_CHARS = 256
    score = 0
    # ...............................ALGORITHM..................................
    def random_string_generator(self, str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for _ in range(str_size))

    def random_specific_string_generator_lvl_1(self, str_size, allowed_chars, i, pattern):
        s = ''.join(random.choice(allowed_chars) for _ in range(i))
        s += ''.join(pattern)
        s += ''.join(random.choice(allowed_chars) for _ in range(str_size - len(pattern) - i))
        return s

    def getNextState(self, pat, M, state, x):
        # If the character c is same as next character in pattern, then simply increment state
        if state < M and x == ord(pat[state]):
            return (state + 1)
        i = 0
        for self.ns in range(state, 0, -1):
            if ord(pat[self.ns - 1]) == x:
                while i < self.ns - 1:
                    if pat[i] != pat[state - self.ns + 1 + i]:
                        break
                    i += 1
                if i == self.ns - 1:
                    return self.ns
        return 0

    def computeTF(self, pat, M):
        '''This function builds the TF table which represents Finite Automata for a given pattern '''
        self.NO_OF_CHARS = 256

        TF = [[0 for _ in range(self.NO_OF_CHARS)] \
              for _ in range(M + 1)]
        for self.state in range(M + 1):
            for x in range(self.NO_OF_CHARS):
                z = self.getNextState(pat, M, self.state, x)
                TF[self.state][x] = z
        return TF

    def search(self, pat, txt):
        '''Prints all occurrences of pat in txt'''
        global NO_OF_CHARS
        M = len(pat)
        N = len(txt)
        TF = self.computeTF(pat, M)
        flag = 0
        # Process txt over FA.
        state = 0
        for i in range(N):
            state = TF[state][ord(txt[i])]
            if state == M:
                print("Pattern found at index: {}".format(i - M + 1))
                self.score += 10

                if self.score <= 30:
                    self.scoreUpdate_lvl1()
                if self.score <= 60 and self.score > 30:
                    self.scoreUpdate_lvl2()
                print(self.score)
                if self.score == 30:
                    self.lvl2()
                if self.score == 70:
                    self.champion()
                    #playsound('applause.mp3')
                flag = 1
        if flag == 0:
            print("NOT FOUND")
            print("Final Score is " + str(self.score))
            self.gameOver()
        return flag
    # ...............................LEVEL_1......................................
    def scoreUpdate_lvl1(self):
        self.scoreLabel.destroy()
        self.scoreLabel = Label(self.lvl1, text="Score: " + str(self.score), font=15)
        self.scoreLabel.config(bg='white')
        self.scoreLabel.config(font=("game over", 40))
        self.scoreLabel.place(x=0, y=0)

    def cmdbtn1_lvl1(self):
        print("Searching Pattern in selected String")
        playsound('groot2.mp3')
        self.search(self.pat1, self.txt1)
        try:
            self.button1.destroy()
        except Exception:
            print("Exception")

    def cmdbtn2_lvl1(self):
        print("Searching Pattern in selected String")
        playsound('groot2.mp3')
        self.search(self.pat1, self.txt2)
        try:
            self.button2.destroy()
        except Exception:
            print("Exception")

    def cmdbtn3_lvl1(self):
        print("Searching Pattern in selected String")
        playsound('groot2.mp3')
        self.search(self.pat1, self.txt3)
        try:
            self.button3.destroy()
        except Exception:
            print("Exception")

    def cmdbtn4_lvl1(self):
        print("Searching Pattern in selected String")
        playsound('groot2.mp3')
        self.search(self.pat1, self.txt4)
        try:
            self.button4.destroy()
        except Exception:
            print("Exception")

    def cmdbtn5_lvl1(self):
        print("Searching Pattern in selected String")
        playsound('groot2.mp3')
        self.search(self.pat1, self.txt5)
        try:
            self.button5.destroy()
        except Exception:
            print("Exception")

    def lvl1(self):
        self.lvl1 = Toplevel(self.root)
        self.pat1 = "Groot"
        self.lvl1.geometry('800x600')
        self.lvl1.title('lvl_1')
        self.lvl1.config(bg='white')

        task_lvl1 = Label(self.lvl1, text="Select strings with pattern \"Groot\"", font=7)
        task_lvl1.config(bg='white',font=("times new roman",22))
        task_lvl1.place(x=120, y=20)

        photo = PhotoImage(file="groot.png")
        label = Label(self.lvl1, image=photo)
        label.config(bg='white')
        label.place(x=350, y=300)

        self.txt1 = self.random_specific_string_generator_lvl_1(self.size, self.chars, random.randint(0, 12), self.pat1)
        self.button1 = Button(self.lvl1, text=self.txt1, bd=0, bg='white', fg='black', command=self.cmdbtn1_lvl1, font=20)
        self.button1.place(x=90, y=100)

        self.txt2 = self.random_specific_string_generator_lvl_1(self.size, self.chars, random.randint(0, 12), self.pat1)
        self.button2 = Button(self.lvl1, text=self.txt2, bd=0, bg='white', fg='black', command=self.cmdbtn2_lvl1, font=20)
        self.button2.place(x=300, y=100)

        self.txt3 = self.random_string_generator(self.size, self.chars)
        self.button3 = Button(self.lvl1, text=self.txt3, bd=0, bg='white', fg='black', command=self.cmdbtn3_lvl1, font=20)
        self.button3.place(x=90, y=300)

        self.txt4 = self.random_string_generator(self.size, self.chars)
        self.button4 = Button(self.lvl1, text=self.txt4, bd=0, bg='white', fg='black', command=self.cmdbtn4_lvl1, font=20)
        self.button4.place(x=300, y=300)

        self.txt5 = self.random_specific_string_generator_lvl_1(self.size, self.chars, random.randint(0, 12), self.pat1)
        self.button5 = Button(self.lvl1, text=self.txt5, bd=0, bg='white', fg='black', command=self.cmdbtn5_lvl1, font=20)
        self.button5.place(x=200, y=200)

        self.scoreLabel = Label(self.lvl1, text="Score: " + str(self.score), font=15)
        self.scoreLabel.place(x=0, y=0)
        self.scoreLabel.config(bg='white')
        self.scoreLabel.config(font=("game over", 40))

        self.lvl1.mainloop()
    # .......................................LEVEL_2................................
    def scoreUpdate_lvl2(self):
        self.scoreLabel.destroy()
        self.scoreLabel = Label(self.lvl2, text="Score: " + str(self.score), font=15)
        self.scoreLabel.config(bg='#adff2f')
        self.scoreLabel.place(x=0, y=0)
        self.scoreLabel.config(font=("game over", 40))

    def cmdbtn1_lvl2(self):
        print("Searching Pattern in selected String")
        playsound('pikachu22.mp3')
        self.search(self.pat2, self.txt1)
        try:
            self.button1.destroy()
        except Exception:
            print("Exception")

    def cmdbtn2_lvl2(self):
        print("Searching Pattern in selected String")
        playsound('pikachu22.mp3')
        self.search(self.pat2, self.txt2)
        try:
            self.button2.destroy()
        except Exception:
            print("Exception")

    def cmdbtn3_lvl2(self):
        print("Searching Pattern in selected String")
        playsound('pikachu22.mp3')
        self.search(self.pat2, self.txt3)
        try:
            self.button3.destroy()
        except Exception:
            print("Exception")

    def cmdbtn4_lvl2(self):
        print("Searching Pattern in selected String")
        playsound('pikachu22.mp3')
        self.search(self.pat2, self.txt4)
        try:
            self.button4.destroy()
        except Exception:
            print("Exception")

    def cmdbtn5_lvl2(self):
        print("Searching Pattern in selected String")
        playsound('pikachu22.mp3')
        self.search(self.pat2, self.txt5)
        try:
            self.button5.destroy()
        except Exception:
            print("Exception")

    def cmdbtn6_lvl2(self):
        print("Searching Pattern in selected String")
        playsound('pikachu22.mp3')
        self.search(self.pat2, self.txt6)
        try:
            self.button6.destroy()
        except Exception:
            print("Exception")

    def cmdbtn7_lvl2(self):
        print("Searching Pattern in selected String")
        playsound('pikachu22.mp3')
        self.search(self.pat2, self.txt7)
        try:
            self.button7.destroy()
        except Exception:
            print("Exception")

    def cmdbtn8_lvl2(self):
        print("Searching Pattern in selected String")
        playsound('pikachu22.mp3')
        self.search(self.pat2, self.txt8)
        try:
            self.button8.destroy()
        except Exception:
            print("Exception")

    def lvl2(self):
        self.lvl2 = Toplevel(self.root)
        self.pat2 = "Pikachu"
        self.lvl2.geometry('800x600')
        self.lvl2.title('lvl_2')
        self.lvl2.config(bg='#ADFF2F')

        task_lvl2 = Label(self.lvl2, text="Select strings with pattern \"Pikachu\"", font=7)
        task_lvl2.config(bg='#adff2f')
        task_lvl2.config(font=("Times new Roman", 22))
        task_lvl2.place(x=110, y=20)

        photo = PhotoImage(file="pikash.png")
        label = Label(self.lvl2, image=photo)
        label.config(bg='#ADFF2F')
        label.place(x=100, y=300)

        self.txt1 = self.random_specific_string_generator_lvl_1(self.size, self.chars, random.randint(0, 12), self.pat2)
        self.button1 = Button(self.lvl2, text=self.txt1, bd=0, bg='#ADFF2F', fg='black', command=self.cmdbtn1_lvl2, font=20)
        self.button1.place(x=100, y=100)

        self.txt2 = self.random_specific_string_generator_lvl_1(self.size, self.chars, random.randint(0, 12), self.pat2)
        self.button2 = Button(self.lvl2, text=self.txt2, bd=0, bg='#ADFF2F', fg='black', command=self.cmdbtn2_lvl2, font=20)
        self.button2.place(x=100, y=180)

        self.txt3 = self.random_string_generator(self.size, self.chars)
        self.button3 = Button(self.lvl2, text=self.txt3, bd=0, bg='#ADFF2F', fg='black', command=self.cmdbtn3_lvl2, font=20)
        self.button3.place(x=100, y=260)

        self.txt4 = self.random_string_generator(self.size, self.chars)
        self.button4 = Button(self.lvl2, text=self.txt4, bd=0, bg='#ADFF2F', fg='black', command=self.cmdbtn4_lvl2, font=20)
        self.button4.place(x=550, y=100)

        self.txt5 = self.random_specific_string_generator_lvl_1(self.size, self.chars, random.randint(0, 12), self.pat2)
        self.button5 = Button(self.lvl2, text=self.txt5, bd=0, bg='#ADFF2F', fg='black', command=self.cmdbtn5_lvl2, font=20)
        self.button5.place(x=550, y=180)

        self.txt6 = self.random_string_generator(self.size, self.chars)
        self.button6 = Button(self.lvl2, text=self.txt6, bd=0, bg='#ADFF2F', fg='black', command=self.cmdbtn6_lvl2, font=20)
        self.button6.place(x=550, y=260)

        self.txt7 = self.random_specific_string_generator_lvl_1(self.size, self.chars, random.randint(0, 12), self.pat2)
        self.button7 = Button(self.lvl2, text=self.txt7, bd=0, bg='#ADFF2F', fg='black', command=self.cmdbtn7_lvl2, font=20)
        self.button7.place(x=330, y=150)

        self.txt8 = self.random_string_generator(self.size, self.chars)
        self.button8 = Button(self.lvl2, text=self.txt8, bd=0, bg='#ADFF2F', fg='black', command=self.cmdbtn8_lvl2, font=20)
        self.button8.place(x=330, y=240)

        self.scoreLabel = Label(self.lvl2, text="Score: " + str(self.score), font=15)
        self.scoreLabel.place(x=0, y=0)
        self.scoreLabel.config(bg='#ADFF2F')
        self.scoreLabel.config(font=("Game Over", 40))
        self.lvl1.destroy()
        self.lvl2.mainloop()
    # ......................................FINAL STATE...........................
    def champion(self):
        self.lvl2.destroy()
        self.label1 = Label(self.root, text="Congrats!", font=10, bg='white')
        self.label1.place(x=150, y=400)
        self.label1.config(font=("Calibri", 15))
        self.label2 = Label(self.root, text="YOU WON!", fg="blue", bg="White")
        self.label2.place(x=150, y=430)
        self.label2.config(font=("Bleeding Cowboys", 18))
        print("\nYou Won\n")
        try:
            if self.labelGameOver:
                self.labelGameOver.destroy()
        except Exception:
            print("Exception")
        self.score = 0

    def gameOver(self):
        self.labelGameOver = Label(self.root, text="GAME OVER with Final Score: " + str(self.score),bg='white',fg='#b50000', font=10)
        self.labelGameOver.config(font=("Blood lust", 24))
        self.labelGameOver.place(x=25, y=400)
        print("\nGAME OVER\n")
        self.score = 0
        try:
            if self.lvl1:
                self.lvl1.destroy()
            if self.label1:
                self.label1.destroy()
                self.label2.destroy()
        except Exception:
            print("Exception")
        try:
            if self.lvl2:
                self.lvl2.destroy()
        except Exception:
            print("Exception")
    # ......................................INITIAL STATE........................
    def protocolhandler(self):
        if messagebox.askyesno("Exit", "Wanna leave?"):
            if messagebox.askyesno("Exit", "Are you sure?"):
                if messagebox.askyesno("Exit", "Really?"):
                    self.root.destroy()

    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x600')
        self.root.title('Stringus Automatas')
        self.root.protocol("WM_DELETE_WINDOW", self.protocolhandler)
      #  winsound.PlaySound('song.mp3', winsound.SND_ALIAS | winsound.SND_ASYNC)

        photo = PhotoImage(file="TFCS.png")
        label = Label(self.root, image=photo)
        label.place(x=0, y=0)

        gameName_1 = Label(self.root, text="Welcome to", bg='white',font=100)
        gameName_1.config(font=("magneto", 22))
        gameName_1.place(x=100, y=100)

        gameName_2 = Label(self.root, text="Stringus Automatas",bd=1,bg='white' ,font=100,fg='Dark green')
        gameName_2.config(font=("Harrington", 30,"bold"))
        gameName_2.place(x=100, y=150)

        gameName_3 = Label(self.root, text="-a game on Finite Automata",bg='white', font=100)
        gameName_3.config(font=("calibri", 18))
        gameName_3.place(x=180, y=215)

        playGame = Button(self.root, text="Play Game", bd=7, bg='black', fg='red', command=self.lvl1)
        playGame.config(font=("Digital-7",20))
        playGame.place(x=150, y=280)

        self.root.mainloop()

s = gameUI()