from Shape.line import Line

class Shape:
    def __init__(self, vertices, is_regular: bool):
        self.vertices = vertices
        self.edges = []
        self.inner_angles = []
        self.is_regular = is_regular
        self.make_edges()

    def make_edges(self):
        for i in range(len(self.vertices) - 1):
            punto_inicio = self.vertices[i]
            punto_final = self.vertices[i + 1]
            lado = Line(punto_inicio, punto_final)
            self.edges.append(lado)

        punto_final = self.vertices[-1]
        punto_inicial = self.vertices[0]
        lado_final = Line(punto_final, punto_inicial)
        self.edges.append(lado_final)

    def compute_area(self):
        raise NotImplementedError

    def compute_perimeter(self):
        raise NotImplementedError

    def compute_inner_angles(self):
        raise NotImplementedError
