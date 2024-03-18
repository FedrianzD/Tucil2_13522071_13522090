import time

import customtkinter as ctk
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

import function

class Gui(ctk.CTk):
    def __init__(self):
        # initialization
        super().__init__()
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.title("Bezier Curve Generator with Divide and Conquer Algorithm")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # attribute
        self.XPointInput = []
        self.YPointInput = []
        self.solutionResult = []
        self.arrayOfInput = []
        self.titikBantu = []
        self.mainPage = ctk.CTkFrame(self)
        self.pageThree = ctk.CTkFrame(self)
        self.pageN = ctk.CTkFrame(self)
        self.pagePlot = ctk.CTkFrame(self)
        self.error = ""
        
        # create frame
        self.create_main_page()
        self.create_page_three()
        self.create_page_n()

        # show page
        self.show_page(self.mainPage)
        
        
    def create_main_page(self):
        # configure root for main
        self.title = "Bezier Curve Generator with Divide and Conquer Algorithm"
        self.geometry('500x200')

        # configure main page frame
        self.mainPage.columnconfigure(0, weight=2)
        self.mainPage.rowconfigure((0, 1, 2), weight=2)

        # configure items in main page
        title = ctk.CTkLabel(self.mainPage, text="Kurva Bezier dengan Algoritma Divide and Conquer",
                             font=ctk.CTkFont(family="Calibri", size=24, weight="bold"))
        title.grid(row=0, column=0)
        openThree = ctk.CTkButton(self.mainPage, text="Start with Three Point Input", hover_color="#0ed9e8",
                                  font=ctk.CTkFont(family="Calibri", size=18, weight="bold"),
                                  command=lambda: self.show_page(self.pageThree))
        openThree.grid(row=1, column=0)
        openN = ctk.CTkButton(self.mainPage, text="Start with n-Point Input", hover_color="#0ed9e8",
                              font=ctk.CTkFont(family="Calibri", size=18, weight="bold"),
                              command=lambda: self.show_page(self.pageN))
        openN.grid(row=2, column=0)


    def create_page_three(self):
        # configure root window
        self.geometry('700x400')
        self.title = "Bezier Curve from 3 Points"

        # configure frame
        self.pageThree.grid_columnconfigure((0, 1, 2), weight=1)
        self.pageThree.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        # configure title
        title = ctk.CTkLabel(self.pageThree, text="Kurva Bezier dengan 3 Titik",
                             font=ctk.CTkFont(family="Calibri", size=22, weight="bold"))
        title.grid(row=0, column=1)

        back = ctk.CTkButton(self.pageThree, text="Main Menu", font=ctk.CTkFont(family="Calibri", size=14),
                             command=lambda: self.show_page(self.mainPage))
        back.grid(row=0, column=2)

        # input 1
        labelInput1 = ctk.CTkLabel(self.pageThree, text="Titik 1:", font=ctk.CTkFont(family="Calibri", size=16))
        labelInput1.grid(row=1, column=0)
        input1X = ctk.CTkEntry(self.pageThree, placeholder_text="x1", font=ctk.CTkFont(family="Calibri", size=14))
        input1X.grid(row=1, column=1)
        input1Y = ctk.CTkEntry(self.pageThree, placeholder_text="y1", font=ctk.CTkFont(family="Calibri", size=14))
        input1Y.grid(row=1, column=2)

        # input coordinate 2
        labelInput2 = ctk.CTkLabel(self.pageThree, text="Titik 2:", font=ctk.CTkFont(family="Calibri", size=16))
        labelInput2.grid(row=2, column=0)
        input2X = ctk.CTkEntry(self.pageThree, placeholder_text="x2", font=ctk.CTkFont(family="Calibri", size=14))
        input2X.grid(row=2, column=1)
        input2Y = ctk.CTkEntry(self.pageThree, placeholder_text="y2", font=ctk.CTkFont(family="Calibri", size=14))
        input2Y.grid(row=2, column=2)

        # input coordinate 3
        labelInput3 = ctk.CTkLabel(self.pageThree, text="Titik 3:", font=ctk.CTkFont(family="Calibri", size=16))
        labelInput3.grid(row=3, column=0)
        input3X = ctk.CTkEntry(self.pageThree, placeholder_text="x3", font=ctk.CTkFont(family="Calibri", size=14))
        input3X.grid(row=3, column=1)
        input3Y = ctk.CTkEntry(self.pageThree, placeholder_text="y3", font=ctk.CTkFont(family="Calibri", size=14))
        input3Y.grid(row=3, column=2)

        # input iterasi
        labelIterasi = ctk.CTkLabel(self.pageThree, text="Iterasi (positif):", font=ctk.CTkFont(family="Calibri", size=16))
        labelIterasi.grid(row=4, column=0, columnspan=2)
        inputIterasi = ctk.CTkEntry(self.pageThree, placeholder_text="iterasi", font=ctk.CTkFont(family="Calibri", size=14))
        inputIterasi.grid(row=4, column=2)

        # submit button
        submitButton = ctk.CTkButton(self.pageThree, text="Submit", font=ctk.CTkFont(family="Calibri", size=22),
                                     hover_color="#02a4b0", command=lambda: self.process3Point([input1X, input2X, input3X],
                                                                                              [input1Y, input2Y, input3Y],
                                                                                               inputIterasi))
        submitButton.grid(row=6, column=0, columnspan=3)
    
    
    def create_page_n(self):
        # configure window
        self.title = "Bezier Curve from N-Points"
        self.pageN.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.pageN.columnconfigure((0, 1), weight=1)
        
        # configure title
        title = ctk.CTkLabel(self.pageN, text="Kurva Bezier dengan n Titik",
                             font=ctk.CTkFont(family="Calibri", size=22, weight="bold"))
        title.grid(row=0, column=0)
        
        # back button
        back = ctk.CTkButton(self.pageN, text="Main Menu", font=ctk.CTkFont(family="Calibri", size=14),
                             command=lambda: self.show_page(self.mainPage))
        back.grid(row=0, column=1)
        
        # label input
        labelInput = ctk.CTkLabel(self.pageN, text="Masukan jumlah titik:", font=ctk.CTkFont(family="Calibri", size=16))
        labelInput.grid(row=1, column=0, columnspan=2)
        
        # input entry
        inputNX = ctk.CTkEntry(self.pageN, placeholder_text="x1", font=ctk.CTkFont(family="Calibri", size=14))
        inputNX.grid(row=2, column=0)
        
        inputNY = ctk.CTkEntry(self.pageN, placeholder_text="y1", font=ctk.CTkFont(family="Calibri", size=14))
        inputNY.grid(row=2, column=1)
        
        # input iterasi
        labelIterasi = ctk.CTkLabel(self.pageN, text="Iterasi (positif):", font=ctk.CTkFont(family="Calibri", size=16))
        labelIterasi.grid(row=3, column=0)
        inputIterasi = ctk.CTkEntry(self.pageN, placeholder_text="iterasi", font=ctk.CTkFont(family="Calibri", size=14))
        inputIterasi.grid(row=3, column=1)

        # instruction button
        instruction = ctk.CTkLabel(self.pageN, text=f'Pisahkan setiap titik dengan titik koma (;)\nBanyak titik X harus sama dengan titik Y',
                                          font=ctk.CTkFont(family="Calibri", size=14))
        instruction.grid(row=4, column=0, columnspan=2)

        # submit button
        submitButton = ctk.CTkButton(self.pageN, text="Submit", font=ctk.CTkFont(family="Calibri", size=22),
                                     hover_color="#02a4b0", command=lambda: self.processNPoint(inputNX, inputNY, inputIterasi))
        submitButton.grid(row=5, column=0, columnspan=2)
        
    # convert the entry into integer and validate it
    def process3Point(self, getEntryX, getEntryY, iteration):
        self.XPointInput = []
        self.YPointInput = []
        self.error = ""
        self.arrayOfInput = []
        self.titikBantu = []
        self.solutionResult = []
        try:
            # get input coordinate
            for i in range(len(getEntryX)):
                self.XPointInput.append(float(getEntryX[i].get()))
                self.YPointInput.append(float(getEntryY[i].get()))
            self.error = ""
            errorLabel = ctk.CTkLabel(self.pageThree, font=ctk.CTkFont(family="Calibri", size=14), text_color="blue",
                                      text=self.error)
            errorLabel.grid(row=7, column=0, columnspan=3)

            # get iteration
            iterate = int(iteration.get())
            if iterate <= 0:
                self.error = "Iterasi harus positif!"
                self.XPointInput = []
                self.YPointInput = []
                errorLabel.grid_forget()
                errorLabel = ctk.CTkLabel(self.pageThree, font=ctk.CTkFont(family="Calibri", size=14), text_color="red",
                                          text=self.error)
                errorLabel.grid(row=7, column=0, columnspan=3)
                return

            errorLabel = ctk.CTkLabel(self.pageThree, font=ctk.CTkFont(family="Calibri", size=14), text_color="blue",
                                          text="Loading...")
            errorLabel.grid(row=7, column=0, columnspan=3)
            # process into bezier function
            self.arrayOfInput = [(self.XPointInput[0], self.YPointInput[0]),
                            (self.XPointInput[1], self.YPointInput[1]),
                            (self.XPointInput[2], self.YPointInput[2])]
            firstMidTime = time.time()
            self.solutionResult = function.Bezier3Point(self.arrayOfInput[0], self.arrayOfInput[1], self.arrayOfInput[2], 1, iterate)
            lastMidTime = time.time()
            self.titikBantu = function.Bezier3PointHelper(self.arrayOfInput[0], self.arrayOfInput[1], self.arrayOfInput[2], 1, iterate)
            self.titikBantu = function.parseArrayNPoint(self.titikBantu)
            firstBruteTime = time.time()
            sol2 = function.BezierBruteforce(self.arrayOfInput[0], self.arrayOfInput[1], self.arrayOfInput[2], iterate)
            lastBruteTime = time.time()
            errorLabel.grid_forget()
            errorLabel = ctk.CTkLabel(self.pageThree, font=ctk.CTkFont(family="Calibri", size=14), text_color="blue",
                                        text=f'Waktu eksekusi (DnC algorithm): {(lastMidTime-firstMidTime) * 1000} ms\n'
                                             f'Waktu eksekusi (Bruteforce algorithm): {(lastBruteTime-firstBruteTime) * 1000} ms')
            errorLabel.grid(row=7, column=0, columnspan=3)
            function.animatePlot(self.arrayOfInput, self.solutionResult, self.titikBantu)

        except ValueError:
            self.XPointInput = []
            self.YPointInput = []
            print(ValueError)
            self.error = "Input tidak valid! Masukan tidak boleh kosong dan harus berupa bilangan!"
            errorLabel = ctk.CTkLabel(self.pageThree, font=ctk.CTkFont(family="Calibri", size=14), text_color="red",
                                      text=self.error)
            errorLabel.grid(row=7, column=0, columnspan=3)
        errorLabel.grid_forget()

    def processNPoint(self, getEntryX, getEntryY, iteration):
        self.XPointInput = []
        self.YPointInput = []
        self.error = ""
        self.titikBantu = []
        self.solutionResult = []
        self.arrayOfInput = []

        try:
            stringX = getEntryX.get()
            stringY = getEntryY.get()

            self.XPointInput = [float(x) for x in stringX.split(';')]
            self.YPointInput = [float(y) for y in stringY.split(';')]

            if len(self.XPointInput) != len(self.YPointInput):
                self.error = "Banyak titik X harus sama dengan titik Y!"
                errorLabel = ctk.CTkLabel(self.pageN, font=ctk.CTkFont(family="Calibri", size=14), text_color="red",
                                          text=self.error)
                self.XPointInput = []
                self.YPointInput = []
                errorLabel.grid(row=6, column=0, columnspan=3)
                return
            iterate = int(iteration.get())
            if iterate <= 0:
                self.error = "Iterasi harus positif!"
                self.XPointInput = []
                self.YPointInput = []
                errorLabel = ctk.CTkLabel(self.pageN, font=ctk.CTkFont(family="Calibri", size=14), text_color="red",
                                          text=self.error)
                errorLabel.grid(row=6, column=0, columnspan=3)
                return
            self.arrayOfInput = [(self.XPointInput[i], self.YPointInput[i]) for i in range(len(self.XPointInput))]

            startTime = time.time()
            self.solutionResult, self.titikBantu = function.BezierNPoint(self.arrayOfInput, 1, iterate)
            endTime = time.time()
            self.titikBantu = function.parseArrayNPoint(self.titikBantu)
            errorLabel = ctk.CTkLabel(self.pageN, font=ctk.CTkFont(family="Calibri", size=14), text_color="blue",
                                      text=f'Waktu eksekusi: {(endTime-startTime) * 1000} ms')
            errorLabel.grid(row=6, column=0, columnspan=3)
            temp = function.parseArrayNPoint(self.titikBantu)
            function.animatePlot(self.arrayOfInput, self.solutionResult, temp)

        except ValueError:
            self.XPointInput = []
            self.YPointInput = []
            self.error = "Input tidak valid! Masukan tidak boleh kosong dan harus berupa integer!"
            errorLabel = ctk.CTkLabel(self.pageN, font=ctk.CTkFont(family="Calibri", size=14), text_color="red",
                                      text=self.error)
            errorLabel.grid(row=6, column=0, columnspan=3)
        errorLabel.grid_forget()

    def show_page(self, page):
        # hide all pages
        self.mainPage.grid_forget()
        self.pageN.grid_forget()
        self.pageThree.grid_forget()

        # show target page
        page.grid(row=0, column=0, sticky="nsew")

