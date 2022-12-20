"""
EN.640.635 Software Carpentry.

Final Project - Robot Runner

This program will visually  actuate a robot  of the player's choosing.
Actuation can be put together into a moview for paper schematics  or
basic modeling.
"""

# Importing Modules
import arcade
import arcade.gui


def nlegs():
    """
    Allow player to choose the amount of legs.

    **Parameters**

        None

    **Returns**

        nlegs : *int*
            The  number of legs on the robot.

    """
    print("We need a few variables to start. \n")
    while True:
        try:
            numlegs = input("\n Amount of Legs (between 2 and 4):")
            nlegs = int(numlegs)
        except ValueError:
            print("Please enter a number.\n")
        else:
            if nlegs <= 4 and nlegs >= 2:
                break
            else:
                print("That is an inviable number of legs. Try again.")
    return nlegs


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Robo Runner"
CHARACTER_SCALING = 0.1


class Player(arcade.Sprite):
    """
    A class to represent the player.

    Attributes
    ----------
    scale: *float*
        Sets the scale of the  acutal image to  what's used.
    currentrobot: *int*
        The index of the current texture for the robot.
    robot_textures: *list*
        A list containing all the textures for the robot animation.
    frames: *int*
        Numbers the frames of each texture.

    Methods
    -------
    _init_(self):
        initiates the player.
    update_animation(self, delta_time:float = 1):
        updates the robot to the specific type required by frame.

    """

    def __init__(self):
        """
        Intiates the class.

        **Parameters**

            None

        **Returns**

            None

        """
        super().__init__()
        self.scale = CHARACTER_SCALING
        self.currentrobot = 0
        self.robot_textures = []
        self.frames = 45
        for i in range(500):
            self.robot_textures.append(
                                       arcade.load_texture(
                                           "ImagesforRoborunner/normal.png"))
        for i in range(self.frames):
            self.robot_textures.append(
                                       arcade.load_texture(
                                           "ImagesforRoborunner/swell1.png"))
        for i in range(self.frames):
            self.robot_textures.append(
                                       arcade.load_texture(
                                           "ImagesforRoborunner/swell2.png"))
        for i in range(self.frames):
            self.robot_textures.append(
                                       arcade.load_texture(
                                           "ImagesforRoborunner/swell1.png"))
        for i in range(self.frames):
            self.robot_textures.append(
                                       arcade.load_texture(
                                           "ImagesforRoborunner/normal.png"))
        for i in range(self.frames):
            self.robot_textures.append(
                                       arcade.load_texture(
                                           "ImagesforRoborunner/deswell1.png"))
        for i in range(self.frames):
            self.robot_textures.append(
                                       arcade.load_texture(
                                           "ImagesforRoborunner/deswell2.png"))
        for i in range(self.frames):
            self.robot_textures.append(
                                       arcade.load_texture(
                                           "ImagesforRoborunner/deswell1.png"))
        for i in range(self.frames):
            self.robot_textures.append(
                                       arcade.load_texture(
                                           "ImagesforRoborunner/normal.png"))
        for i in range(20):
            self.robot_textures.append(
                                       arcade.load_texture(
                                           "ImagesforRoborunner/normal.png"))

    def update_animation(self, delta_time: float = 1):
        """
        Update the robot image to the right animation frame.

        **Parameters**

            None

        **Returns**

            None

        """
        total = (self.frames*8)+500+20
        if self.currentrobot >= total-1:
            self.currentrobot = 500
        else:
            self.currentrobot += 1
            self.texture = self.robot_textures[self.currentrobot]


