from Shape.point import Point
from Shape.triangle import Triangle
from Shape.rectangle import Rectangle
from Shape.square import Square

punto1 = Point(0, 0)
punto2 = Point(3, 0)
punto3 = Point(0, 4)

triangulo = Triangle([punto1, punto2, punto3], is_regular=False)

print("Área del triángulo:", triangulo.compute_area())
print("Perímetro del triángulo:", triangulo.compute_perimeter())
print("Ángulos internos del triángulo:", triangulo.compute_inner_angles())

punto4 = Point(0, 0)
punto5 = Point(4, 0)
punto6 = Point(4, 2)
punto7 = Point(0, 2)

rectangulo = Rectangle([punto4, punto5, punto6, punto7], is_regular=False)

print("Rectángulo")
print("Área:", rectangulo.compute_area())
print("Perímetro:", rectangulo.compute_perimeter())
print("Ángulos internos:", rectangulo.compute_inner_angles())
print()

punto8 = Point(0, 0)
punto9 = Point(2, 0)
punto10 = Point(2, 2)
punto11 = Point(0, 2)

cuadrado = Square([punto8, punto9, punto10, punto11], is_regular=True)

print("Cuadrado")
print("Área:", cuadrado.compute_area())
print("Perímetro:", cuadrado.compute_perimeter())
print("Ángulos internos:", cuadrado.compute_inner_angles())
