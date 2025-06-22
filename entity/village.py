class Village():
    def __init__(self, coords, type, player, tribe, points, conquered):
        self.coords = coords
        self.type = type
        self.player = player
        self.tribe = tribe
        self.points = points
        self.conquered = conquered

    @property
    def x(self):
        return self.coords[0]
    
    @property
    def y(self):
        return self.coords[1]
    
    def derive_continent_name(self, x, y):
        return 'K'+str(y)[:1]+str(x)[:1]

    def derive_segment_coords(self, x, y):
        while x % 5 != 0:
            x -= 1
        while y % 5 != 0:
            y -= 1
        return x, y
    
    def derive_continent_coords(self, x, y):
        x = int(str(x)[:1]) * 100
        y = int(str(y)[:1]) * 100
        return x, y

    def __repr__(self):
        string = f"Village(coords={self.coords}, type='{self.type}'"
        if self.player:
            string += f", player='{self.player}'"
        if self.tribe:
            string += f", tribe='{self.tribe}'"
        string += f", points={self.points}"
        if self.conquered:
            string += f", conquered={self.conquered}"
        string += ")"
        return string