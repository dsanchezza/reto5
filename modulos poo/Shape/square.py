from Shape.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, vertices, is_regular: bool):
        super().__init__(vertices, is_regular)
