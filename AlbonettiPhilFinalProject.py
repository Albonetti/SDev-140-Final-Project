"""
Final Project
author: Phil Albonetti
created: 2023-12-17
IDE: Visual Studio Code
Description: This program lets users play Tic-Tac-Toe. It takes the users names and then passes
their names into the game board. 

PSEUDOCODE DESCRIPTION OF PROGRAM
This program performs the following steps:
1. imports tkinter for GUI interface
2. The first window introduces the game. User presses Yes if he or she wants to play.
3. The second window opens and takes the names of the two game players. The user presses Play to start.
4. The third window lets the users play the game. 
5. The game checks for a winner and announces that someone has won the game or if there is a tie. 
"""

# import necessary methods from tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox # import message box for various extra messages during game play


# create GLOBAL Variables for window colors
BG_WINDOW = "#FFF1E0"
LABEL_COLOR = "#6493AA"
BUTTON_FG = "#6B3C1B"
BUTTON_BG = "#6B3C1B"


# class for the names of the players
class Player_Names():
    def __init__(self):
        self.first_name = ""
        self.last_name = ""

# class for the third window, where the tic-tac-toe game takes place
class Third_Window(tk.Toplevel):
    def __init__(self, parent, p1_name, p2_name):
        super().__init__(parent)
        Player_Names.__init__(self) # import Player_Names to include them Second_Window

        # window configuration -- name and color
        self.title('The Game') # name
        self.config(bg=BG_WINDOW) # color
        
        # Variables for the sqr_click() function
        self.is_X = True # X will have the first move
        self.count = 0 # sets count to 0. Count used to determine how many moves left in game
        self.player1 = p1_name # player names, entered in 2nd window
        self.player2 = p2_name

        #region Squares
        # squares for each of the game tiles, starts with blank text
        # got help from Codemy.com tictactoe video on YouTube to create these buttons
        self.square1 = Button(self, text=" ", font=("Arial", 25), height=5, width=8, bg="silver",
                            command=lambda: self.sqr_click(self.square1))
        self.square2 = Button(self, text=" ", font=("Arial", 25), height=5, width=8, bg="silver",
                            command=lambda: self.sqr_click(self.square2))
        self.square3 = Button(self, text=" ", font=("Arial", 25), height=5, width=8, bg="silver",
                            command=lambda: self.sqr_click(self.square3))
        self.square4 = Button(self, text=" ", font=("Arial", 25), height=5, width=8, bg="silver",
                            command=lambda: self.sqr_click(self.square4))
        self.square5 = Button(self, text=" ", font=("Arial", 25), height=5, width=8, bg="silver",
                            command=lambda: self.sqr_click(self.square5))
        self.square6 = Button(self, text=" ", font=("Arial", 25), height=5, width=8, bg="silver",
                            command=lambda: self.sqr_click(self.square6))
        self.square7 = Button(self, text=" ", font=("Arial", 25), height=5, width=8, bg="silver",
                            command=lambda: self.sqr_click(self.square7))
        self.square8 = Button(self, text=" ", font=("Arial", 25), height=5, width=8, bg="silver",
                            command=lambda: self.sqr_click(self.square8))
        self.square9 = Button(self, text=" ", font=("Arial", 25), height=5, width=8, bg="silver",
                            command=lambda: self.sqr_click(self.square9))
        #endregion 


        # Player names for the game. self.player1 and self.player2 imports the names from Second_Window
        self.player1 = Button(self, text=self.player1, font=("Arial", 16), height=7, width=10, bg="silver",
                            command=Text)

        self.player2 = Button(self, text=self.player2, font=("Arial", 16), height=7, width=10, bg="silver", 
                            command=Text)      

        #region 12 grid spots on game board
        # top row of grid squares
        self.player1.grid(row=0, column=0) # name for player 1
        self.VSimage = tk.PhotoImage(file="StreetFighter2VS.gif") # VS sign from Street Fighter 2
        self.labelVS = Label(self, image=self.VSimage) 
        self.labelVS.grid(row=0, column=1)
        self.player2.grid(row=0, column=2) # name for player 2
        
        # second row of squares - first row of the tic-tac-toe game
        self.square1.grid(row=1, column=0)
        self.square2.grid(row=1, column=1)
        self.square3.grid(row=1, column=2)
        # third row of squares - second row of the tic-tac-toe game
        self.square4.grid(row=2, column=0)
        self.square5.grid(row=2, column=1)
        self.square6.grid(row=2, column=2)
        # fourth row of squares - third row of the tic-tac-toe game
        self.square7.grid(row=3, column=0)
        self.square8.grid(row=3, column=1)
        self.square9.grid(row=3, column=2)
        #endregion

    # checks if there is a winner to the game
    def check_for_winner(self):
        self.winner = False # set to false now and true once winner found

        # check rows for winner; checks for both 'X' and 'O'
        if self.square1["text"] == self.square2["text"] == self.square3["text"] and self.square1["text"] in ["X", "O"]:
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "Winner, Winner -- Chicken Dinner!")
        elif self.square4["text"] == self.square5["text"] == self.square6["text"] and self.square4["text"] in ["X", "O"]:
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "Winner, Winner -- Chicken Dinner!")
        elif self.square7["text"] == self.square8["text"] == self.square9["text"] and self.square7["text"] in ["X", "O"]:
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "Winner, Winner -- Chicken Dinner!")

        # check columns for winner
        if self.square1["text"] == self.square4["text"] == self.square7["text"] and self.square1["text"] in ["X", "O"]:
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "Winner, Winner -- Chicken Dinner!")
        elif self.square2["text"] == self.square5["text"] == self.square8["text"] and self.square2["text"] in ["X", "O"]:
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "Winner, Winner -- Chicken Dinner!")
        elif self.square3["text"] == self.square6["text"] == self.square9["text"] and self.square3["text"] in ["X", "O"]:
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "Winner, Winner -- Chicken Dinner!")

        # check diagonals for winner
        if self.square1["text"] == self.square5["text"] == self.square9["text"] and self.square1["text"] in ["X", "O"]:
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "Winner, Winner -- Chicken Dinner!")
        elif self.square3["text"] == self.square5["text"] == self.square7["text"] and self.square3["text"] in ["X", "O"]:
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "Winner, Winner -- Chicken Dinner!")


    # function that shifts squares from blank to X or blank to O
    def sqr_click(self, square):
        # sets blank square to X since X goes first (and since self.is_X set to True at beginning of program)
        if square["text"] == " " and self.is_X == True:
            square["text"] = "X" 
            self.is_X = False # change self.is_X so next move will create an O
            self.count += 1 # increment counter so that we can determine if the game ends in a tie
            self.check_for_winner()

        elif square["text"] == " " and self.is_X == False:
            square["text"] = "O"
            self.is_X = True
            self.count += 1
            self.check_for_winner()
        else: # input validation to ensure the user does not select a square that's already chosen
            messagebox.showerror("Tic-Tac-Toe", "Hey there, buddy. Can't do that.\n Someone's on that square.") 
        
        if self.count == 9: # message for a tie game
            messagebox.showerror("Tic-Tac-Toe", "It's a tie!") 

