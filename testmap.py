from random import randint
from entity.village import Village
from main import new_map

def main():
    test_villages = generateTestVillages()
    while 1:
        map_type = input('Map type? (SCORE, ODA, ODD, ODS): ').upper()
        if not map_type:
            map_type = 'SCORE'
        if map_type in ['SCORE', 'ODA', 'ODD', 'ODS']:
            break
        print('Invalid map type')
    while 1:
        scale = input('Scale? 1-9: ')
        if not scale:
            scale = 1
        scale = int(scale)
        if scale >= 1 and scale <= 9:
            break
        print('Scale must be between 1 and 9')
    while 1:
        continent = input('Continent or blank for all: ')
        if not continent:
            break
        try:
            if continent[:1] != 'K':
                continent = 'K'+continent
            if int(continent[1:2]) >= 2 and int(continent[1:2]) <= 7:
                if int(continent[2:]) >=2 and int(continent[2:]) <= 7:
                    break
        except Exception:
            pass
        print('Invalid continent')
    tribes = input('Tribes (comma seperated or blank): ')
    players = input('Players (comma seperated or blank): ')
    while 1:
        conquers = input('Show conquers, Y/N: ').upper()
        if not conquers or conquers[:1] in 'Y'/'N':
            break
        print('Invalid option')
    new_map(test_villages, map_type, scale, continent, tribes, players, conquers)

def generateTestCoords():
    coords = []
    generated_villages = 0
    while generated_villages < 2500:
        generated_coords = (randint(430, 570), randint(430, 570))
        print('Fake coords = '+str(generated_coords))
        if generated_coords not in coords:
            coords.append(generated_coords)
        generated_villages += 1
    return coords

def generateTestVillages():
    test_villages = []
    test_coords = generateTestCoords()
    for coords in test_coords:
        if coords[0] % 2 == 0 or coords[1] % 2 == 0:
            player_name = 'player'+str(randint(0,50))
            tribe_name = 'tribe'+str(randint(0,20))
            village_type = 'Player'
            points = randint(26,10000)
        else:
            player_name = None
            tribe_name = None
            village_type = 'Barbarian'
            points = randint(26,3500)
        test_village = Village(coords, village_type, player_name,
                               tribe_name, points, None)
        print('Generated '+str(test_village))
        test_villages.append(test_village)
    return test_villages

if __name__ == '__main__':
    main()