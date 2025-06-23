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

def generate_map(map):
    continents_x = int(len(map.continents) / 2)
    width = continents_x * 100 * 2 * map.scale
    
    k_border_width = 2
    k_border_colour = (0, 0, 0)
    
    s_border_width = 1
    s_border_colour = (72, 72, 72)
    
    width += k_border_width * continents_x
    width += s_border_width * continents_x * 20
    
    height = width
    
    v_width = v_height = 2 * map.scale
    
    img = Image.new('RGB', (width, height), (80, 80, 80))
    data = img.load()

    k_names = []
    for continent in map.continents:
        k_names.append(continent.name)
    
    k_names = sorted(k_names)
    print(k_names)
    
    print(width)
    
    k_border_total = 0
    s_border_total = 0
    
    for k_name in k_names:
        continent = None
        for m_continent in map.continents:
            if k_name == m_continent.name:
                continent = m_continent
            #
        if not continent:
            print('Cannot find continent')
            
        x_start = (continent.coords[0] - map.map_start[0]) * 2 * map.scale + k_border_total
        x_end = ((continent.coords[0] - map.map_start[0]) + 99 * 2 * map.scale) + k_border_width + k_border_total
        
        y_start = (continent.coords[1] - map.map_start[1]) * 2 * map.scale
        y_end = ((continent.coords[1] - map.map_start[1]) + 99 * 2 * map.scale) + k_border_width

        k_border_total += k_border_width

        for x in range(x_start, x_end):
            print(y_end)
            data[x, y_end - 1] = k_border_colour
            data[x, y_end] = k_border_colour
        #
        for y in range(y_start, y_end):
            data[x_end -1, y] = k_border_colour
            data[x_end, y] = k_border_colour
        #
    #
        
    img.save('image.png')

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