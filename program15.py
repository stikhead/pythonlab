from abc import ABC, abstractmethod
import math

class GeometricEntity(ABC):
    """
    Abstract base class defining a mandatory blueprint for all geometric entities.
    """
    
    @abstractmethod
    def magnitude(self) -> float:
        """Calculates the primary magnitude/size metric of the entity."""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """String representation of the entity."""
        pass
    
    def __eq__(self, other) -> bool:
        if isinstance(other, GeometricEntity):
            return math.isclose(self.magnitude(), other.magnitude())
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, GeometricEntity):
            return self.magnitude() < other.magnitude()
        raise TypeError("Can only compare with other GeometricEntities.")


class Vector2D(GeometricEntity):
    """
    A 2D Vector class implementing the GeometricEntity abstract contracts 
    and overloading mathematical operators.
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def magnitude(self) -> float:
        """Returns the length of the vector."""
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        """Overloads the '+' operator for vector addition."""
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        raise TypeError("Can only add Vector2D to another Vector2D.")

    def __str__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"


class Circle(GeometricEntity):
    """
    A Circle class implementing the GeometricEntity abstract contracts 
    and overloading mathematical operators.
    """
    def __init__(self, radius: float):
        self.radius = radius

    def magnitude(self) -> float:
        """Returns the area of the circle as its magnitude."""
        return math.pi * (self.radius ** 2)

    def __add__(self, other):
        """
        Overloads the '+' operator to combine two circles.
        Creates a new circle whose area is the sum of the two areas.
        """
        if isinstance(other, Circle):
            new_radius = math.hypot(self.radius, other.radius)
            return Circle(new_radius)
        raise TypeError("Can only add Circle to another Circle.")

    def __str__(self) -> str:
        return f"Circle(Radius: {self.radius:.2f})"


if __name__ == "__main__":
    print("--- Abstract Shape Math Engine ---\n")
    v1 = Vector2D(3, 4)  # Magnitude: 5
    v2 = Vector2D(1, 1)  # Magnitude: ~1.414
    v3 = v1 + v2        

    print("Vector Operations:")
    print(f"v1: {v1} | Magnitude: {v1.magnitude():.2f}")
    print(f"v2: {v2} | Magnitude: {v2.magnitude():.2f}")
    print(f"v1 + v2 = {v3}")
    print(f"Is v1 > v2? {not (v1 < v2) and v1 != v2}")
    
    print("\n" + "-"*35 + "\n")

    c1 = Circle(3) # Area: ~28.27
    c2 = Circle(4) # Area: ~50.26
    c3 = c1 + c2   # Combined area -> Radius: 5

    print("Circle Operations:")
    print(f"c1: {c1} | Area (Magnitude): {c1.magnitude():.2f}")
    print(f"c2: {c2} | Area (Magnitude): {c2.magnitude():.2f}")
    print(f"c1 + c2 = {c3} | New Area: {c3.magnitude():.2f}")
    
    print("\n" + "-"*35 + "\n")

    print("Polymorphic Comparisons (Comparing Vector Magnitude vs Circle Area):")
    print(f"Is {v1} smaller than {c1}? {v1 < c1}")
    print(f"Are {Vector2D(0, 0)} and {Circle(0)} equal in magnitude? {Vector2D(0, 0) == Circle(0)}")