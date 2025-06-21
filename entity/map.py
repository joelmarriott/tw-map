class Map:
    def __init__(self, continents, type='SCORE', scale=1, continent=None,
                 tribes=None, players=None, conquers=False):
        self.continents = continents
        self.type = type
        self.scale = scale
        self.continent = continent
        self.tribes = tribes
        self.players = players
        self.conquers = conquers

    def __repr__(self):
        string = f"Map(continents='{self.continents}, type={self.type}, "+\
            f"scale={self.scale}"
        if self.continent:
            string += f", continent={self.continent}"
        if self.tribes:
            string += f", tribes={self.tribes}"
        if self.players:
            string += f", players={self.players}"
        if self.conquers:
            string += f", conquers=True"
        string += ")"
        return string