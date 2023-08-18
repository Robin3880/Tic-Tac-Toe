import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue") 

app = customtkinter.CTk() 
app.title("TicTacToe")
app.geometry("350x500")
app.resizable(False, False)

winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]  
]

def main():
    global turn
    turn = 2


    def button_event(x):
        if x.cget("text") == "" and "Game Over" not in label.cget("text"): 
            global turn
            if turn % 2 == 0:
                x.configure(text="X", font = ("Arial", 38))
                turn += 1
                
            else:
                x.configure(text="O", font = ("Arial", 38))
                turn += 1
        else:
            pass
        call_turn()
        checkwin()


    def call_turn():
        global turn
        if turn % 2 == 0:
            label.configure(text="Players 1's turn")
        else:
            label.configure(text="Players 2's turn")

    def checkwin():
        global turn
        for combination in winning_combinations:
            if all(buttons[i].cget("text") == buttons[combination[0]].cget("text") != "" for i in combination):
                if turn % 2 == 0:
                    label.configure(text= f"Game Over, Player 2 wins!")
                else:
                    label.configure(text= f"Game Over, Player 1 wins!")
                reset()         
        if turn == 11:
            label.configure(text = "Draw!!!")
            reset()        

    def reset():
        button_reset = customtkinter.CTkButton(app, text="Reset", command=b_reset, text_color="white", fg_color="red", width=52.5, hover_color="dark red")
        button_reset.place(relx=0.875, rely=0.95, anchor=customtkinter.CENTER)

    def b_reset():
        label.destroy()
        main()

    button1 = customtkinter.CTkButton(app, text="", command=lambda: button_event(button1), width=105, height=105, text_color="white")
    button1.place(relx=0.2, rely=0.8, anchor=customtkinter.CENTER)

    button2 = customtkinter.CTkButton(app, text="", command=lambda: button_event(button2), width=105, height=105, text_color="white")
    button2.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

    button3 = customtkinter.CTkButton(app, text="", command=lambda: button_event(button3), width=105, height=105, text_color="white")
    button3.place(relx=0.8, rely=0.8, anchor=customtkinter.CENTER)

    button4 = customtkinter.CTkButton(app, text="", command=lambda: button_event(button4), width=105, height=105, text_color="white")
    button4.place(relx=0.2, rely=0.59, anchor=customtkinter.CENTER)

    button5 = customtkinter.CTkButton(app, text="", command=lambda: button_event(button5), width=105, height=105, text_color="white")
    button5.place(relx=0.5, rely=0.59, anchor=customtkinter.CENTER)

    button6 = customtkinter.CTkButton(app, text="", command=lambda: button_event(button6), width=105, height=105, text_color="white")
    button6.place(relx=0.8, rely=0.59, anchor=customtkinter.CENTER)

    button7 = customtkinter.CTkButton(app, text="", command=lambda: button_event(button7), width=105, height=105, text_color="white")
    button7.place(relx=0.2, rely=0.38, anchor=customtkinter.CENTER)

    button8 = customtkinter.CTkButton(app, text="", command=lambda: button_event(button8), width=105, height=105, text_color="white")
    button8.place(relx=0.5, rely=0.38, anchor=customtkinter.CENTER)

    button9 = customtkinter.CTkButton(app, text="", command=lambda: button_event(button9), width=105, height=105, text_color="white")
    button9.place(relx=0.8, rely=0.38, anchor=customtkinter.CENTER)

    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

    label = customtkinter.CTkLabel(app, text="Player 1's turn", fg_color="transparent", font=("Arial", 28))
    label.place(relx=0.5, rely=0.13, anchor=customtkinter.CENTER)

    app.mainloop() 

if __name__ == "__main__":
    main()
