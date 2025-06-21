class Continent():
    def __init__(self, name, coords, segments):
        self.name = name
        self.coords = coords
        self.segments = segments

    @property
    def x(self):
        return self.coords[0]
    
    @property
    def y(self):
        return self.coords[1]
    
    def __repr__(self):
        return f"Continent(name='{self.name}', coords={self.coords}, "+\
            f"segments={self.segments})"
