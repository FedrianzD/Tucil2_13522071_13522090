import customtkinter as ctk

def createMainWindow():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    mainWindow = ctk.CTk()

    mainWindow.title("Bezier Curve Generator with Midpoint Algorithm")
    mainWindow.geometry('200x200')
    mainWindow.columnconfigure(0, weight=1)
    mainWindow.rowconfigure(0, weight=1)
    startButton = ctk.CTkButton(mainWindow, text="Start", hover_color="#0ed9e8")
    startButton.grid(row=0, column=0)
    mainWindow.mainloop()

# show window for input of three point
def createThreePointWindow():
    # initialization and config of window
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    threePointWindow = ctk.CTk()
    threePointWindow.title("Bezier Curve from Three Points")
    threePointWindow.geometry('600x400')
    threePointWindow.grid_columnconfigure((0, 1, 2), weight=1)
    threePointWindow.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

    # main title in frame
    title = ctk.CTkLabel(threePointWindow, text="Kurva Bezier dengan 3 Titik", font=ctk.CTkFont(family="Calibri", size=22, weight="bold"))
    title.grid(row=0, column=1)

    #input coordinate 1
    labelInput1 = ctk.CTkLabel(threePointWindow, text="Titik 1:", font=ctk.CTkFont(family="Calibri", size=16))
    labelInput1.grid(row=1, column=0)
    input1X = ctk.CTkEntry(threePointWindow, placeholder_text="x1", font=ctk.CTkFont(family="Calibri", size=14))
    input1X.grid(row=1, column=1)
    input1Y = ctk.CTkEntry(threePointWindow, placeholder_text="y1", font=ctk.CTkFont(family="Calibri", size=14))
    input1Y.grid(row=1, column=2)

    #input coordinate 2
    labelInput2 = ctk.CTkLabel(threePointWindow, text="Titik 2:", font=ctk.CTkFont(family="Calibri", size=16))
    labelInput2.grid(row=2, column=0)
    input2X = ctk.CTkEntry(threePointWindow, placeholder_text="x2", font=ctk.CTkFont(family="Calibri", size=14))
    input2X.grid(row=2, column=1)
    input2Y = ctk.CTkEntry(threePointWindow, placeholder_text="y2", font=ctk.CTkFont(family="Calibri", size=14))
    input2Y.grid(row=2, column=2)

    #input coordinate 3
    labelInput3 = ctk.CTkLabel(threePointWindow, text="Titik 3:", font=ctk.CTkFont(family="Calibri", size=16))
    labelInput3.grid(row=3, column=0)
    input3X = ctk.CTkEntry(threePointWindow, placeholder_text="x3", font=ctk.CTkFont(family="Calibri", size=14))
    input3X.grid(row=3, column=1)
    input3Y = ctk.CTkEntry(threePointWindow, placeholder_text="y3", font=ctk.CTkFont(family="Calibri", size=14))
    input3Y.grid(row=3, column=2)

    # error label
    errorLabel = ctk.CTkLabel(threePointWindow, font=ctk.CTkFont(family="Calibri", size=18), text_color="red", text="")
    errorLabel.grid(row=4, column=1)

    # submit button
    submitButton = ctk.CTkButton(threePointWindow, text="Submit", font=ctk.CTkFont(family="Calibri", size=16), hover_color="#02a4b0")
    submitButton.grid(row=5, column=1)

    # mainloop of window
    threePointWindow.mainloop()




if __name__ == "__main__":
    createThreePointWindow()