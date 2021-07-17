class PolygonSequence:
    """
    Given number of vertex for a Polygon, the PolygonSequence class will build all convex polygons upto that size.
    All sequence operations are possible with this class including - geting the the length, accessing by index, and slicing.
    Additionally the user can also use the method get_max_efficient_polygon to get the polygon with the max efficiency.
    """
    def __init__(self, n, r):
        self.n = n
        self.r = r
        
        self.seq = [Polygon(i, r) for i in range(3, n + 1)]
        
        
    def get_max_efficient_polygon(self):
        """
        efficiency of a polygon is defined as area:perimeter ratio.
        """
        argmax, ratio = max(
            [
                (n, (x.area / x.perimeter))
                for n, x in enumerate(self.seq)
            ], 
            key=lambda x: x[1]
        )
        print(f'Index of most efficient polygon - {argmax}\tarea:perimeter - {round(ratio, 4)}')
        return self.seq[argmax]
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0 or s > self.n:
                raise IndexError
            else:
                return self.seq[s]
        else:
            start, stop, step = s.indices(self.n)
            rng = range(start, stop, step)
            return [self.seq[i] for i in rng]
    
    def __repr__(self):
        return str([x for x in self.seq])
            
