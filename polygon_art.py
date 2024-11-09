import turtle
import random


class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def move(self, new_location):
        self.location = new_location
        turtle.goto(self.location[0], self.location[1])
        turtle.penup()


def get_new_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


class PolygonArt:

    def __init__(self):
        self.num_levels = 3
        self.reduction_ratio = 0.618

    def run(self):
        choice = int(input('Which art do you want to generate? Enter a number between 1 to 9 inclusive: '))
        if choice == 1:
            for n in range(30):
                num_sides = 3
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = get_new_color()
                border_size = random.randint(1, 10)
                polygon = Polygon(num_sides, size, orientation, location, color,
                                  border_size)
                polygon.draw()
            turtle.done()
        elif choice == 2:
            for n in range(30):
                num_sides = 4
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = get_new_color()
                border_size = random.randint(1, 10)
                polygon = Polygon(num_sides, size, orientation, location, color,
                                  border_size)
                polygon.draw()
            turtle.done()
        elif choice == 3:
            for n in range(30):
                num_sides = 5
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = get_new_color()
                border_size = random.randint(1, 10)
                polygon = Polygon(num_sides, size, orientation, location, color,
                                  border_size)
                polygon.draw()
            turtle.done()
        elif choice == 4:
            for n in range(30):
                num_sides = random.randint(3, 5)
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = get_new_color()
                border_size = random.randint(1, 10)
                polygon = Polygon(num_sides, size, orientation, location, color,
                                  border_size)
                polygon.draw()
            turtle.done()
        elif choice == 5:
            for n in range(30):
                num_sides = 3
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = get_new_color()
                border_size = random.randint(1, 10)
                polygon = EmbeddedPolygon(num_sides, size, orientation, location, color,
                                          border_size, self.num_levels, self.reduction_ratio)
                polygon.draw()
            turtle.done()
        elif choice == 6:
            for n in range(30):
                num_sides = 4
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = get_new_color()
                border_size = random.randint(1, 10)
                polygon = EmbeddedPolygon(num_sides, size, orientation, location, color,
                                          border_size, self.num_levels, self.reduction_ratio)
                polygon.draw()
            turtle.done()
        elif choice == 7:
            for n in range(30):
                num_sides = 5
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = get_new_color()
                border_size = random.randint(1, 10)
                polygon = EmbeddedPolygon(num_sides, size, orientation, location, color,
                                          border_size, self.num_levels, self.reduction_ratio)
                polygon.draw()
            turtle.done()
        elif choice == 8:
            for n in range(30):
                num_sides = random.randint(3, 5)
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = get_new_color()
                border_size = random.randint(1, 10)
                polygon = EmbeddedPolygon(num_sides, size, orientation, location, color,
                                          border_size, self.num_levels, self.reduction_ratio)
                polygon.draw()
            turtle.done()
        elif choice == 9:
            for n in range(30):
                num_sides = random.randint(3, 5)
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = get_new_color()
                border_size = random.randint(1, 10)
                rand = random.randint(1, 2)
                if rand == 1:
                    polygon = Polygon(num_sides, size, orientation, location, color,
                                      border_size)
                    polygon.draw()
                elif rand == 2:
                    polygon = EmbeddedPolygon(num_sides, size, orientation, location, color,
                                              border_size, self.num_levels, self.reduction_ratio)
                    polygon.draw()
            turtle.done()


class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio):
        super().__init__(num_sides, size, orientation, location, color, border_size)
        self.num_levels = num_levels
        self.reduction_ratio = reduction_ratio

    def draw(self):
        while self.num_levels >= 2:
            super().draw()
            self.size *= self.reduction_ratio
            turtle.penup()
            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            super().draw()
            self.num_levels -= 1


pyrun = PolygonArt()
pyrun.run()