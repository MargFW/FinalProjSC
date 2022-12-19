import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
TITLE = "ROBO RUNNERS"


class RObotGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color((237, 251, 255))

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        # Your drawing code goes here
        # Clear the screen to the background color
        self.clear()

        # Draw our sprites
        self.wall_list.draw()
        self.player_list.draw()
        
    def on_key_press(self):
        pass

    def on_update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()