class StartView(arcade.View):
    """
    A class to represent the start screen.

    Attributes
    ----------
    uimanager: *arcade.gui.UIManager*
        Manages the UI and GUI features for this program.
    start_button: *arcade.gui.UIFlatButton*
        Is the start button for the page.

    Methods
    -------
    on_show_view(self):
        When the window first opens, what to show.
    on_buttonclick(self, event):
        Allows page to change with button click.
    on_draw(self):
        Draws page when first created.

    """

    def on_show_view(self):
        """
        Put the window together when first shown.

        **Parameters**

            None

        **Returns**

            None

        """
        arcade.set_background_color((arcade.color.BLACK))
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

        start_button = arcade.gui.UIFlatButton(text="Start Game",
                                               width=200)

        start_button.on_click = self.on_buttonclick

        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                align_y=-200,
                child=start_button),
                )
        self.uimanager.add(
            arcade.gui.UIBorder(
                border_width=2,
                child=start_button)
                )

    def on_buttonclick(self, event):
        """
        Create the action when a button is clicked.

        **Parameters**

            event: *None*
                The event done by the buttonclicl

        **Returns**

            None

        """
        game_view = IntructionView()
        self.window.show_view(game_view)

    def on_draw(self):
        """
        Draw the window when first shown.

        **Parameters**

            None

        **Returns**

            None

        """
        self.clear()
        arcade.draw_text("WELCOME TO", self.window.width / 2, 450,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("ROBO RUNNER", self.window.width / 2, 350,
                         arcade.color.WHITE, font_size=70, anchor_x="center")
        self.uimanager.draw()
        arcade.draw_text("This game is designed", self.window.width / 2, 300,
                         arcade.color.WHITE, font_size=25, anchor_x="center")
        arcade.draw_text("to visualize robot", self.window.width / 2, 260,
                         arcade.color.WHITE, font_size=25, anchor_x="center")
        arcade.draw_text("actuation.", self.window.width / 2, 220,
                         arcade.color.WHITE, font_size=25, anchor_x="center")
        arcade.draw_text("EXIT TO QUIT", self.window.width / 2, 150,
                         arcade.color.WHITE, font_size=50, anchor_x="center")


class IntructionView(arcade.View):
    """
    A class to represent the instruction screen.

    Attributes
    ----------
    uimanager: *arcade.gui.UIManager*
        Manages the UI and GUI features for this program.
    continue_button: *arcade.gui.UIFlatButton*
        Is the continue button for the page.

    Methods
    -------
    on_show_view(self):
        When the window first opens, what to show.
    on_conttinue_buttonclick(self, event):
        Allows page to change with button click.
    on_draw(self):
        Draws page when first created.

    """

    def __init__(self):
        """
        Intiates the class.

        **Parameters**

            None

        **Returns**

            None

        """
        super().__init__()
        arcade.set_background_color((arcade.color.BLACK))

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

        # Creating Button using UIFlatButton
        continue_button = arcade.gui.UIFlatButton(text="CONTINUE",
                                                  width=300)

        # Assigning our on_buttonclick() function
        continue_button.on_click = self.on_continue_buttonclick

        # Adding button in our uimanager
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                align_y=-200,
                child=continue_button)
        )

    def on_continue_buttonclick(self, event):
        """
        Create the action of the button.

        **Parameters**

            event: *None*
                The event the buttonclick actions.

        **Returns**

            None

        """
        game_view = RoborunView()
        game_view.setup()
        self.window.show_view(game_view)

    def on_draw(self):
        """
        Draw the window when first shown.

        **Parameters**

            None

        **Returns**

            None

        """
        self.clear()
        arcade.draw_text("INSTRUCTIONS", self.window.width / 2, 450,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("You will provide the game with",
                         self.window.width / 2, 350,
                         arcade.color.WHITE, font_size=25, anchor_x="center")
        arcade.draw_text("the desired robot design.",
                         self.window.width / 2, 320,
                         arcade.color.WHITE, font_size=25, anchor_x="center")
        arcade.draw_text("ROBO RUNNER will show actuation through the",
                         self.window.width / 2, 290,
                         arcade.color.WHITE, font_size=25, anchor_x="center")
        arcade.draw_text("desired cycles in the next window.",
                         self.window.width / 2, 260,
                         arcade.color.WHITE, font_size=25, anchor_x="center")
        arcade.draw_text("Click 'Continue' to input and watch.",
                         self.window.width / 2, 200,
                         arcade.color.WHITE, font_size=25, anchor_x="center")
        self.uimanager.draw()


class RoborunView(arcade.View):
    """
    The game/visualization itself.

    Attributes
    ----------
    uimanager: *arcade.gui.UIManager*
        Manages the UI and GUI features for this program.
    continue_button: *arcade.gui.UIFlatButton*
        Is the continue button for the page.
    player_list: *list*
        List  of player locations.
    hotwater_list: *list*
        List of hotwater image locations.
    coldwater_list: *list*
        List of coldwater image locations.
    score: *int*
        Keeps the number of cycles.
    distance: *float*
        Keeps the distance traveled by bot.
    player_sprite *_main_.Player*
        The player itself.

    Methods
    -------
    __init__(self):
        Inititalizes the class.
    def setup(self):
        Sets up the page before use.
    on_draw(self):
        Draws page when first created.
    add_hotwater(self, delta_time: float):
        Pushes a hotwater cycle image through the screen.
    add_coledwater(self, delta_time: float):
        Pushes a coldwater cycle image through the screen.
    on_update(self, delta_time=1):
        Updates the system and sprites.
    """

    def __init__(self):
        """
        Intiates the class.

        **Parameters**

            None

        **Returns**

            None

        """
        super().__init__()
        self.player_list = None
        self.hotwater_list = None
        self.coldwater_list = None
        self.window.set_mouse_visible(False)
        self.score = -1
        self.distance = -1.96

    def setup(self):
        """
        Set the game up.

        **Parameters**

            None

        **Returns**

            None

        """
        self.player_list = arcade.SpriteList()
        self.hotwater_list = arcade.SpriteList()
        self.coldwater_list = arcade.SpriteList()

        arcade.schedule(self.add_coldwater, 7)
        arcade.schedule(self.add_hotwater, 7)

        self.player_sprite = self.player = Player()
        self.player.scale = 0.2
        self.player_sprite.center_x = 90
        self.player_sprite.center_y = self.window.height/2
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """
        Draw the window when first shown.

        **Parameters**

            None

        **Returns**

            None

        """
        self.clear()

        arcade.draw_lrtb_rectangle_filled(0, 800,
                                          (self.window.height / 2)+100,
                                          (self.window.height / 2)-100,
                                          (237, 251, 255))

        self.player_list.draw()
        self.hotwater_list.draw()
        self.coldwater_list.draw()
        if self.score >= 0:
            score_text = f"Full Cycles: {self.score}"
            arcade.draw_text(
                score_text,
                500,
                550,
                arcade.csscolor.WHITE,
                18,
            )
        if self.distance >= 0:
            distance_text = f"Distance Traveled: {self.distance} mm"
            arcade.draw_text(
                distance_text,
                500,
                520,
                arcade.csscolor.WHITE,
                18,
                )

    def add_hotwater(self, delta_time: float):
        """
        Move the hotwater image around the screen.

        **Parameters**

            delta_time: *float*
            Time between each movement.

        **Returns**

            None

        """
        hotwater = arcade.Sprite("ImagesforRoborunner/redline.png", 2)
        hotwater.left = 800
        hotwater.top = (self.window.height/2)-100
        hotwater.change_x = -5
        self.hotwater_list.append(hotwater)
        self.distance += 1.96

    def add_coldwater(self, delta_time: float):
        """
        Move the coldwater image around the screen.

        **Parameters**

            delta_time: *float*
            Time between each movement.

        **Returns**

            None

        """
        coldwater = arcade.Sprite("ImagesforRoborunner/blueline.png", 2)
        coldwater.left = 1575
        coldwater.top = (self.window.height/2)-100
        coldwater.change_x = -5
        self.coldwater_list.append(coldwater)
        self.score += 1
        self.distance += 1.96

    def on_update(self, delta_time=1):
        """
        Update the screen and sprites regularily.

        **Parameters**

            delta_time: *float*
            Time between each movement.

        **Returns**

            None

        """
        self.add_coldwater
        self.hotwater_list.update()
        self.player_list.update()
        self.coldwater_list.update()
        self.player_list.update_animation()


def main():
    """
    Is the main function.

    **Parameters**

        None

    **Returns**

        None

    """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = StartView()
    window.show_view(start_view)

    arcade.run()


if __name__ == "__main__":
    main()
