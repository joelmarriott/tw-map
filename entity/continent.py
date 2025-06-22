from entity.segment import Segment

class Continent():
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords
        self.segments = self.generateSegments()

    @property
    def x(self):
        return self.coords[0]
    
    @property
    def y(self):
        return self.coords[1]
    
    def generateSegments(self):
        segments = []

        cur_x = self.x
        cur_y = self.y
        while cur_x < self.x + 100 and cur_y < self.y + 100:
            segments.append(Segment((cur_x, cur_y)))
            cur_x += 5
            if cur_x >= self.x + 100:
                cur_x = self.x
                cur_y += 5
            #
        #
        return segments
    
    def __repr__(self):
        return f"Continent(name='{self.name}', coords={self.coords}, "+\
            f"segments={self.segments})"
