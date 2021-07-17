![Build Status](https://github.com/askmuhsin/convex_polygons/workflows/python_test/badge.svg)

# convex_polygons
a python polygon sequence

# Polygon module
module file -- [`./polygon.py`](https://github.com/askmuhsin/convex_polygons/blob/main/polygon.py)
To create a new Polygon - 
```python
from polygon import Polygon
p1 = Polygon(3, 12)
print(p1)
```
>
```bash
        Edges / Vertices (n) - 3
        Circumradius (R)     - 12
        
        Interior Angle       - 60.0
        Edge Length (s)      - 20.7846
        Apothem (a)          - 6.0
        Area                 - 187.0615
        Perimeter            - 62.3538
```

# PolygonSeqence module
module file -- [`./polygon_sequence.py`](https://github.com/askmuhsin/convex_polygons/blob/main/polygon_sequence.py)
```python
from polygon_sequence import PolygonSequence
ps = PolygonSequence(10, 10) 
print(ps)
```
The above will create a sequence of polygons starting from with the smallest possible edges of 3 to 10 (including 10), ie.. 8 polygons.
```bash
[Polygon(edges/vertices - 3, circumradius - 10), Polygon(edges/vertices - 4, circumradius - 10), Polygon(edges/vertices - 5, circumradius - 10), Polygon(edges/vertices - 6, circumradius - 10), Polygon(edges/vertices - 7, circumradius - 10), Polygon(edges/vertices - 8, circumradius - 10), Polygon(edges/vertices - 9, circumradius - 10), Polygon(edges/vertices - 10, circumradius - 10)]
```

# Tests
Tests for both modules -- [`./test.py`](https://github.com/askmuhsin/convex_polygons/blob/main/test.py)