# class for the second window, where users can enter their names, if they so choose
class Second_Window(tk.Toplevel):

    def __init__(self, parent): #opening code to create window
        super().__init__(parent)

        # window configuration
        self.geometry('700x400') # size
        self.title('Player Names') # name
        self.config(bg=BG_WINDOW) # color
        
        # label to give instructions to the user
        label0 = Label(self,text="What are the player names?",font=("Arial",40),
                       borderwidth=1.2, relief="solid") # use Label method to create label
        label0.place(relx = 0.5, rely = 0.15, anchor = CENTER) # position label in the top middle of screen
        label0.config(bg=LABEL_COLOR) # label color

        # label to give instructions to the user
        label1 = Label(self,text="First player?",font=("Arial",22),
                       borderwidth=1.2, relief="solid") # use Label method to create label
        label1.place(relx = 0.3, rely = 0.35, anchor = CENTER) # position label in the left middle of screen
        label1.config(bg=LABEL_COLOR) # label color

        #create the data entry field for the user
        self.p1name = Entry(self)
        self.p1name.place(relx = 0.3, rely = 0.5, anchor = CENTER) # position data entry field in the left middle
        self.p1name.config(bg="#FFFFFF", fg="#000000") # colors for background and font of field


        # label to give instructions to the user
        label2 = Label(self,text="Second player?",font=("Arial",22),
                       borderwidth=1.2, relief="solid") # use Label method to create label
        label2.place(relx = 0.7, rely = 0.35, anchor = CENTER) # position label in the right middle
        label2.config(bg=LABEL_COLOR) # label color

        #create the data entry field for the user
        self.p2name = Entry(self)
        self.p2name.place(relx = 0.7, rely = 0.5, anchor = CENTER) # position data entry field in the right middle
        self.p2name.config(bg="#FFFFFF", fg="#000000") # colors for background and font of field
        
        # label to give instructions to the user
        label3 = Label(self,text="Click button to start.",font=("Arial",36),
                       borderwidth=1.2, relief="solid") # use Label method to create label
        label3.place(relx = 0.5, rely = 0.7, anchor = CENTER) # position label in the bottom center of screen
        label3.config(bg=LABEL_COLOR) # label color

        # Submit button to enter user names and open third window
        ttk.Button(self,text='Enter Names and Play', command=self.open_window_three).place(relx = 0.5, rely = 0.85, anchor = CENTER)
    
    # check that user entered names into the text entry boxes
    def check_for_names(self):
        # get both usernames from data entry fields
        p1_check = self.p1name.get()
        p2_check = self.p2name.get()
        # if statement to determine if user entered names 
        if p1_check != "" and p2_check != "":  
            return True # confirms user entered two names
        else: 
            # label to prompt user to input names
            prompt_label = tk.Label(self, text="Please enter two names.",font=("Arial",18),
                       borderwidth=1.2, relief="solid")
            prompt_label.place(relx = 0.5, rely = 0.93, anchor = CENTER)

    # function that brings user names from second window to third window
    def open_window_three(self):
        # if statement to confirm user entered names for name entry fields
        if self.check_for_names() == True: 
            p1_name = self.p1name.get() # get user names so I can pass them to Third_Window
            p2_name = self.p2name.get()
            # opens third window and passes user names to third window
            new_window = Third_Window(self, p1_name, p2_name)
            new_window.grab_set()


