import tkinter

import customtkinter as ctk
import controller
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Gui(ctk.CTk):
    def __init__(self):
        # initialization
        super().__init__()
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.title("Bezier Curve Generator with Midpoint Algorithm")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # attribute
        self.XPointInput = []
        self.YPointInput = []
        self.solutionResult = []
        self.titikBantu = []
        self.mainPage = ctk.CTkFrame(self)
        self.pageThree = ctk.CTkFrame(self)
        self.pageN = ctk.CTkFrame(self)
        self.error = ""
        
        # create frame
        self.create_main_page()
        self.create_page_three()
        self.create_page_n()

        # show page
        self.show_page(self.mainPage)
        
        
    def create_main_page(self):
        # configure root for main
        self.title("Bezier Curve Generator with Midpoint Algorithm")
        self.geometry('400x200')

        # configure main page frame
        self.mainPage.columnconfigure(0, weight=2)
        self.mainPage.rowconfigure((0, 1, 2), weight=2)

        # configure items in main page
        title = ctk.CTkLabel(self.mainPage, text="Kurva Bezier dengan Algoritma Midpoint",
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
        self.geometry('500x350')
        self.title("Bezier Curve from Three Points")

        # configure frame
        self.pageThree.grid_columnconfigure((0, 1, 2), weight=1)
        self.pageThree.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

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

        # submit button
        submitButton = ctk.CTkButton(self.pageThree, text="Submit", font=ctk.CTkFont(family="Calibri", size=22),
                                     hover_color="#02a4b0", command=lambda: self.convertInput([input1X, input2X, input3X],
                                                                                              [input1Y, input2Y, input3Y]))
        submitButton.grid(row=4, column=0, columnspan=3)


    # convert the entry into integer and validate it
    def convertInput(self, getEntryX, getEntryY):
        try:
            for i in range(len(getEntryX)):
                self.XPointInput.append(int(getEntryX[i].get()))
                self.YPointInput.append(int(getEntryY[i].get()))
            self.error = ""
            errorLabel = ctk.CTkLabel(self.pageThree, font=ctk.CTkFont(family="Calibri", size=14), text_color="red",
                                      text=self.error)
            errorLabel.grid(row=5, column=0, columnspan=3)
        except ValueError:
            self.XPointInput = []
            self.YPointInput = []
            self.error = "Input tidak valid! Masukan tidak boleh kosong dan harus berupa integer!"
            # error label
            errorLabel = ctk.CTkLabel(self.pageThree, font=ctk.CTkFont(family="Calibri", size=14), text_color="red",
                                      text=self.error)
            errorLabel.grid(row=5, column=0, columnspan=3)

    def create_page_n(self):
        return


    def show_page(self, page):
        # hide all pages
        self.mainPage.grid_forget()
        self.pageN.grid_forget()
        self.pageThree.grid_forget()

        # show target page
        page.grid(row=0, column=0, sticky="nsew")


def showPlot(arrayOfPoints, arrayOfSol):
    # Show main bezier plot result
    plt.plot([point[0] for point in arrayOfSol], [point[1] for point in arrayOfSol], 'bo-', label="Kurva Bezier")
    # Show points in the bezier
    plt.title("Kurva Graf Bezier dengan Algoritma Titik Tengah")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    App = Gui()
    App.mainloop()