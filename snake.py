from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SNAKE_COLOR = "brown"


class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.shapesize(1, 1, 0)
            new_segment.penup()
            new_segment.color(SNAKE_COLOR)
            new_segment.goto(position)
            self.segments.append(new_segment)

    def snake_grows(self):
        head = self.segments[0]
        added_segment = Turtle("square")
        added_segment.shapesize(1, 1, 0)
        added_segment.penup()
        added_segment.color(SNAKE_COLOR)
        added_segment.goto(self.segments[- 1].position())
        self.segments.append(added_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].position())
        self.segments[0].fd(MOVE_DISTANCE)

    def turn_right(self):
        head = self.segments[0]
        if head.heading() != float(180):
            head.setheading(0)

    def turn_left(self):
        head = self.segments[0]
        if head.heading() != float(0):
            head.setheading(180)

    def turn_up(self):
        head = self.segments[0]
        if head.heading() != float(270):
            head.setheading(90)

    def turn_back(self):
        head = self.segments[0]
        if head.heading() != float(90):
            head.setheading(270)

