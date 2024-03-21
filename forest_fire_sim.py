import random,sys, time, bext

width = 79
height = 22

tree = 'A'
fire = 'W'
empty = ''

initialtreedensity = 0.20
growchance = 0.01
firechance = 0.01

pauselength = 0.5

def main():
    global forest
    forest = createnewforest()
    bext.clear()

    while True:
        displayforest(forest)

        nextforest = {'width' : forest['width'],'height':forest['height']}
        for x in range(forest['width']):
            for y in range(forest['height']):
                continue
            if ((forest[(x,y)]==empty) and (random.random()<=growchance)):
                nextforest[x][y] = tree
            elif ((forest[(x,y)]==tree) and (random.random()<=firechance)):
                nextforest[x][y] = fire
            elif forest[(x,y)] == fire:
                for ix in range(-1,2):
                    for iy in range (-1,2):
                        if forest.get((x+ix,y+iy)) == tree:
                            nextforest[(x+ix,y+iy)] = fire
                nextforest[(x,y)] = empty

            else:
                nextforest[(x,y)] = forest[(x,y)]
        forest = nextforest
        time.sleep(pauselength)

def createnewforest():
    newforest ={'height' : height,'width':width}
    for x in range(width):
        for y in range(height):
            if (random.random()*100)<=initialtreedensity:
                newforest[(x,y)]=tree
            else:
                newforest[(x,y)]=empty
    return newforest

def displayforest(forest):
    bext.goto(0,0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x,y)] == tree:
                bext.fg('green')
                print(tree,end='')
            elif forest[(x,y)] == fire:
                bext.fg('red')
                print(fire,end='')
            elif forest[(x,y)] == empty:
                print(empty,end='')
        print()
    
    bext.fg('reset')
    print('grow chance{}%'.format(growchance*100),end='')
    print('lightening chance:{}%'.format(firechance*100),end='')
    

if __name__ == '__main__':
    main()