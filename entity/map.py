from entity.continent import Continent

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
        self.map_start = (999, 999)

    def map_villages(self, villages):
        for village in villages:
            k_name = village.derive_continent_name(village.x, village.y)
            v_continent = self.get_continent(k_name)
            if not v_continent:
                k_coords = village.derive_continent_coords(village.x, village.y)
                self.continents.append(Continent(k_name, k_coords))
                v_continent = self.get_continent(k_name)
                if k_coords[0] < self.map_start[0]:
                    self.map_start = (k_coords[0], self.map_start[1])
                #
                if k_coords[1] < self.map_start[1]:
                    self.map_start = (self.map_start[0], k_coords[1])
                #
            #
            s_coords = village.derive_segment_coords(village.x, village.y)
            for segment in v_continent.segments:
                if s_coords == segment.coords:
                    segment.villages.append(village)
                #
            #
        #

    def get_continent(self, k_name):
        v_continent = None
        for continent in self.continents:
            if continent.name == k_name:
                v_continent = continent
            #
        #
        return v_continent

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