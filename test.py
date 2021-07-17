from polygon import Polygon
from polygon_sequence import PolygonSequence

def test_polygon_methods():
    method_list = [x for x in dir(Polygon) if 'calc_' in x]
    exptected_methods = [
        'calc_apothem',
        'calc_area',
        'calc_edge_length',
        'calc_interior_angle',
        'calc_perimeter'
    ]
    assert all([x in method_list for x in exptected_methods]), "Did not find all methods"

    
def test_polygon_inputs():
    try:
        p1 = Polygon(0, 10)
    except AssertionError:
        pass
    
    p2 = Polygon(3, 10)
    p2.n == 3, "incorrect n"
    p2.r == 10, "incorrect r"

    
def test_polygon_porperties():
    p1 = Polygon(7, 10)
    expected_values = {
        'n': 7,
        'r': 10,
        'interior_angle': 128.57142857142858,
        'edge_length': 8.677674782351163,
        'apothem': 9.009688679024192,
        'area': 273.6410188638105,
        'perimeter': 60.74372347645814
    }
    assert p1.__dict__ == expected_values, "incorrect property values"

    
def test_polygon_equalities():
    p1 = Polygon(7, 10)
    p2 = Polygon(7, 10)
    p3 = Polygon(10, 5)
    
    assert p1==p2, "== equality incorrect."
    assert p1!=p3, "!= equality incorrect."
    assert p1<p3, "< equality incorrect."
    assert p3>p1, "> equality incorrect."
    assert p1>=p2, ">= equality incorrect."
    assert p2<=p3, "<= equality incorrect."
    

def test_polygon_sequence_inputs():
    ps1 = PolygonSequence(10, 10)
    assert len(ps1) == 8, "Incorrect __len__ implementation"
    
    ps2 = PolygonSequence(2, 10)
    assert len(ps2) == 0, "Incorrect __len__ implementation"

    
def test_polygon_sequence_methods():
    ps1 = PolygonSequence(2, 10)
    try:
        ps1 = PolygonSequence(2, 10)
        ps1.get_max_efficient_polygon()
    except AssertionError:
        pass
    
    ps2 = PolygonSequence(5, 10)
    p1 = ps2.get_max_efficient_polygon()
    assert isinstance(p1, Polygon), "Unexpected type of Polygon."
    assert p1.n==5, "Incorrect polygon eff calculation, expecting polygon with max edges"
    

def test_polygon_sequence_indexing():
    ps1 = PolygonSequence(10, 10)
    
    p = ps1[0]
    assert p.n==3, "incorrect index returned"
    
    p = ps1[-1]
    assert p.n==10, "incorrect index returned"
    
    assert len(ps1[2:7:2])==3, "incorrect slicing executed"