# class for the main window
class Main_Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # window configuration
        self.geometry('600x500') # size
        self.title('Tic-Tac-Toe') # name
        self.config(bg=BG_WINDOW) # color

        # informational label for the window
        label0 = Label(self,text="Tic-Tac-Toe",font=("Arial",40),
                       borderwidth=1.2, relief="solid")
        label0.place(relx = 0.5, rely = 0.1, anchor = CENTER) # label in top center of window
        label0.config(bg = LABEL_COLOR) # color
        
        # sub-label that goes below the top label
        label1 = Label(self,text="Want to Play? Click Yes if you do.", font=("Arial",30),
                       borderwidth=1.2, relief="solid")
        label1.place(relx = 0.5, rely = 0.25, anchor = CENTER) # position on scren
        label1.config(bg=LABEL_COLOR) # color

        # button to open the new window
        ttk.Button(self, text='Yes!', 
                   command=self.open_window).place(relx = 0.5, rely = 0.4, anchor = CENTER) # puts button in center of screen

        # image below the button
        self.image = tk.PhotoImage(file="image.gif")
        label2 = Label(self, image=self.image)
        label2.place(relx = 0.5, rely = 0.7, anchor = CENTER) # image in bottom center of screen
        label2.config(bg=LABEL_COLOR) # color

    # calls the 2nd window from the first window
    def open_window(self):
        window = Second_Window(self)
        window.grab_set()

# code to run the program
if __name__ == "__main__":
    app = Main_Window()
    app.mainloop()