from turtle import Turtle



STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.right(270)
        self.penup()
        self.goto(position)
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor()> FINISH_LINE_Y:
            return True
        else:
            return False


