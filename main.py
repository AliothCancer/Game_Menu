from menu_screen import menu_screen
from new_game import new_game
from load_game import load_game
from settings import settings



selector_counter = 0
while True:
    option = menu_screen(selector_counter)
    print(option)
    if option == "Start a new game":
        new_game()

    elif option == "Load a game":
        load_game()

    elif option == "Settings":
        settings()

    elif option == "Exit":
        break

