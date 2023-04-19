import math
import data


class Ball:
    def __init__(self, pos_x, pos_y, angle_with_positive_x_axis):
        # self.diameter = data.BALL_DIAMETER  # ignore this in first version
        self.x = pos_x
        self.y = pos_y
        self.angle = angle_with_positive_x_axis
        self.status = "stop"

    def move(self, step_distance):
        self.x += math.cos(math.radians(self.angle)) * step_distance
        self.y += math.sin(math.radians(self.angle)) * step_distance
        self.check_status()
        if self.status != "move":
            self.change_status()

    def check_status(self):
        if data.HOLE_DIAMETER / 2 < self.y < data.TABLE_Y - data.HOLE_DIAMETER / 2:
            if self.x <= 0:
                self.status = "left"
            elif self.x >= data.TABLE_X:
                self.status = "right"

            else:
                self.status = "move"
        elif data.HOLE_DIAMETER / 2 < self.x < data.TABLE_X / 2 - data.HOLE_DIAMETER / 2 or data.TABLE_X / 2 + data.HOLE_DIAMETER / 2 < self.x < data.TABLE_X - data.HOLE_DIAMETER / 2:
            if self.y >= data.TABLE_Y:
                self.status = "up"
            elif self.y <= 0:
                self.status = "down"
            else:
                self.status = "move"
        elif data.TABLE_X / 2 - data.HOLE_DIAMETER / 2 < self.x < data.TABLE_X / 2 + data.HOLE_DIAMETER / 2:
            if self.y >= data.TABLE_Y:
                self.status = "hole"
            elif self.y <= 0:
                self.status = "hole"
            else:
                self.status = "move"
        elif (self.y <= 0 and self.x <= 0) or (self.y >= data.TABLE_Y and self.x <= 0) or (
                self.y <= 0 and self.x >= data.TABLE_X) or (self.y >= data.TABLE_Y and self.x >= data.TABLE_X):
            self.status = "hole"
        elif self.x <= 0 or self.x >= data.TABLE_X or self.y <= 0 or self.y >= data.TABLE_Y:
            self.status = "hole"
        else:
            self.status = "move"

    def change_status(self):

        if self.status == "up" or self.status == "down":
            self.angle = 360 - self.angle

            self.status = "move"
            if self.angle < 0:
                self.angle += 360

        elif self.status == "left" or self.status == "right":
            self.angle = -self.angle + 180
            self.status = "move"
            if self.angle < 0:
                self.angle += 360

    def display(self):
        print("X:" + str(self.x), end="     ")
        print("Y:", str(self.y), end="     ")
        print("angle:", str(self.angle), end="     ")
        print("status:" + str(self.status), end="     ")
