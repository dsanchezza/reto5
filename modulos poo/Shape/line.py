from Shape.point import Point

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.calculate_length()

    def calculate_length(self):
        self.length = self.start_point.compute_distance(self.end_point)
