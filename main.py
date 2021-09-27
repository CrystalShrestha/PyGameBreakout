from breakouttwo import Game
import username
import global_imports


username.main()
if global_imports.running:
    g = Game()

    while g.running:
        g.curr_menu.display_menu()
        g.game_loop()
