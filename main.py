from PIL import Image
from entity.map import Map
import json
import jsonpickle

def new_map(villages, map_type='SCORE', scale=1, continent=None,
         tribes=None, players=None, conquers=False):
    map = Map([], map_type, scale, continent, tribes, players, conquers)
    map.map_villages(villages)
    json_string = jsonpickle.encode(map)
    json_obj = json.loads(json_string)
    with open('dump.json', 'w') as f:
        f.write(json.dumps(json_obj, indent=2))
    #
    generate_map(map)
    # Meat of map generation here
    #genImage():                                # Just a funky image gen test

def genImage():
    img = Image.new('RGB', [500,500], 255)
    data = img.load()


    for x in range(img.size[0]):
        for y in range(img.size[1]):
            data[x,y] = (
                x % 255,
                y % 255,
                (x**2-y**2) % 255,
            )

    img.save('image.png')

if __name__ == '__main__':
    print('Must be called from another program')