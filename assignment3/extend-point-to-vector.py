import math


class Point:
    """Represents a point in 2D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # equality: lets you do p1 == p2
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    # string representation: lets you do print(p1)
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Euclidean distance to another point
    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("distance_to expects another Point")

        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)


class Vector(Point):
    """A Vector is a Point, but prints differently and supports vector addition."""

    # override string representation
    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    # override + operator for vector addition
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector + Vector")

        return Vector(self.x + other.x, self.y + other.y)


# ---------------- DEMO / MAINLINE ----------------
if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)

    print("Points:")
    print("p1 =", p1)
    print("p2 =", p2)
    print("p1 == p2?", p1 == p2)
    print("distance from p1 to p2 =", p1.distance_to(p2))
    print()

    v1 = Vector(3, 5)
    v2 = Vector(2, -1)

    print("Vectors:")
    print("v1 =", v1)
    print("v2 =", v2)
    print("v1 + v2 =", v1 + v2)
    print("v1 == v2?", v1 == v2)
