class Segment():
    def __init__(self, coords):
        self.coords = coords
        self.villages = []
        
    @property
    def x(self):
        return self.coords[0]
    
    @property
    def y(self):
        return self.coords[1]
    
    def __repr__(self):
        string = f"Segment(coords={self.coords}"
        if self.villages:
            string += f", villages={self.villages}"
        string += ")"
        return string