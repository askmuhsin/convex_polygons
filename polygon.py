import math

class Polygon:
    """
    A strictly convex polygon class, ie.. all interior angles < 180 and all sides are equal.
    Arguments:
        n: int, the number of edges or vertices for the polygon.
        r: int, the circumradius of the polygon.
    """
    def __init__(self, n, r):
        assert n >= 3, "a polygon needs to have minimum of 3 edges"
        assert isinstance(n, int), "number of edges/vertices need to be a whole number > 3"
        
        self.n = n # no of edges / vertices
        self.r = r # circumradius
        
        self.interior_angle = self.calc_interior_angle()
        self.edge_length = self.calc_edge_length()
        self.apothem = self.calc_apothem()
        self.area = self.calc_area()
        self.perimeter = self.calc_perimeter()
    
    def calc_interior_angle(self):
        return (self.n - 2) * (180 / self.n)

    def calc_edge_length(self):
        return 2 * self.r * math.sin(math.pi / self.n)

    def calc_apothem(self):
        return self.r * math.cos(math.pi / self.n)

    def calc_area(self):
        return 0.5 * self.n * self.edge_length * self.apothem

    def calc_perimeter(self):
        return self.n * self.edge_length
    
    def __str__(self):
        summary = f"""
        Edges / Vertices (n) - {self.n}
        Circumradius (R)     - {self.r}
        
        Interior Angle       - {self.interior_angle}
        Edge Length (s)      - {self.edge_length}
        Apothem (a)          - {self.apothem}
        Area                 - {self.area}
        Perimeter            - {self.perimeter}
        """
        return summary
    
    def __repr__(self):
        return f"Polygon(edges/vertices - {self.n}, circumradius - {self.r})"
    
    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self.n == other.n and self.r == other.r
        else:
            print("Is not an instance of class Polygon !")
            return False
        
    def __ne__(self, other):
        return not self == other
    
    def __ge__(self,other):
        return self.n >= other.n
    
    def __gt__(self,other):
        return self.n > other.n
    
    def __le__(self,other):
        return self.n <= other.n
    
    def __lt__(self,other):
        return self.n < other.n
