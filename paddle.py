from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def goUp(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def goDown(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
