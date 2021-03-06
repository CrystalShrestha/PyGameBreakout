import pygame
import mongodb


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.leaderboardx, self.leaderboardy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):  # Menu
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 20)  # Menu text

            self.game.draw_text(
                "Start Game", 20, self.startx, self.starty)  # Button
            self.game.draw_text(
                "Controls", 20, self.controlsx, self.controlsy)  # Button
            self.game.draw_text("Credits", 20, self.creditsx,
                                self.creditsy)  # Button
            self.game.draw_text("Leaderboard", 20, self.leaderboardx,
                                self.leaderboardy)  # Button
            self.cursor()  # Generate cursor
            self.blit_screen()  # Generate Screen

    def move_cursor(self):  # Menu cursor
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.controlsx + self.offset, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (
                    self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (
                    self.leaderboardx + self.offset, self.leaderboardy)
                self.state = 'Leaderboard'
            elif self.state == 'Leaderboard':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.leaderboardx + self.offset, self.leaderboardy)
                self.state = 'Leaderboard'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (
                    self.controlsx + self.offset, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Leaderboard':
                self.cursor_rect.midtop = (
                    self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Controls':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Leaderboard':
                self.game.curr_menu = self.game.leaderboard
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Controls'
        self.leftx, self.lefty = self.mid_w, self.mid_h + 20
        self.rightx, self.righty = self.mid_w, self.mid_h + 40
        self.escx, self.escy = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.rightx + self.offset, self.righty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.chk_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text(
                'Controls', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Left Arrow Key", 15, self.leftx, self.lefty)
            self.game.draw_text("Right Arrow Key", 15,
                                self.rightx, self.righty)
            self.game.draw_text("Esc To Exit", 15, self.escx, self.escy)

            self.blit_screen()

    def chk_input(self):
        if self.game.BACK_KEY or self.game.START_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False

        elif self.game.START_KEY:
            pass


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(
                'Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text(
                'Samana Shrestha', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text(
                'Crystal Shrestha', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text(
                'Sujan Rijal', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)

            self.blit_screen()


class LeaderboardMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        allscores = mongodb.fetch_scores()

        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(
                'Leaderboards', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)

            # Loop through the MongoDB scores table
            for i in range(len(allscores)):
                pos = (i + 1) * 20
                self.game.draw_text(
                    (allscores[i].get('user_name') + "    " + str(allscores[i].get('score')) + "     " + allscores[i].get('time')), 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + pos)
            self.blit_screen()
