from PIL import Image

def new_map(villages, map_type='SCORE', scale=1, continent=None,
         tribes=None, players=None, conquers=False):
    # Meat of map generation here
    print(deriveContinentName(305, 405))       # Test - ends up as K43
    print(deriveSegmentCoords(307, 407))       # Test - ends up as (305, 405)
    genImage():                                # Just a funky image gen test

def deriveContinentName(x, y):
    return 'K'+str(y)[:1]+str(x)[:1]

def deriveSegmentCoords(x, y):
    while x % 5 != 0:
        x -= 1
    while y % 5 != 0:
        y -= 1
    return x, y

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