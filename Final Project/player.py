"Generated by ChatGPT, edited by Nic Ekstrand"
class Player:
    def __init__(self, size, x, y, x_speed, y_speed):
        self.size = size

        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    # Getter methods
    def get_size(self):
        return self.size

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_y_speed(self):
        return self.y_speed
    
    def move_x(self):
        self.x += self.x_speed
    
    def move_y(self):
        self.y += self.y_speed

    def set_y_speed(self, x):
        self.y_speed = x

    def set_x_speed(self, x):
        self.x_speed = x

    def set_x(self, x):
        self.x = x

    def set_y(self, x):
        self.y = x

    def increase_y(self, x):
        self.y += x

    def increase_y_speed(self, x):
        self.y_speed += x

    def __str__(self):
        return f"Player - Position: ({self.x}, {self.y}), Velocity: ({self.x_speed}, {self.y_speed}), Size: {self.size}"