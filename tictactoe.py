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
                return     
            elif turn == 11:
                label.configure(text = "Draw!!!")
                reset()        

    def reset():
        button_reset = customtkinter.CTkButton(app, text="Reset", command=b_reset, text_color="white", fg_color="red", width=52.5, hover_color="dark red")
        button_reset.place(relx=0.875, rely=0.95, anchor=customtkinter.CENTER)

    def b_reset():
        label.destroy()
        main()


    button_positions = [(0.2, 0.8), (0.5, 0.8), (0.8, 0.8), (0.2, 0.59), (0.5, 0.59), (0.8, 0.59), (0.2, 0.38), (0.5, 0.38), (0.8, 0.38)]
    buttons = []

    for i, position in enumerate(button_positions):
        button = customtkinter.CTkButton(app, text="", command=lambda i=i: button_event(buttons[i]), width=105, height=105, text_color="white")
        button.place(relx=position[0], rely=position[1], anchor=customtkinter.CENTER)
        buttons.append(button)

    label = customtkinter.CTkLabel(app, text="Player 1's turn", fg_color="transparent", font=("Arial", 28))
    label.place(relx=0.5, rely=0.13, anchor=customtkinter.CENTER)

    app.mainloop()  
    
if __name__ == "__main__":
    main()
