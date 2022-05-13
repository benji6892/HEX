from tkinter import Tk, Label, Radiobutton, StringVar, Button, S, W, E, N, Frame, Listbox, END, Scrollbar, VERTICAL, DISABLED
from game import Game
from player import HumanPlayer, ComputerPlayer

font = ("Comic Sans MS", 20)


def display_welcome_window():
    welcome_window = Tk()
    welcome_window.geometry('600x600')
    welcome_window.grid_rowconfigure(0, pad=50)
    welcome_window.grid_rowconfigure(1, pad=50)
    welcome_window.grid_columnconfigure(0, pad=50)

    frame_player1 = Frame(welcome_window, background='white', padx=20, pady=10)
    frame_player1.grid(row=0, column=0)
    frame_player2 = Frame(welcome_window, background='white', padx=20, pady=10)
    frame_player2.grid(row=1, column=0)
    additional_frame = Frame(welcome_window, padx=25)
    additional_frame. grid(row=2, column=0, sticky=W)
    additional_frame.grid_columnconfigure(2, minsize=200)

    player_1_type = StringVar()
    colour_1 = StringVar()
    player_2_type = StringVar()
    colour_2 = StringVar()

    radio_buttons_colour_1 = display_form_player(frame_player1, player_1_type, 'Human', colour_1, 'blue', 1)
    radio_buttons_colour_2 = display_form_player(frame_player2, player_2_type, 'Computer', colour_2, 'red', 2)
    display_form_size_and_start_button(additional_frame, player_1_type, colour_1, player_2_type, colour_2)
    prevent_players_from_picking_same_colour(radio_buttons_colour_1, radio_buttons_colour_2, colour_1, colour_2)

    welcome_window.mainloop()


def display_form_player(frame_player, var_player_type, var_player_type_initial, var_colour, var_colour_initial,
                        player_index):
    frame_player.grid_columnconfigure(0, minsize=150)
    frame_player.grid_columnconfigure(1, minsize=150)
    frame_player.grid_columnconfigure(2, minsize=130)

    player = Label(frame_player, font=font, text=f'Player{player_index}: ', background='white')
    player.grid(row=0, column=0, rowspan=4, sticky=W)

    var_player_type.set(var_player_type_initial)
    player_types = ['Human', 'Computer']
    for i in range(0, len(player_types)):
        player_button = Radiobutton(frame_player, text=player_types[i], variable=var_player_type,
                                    value=player_types[i], font=font, indicatoron=False, width=10, borderwidth=4)
        player_button .grid(row=2 * i, column=1, rowspan=2, sticky=W + S, pady=5)

    var_colour.set(var_colour_initial)
    colour_list = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
    radio_buttons_colour = {}
    for i in range(0, len(colour_list)):
        column = 2 if int(i / 4) == 0 else 3
        colour = colour_list[i]
        button = Radiobutton(frame_player, variable=var_colour, value=colour, indicatoron=False,
                             background=colour, selectcolor=colour, width=5, borderwidth=5)
        button.grid(row=i % 4, column=column, sticky=E, padx=5)
        radio_buttons_colour[colour] = button
    return radio_buttons_colour


def display_form_size_and_start_button(frame, player_1_type, colour_1, player_2_type, colour_2):
    Label(frame, font=("Comic Sans MS", 17), text='Board size').grid(row=0, column=1)

    scrollbar = Scrollbar(frame, orient=VERTICAL)
    listbox = Listbox(frame, yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    scrollbar.grid(row=1, column=0, sticky=N + S)
    listbox.grid(row=1, column=1)
    for board_size in range(7, 21):
        listbox.insert(END, board_size)
    listbox.config(font=("Comic Sans MS", 12), height=5)
    listbox.select_set(4)

    command = lambda: start_game(player_1_type.get(), colour_1.get(), player_2_type.get(), colour_2.get(),
                                 listbox.curselection())
    start_button = Button(frame, text='Start', borderwidth=4, command=command, font=font, background='green')
    start_button.grid(row=1, column=2, sticky=E)


def start_game(player1_type, player1_colour, player2_type, player2_colour, size_selection):
    size = 7 + int(size_selection[0])
    player1 = HumanPlayer(player1_colour) if player1_type == 'Human' else ComputerPlayer(player1_colour, size)
    player2 = HumanPlayer(player2_colour) if player2_type == 'Human' else ComputerPlayer(player2_colour, size)
    window = Tk()
    Game(size, player1, player2, window)
    window.mainloop()


def prevent_players_from_picking_same_colour(radio_buttons_colour_1, radio_buttons_colour_2, colour_1, colour_2):
    for colour in radio_buttons_colour_1:
        radio_buttons_colour_1[colour].config(command=lambda: radio_button_colour_command(colour_1, colour_2))
        radio_buttons_colour_2[colour].config(command=lambda: radio_button_colour_command(colour_2, colour_1))


def radio_button_colour_command(my_var_colour, other_var_colour):
    default1 = 'blue'
    default2 = 'red'
    if my_var_colour.get() == other_var_colour.get():
        if my_var_colour.get() == default1:
            other_var_colour.set(default2)
        else:
            other_var_colour.set(default1)
