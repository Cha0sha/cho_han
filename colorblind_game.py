
import random,sys

try:
    import bext
except ImportError:
    print("THIs program requires the bext module,which you need to  install")
    sys.exit()

boardwidth = 16
boardheight = 14
movespergame = 20

heart = chr(9829)
diamond = chr(9830)
spade = chr(9824)
club = chr(9827)
ball = chr(9679)
triangle = chr(9650)
block = chr(9602)
leftright = chr(9472)
updown = chr(9474)
downright = chr(9484)
downleft = chr(9488)
upright = chr(9492)
upleft = chr(9496)

tiletypes = (0,1,2,3,4,5)
colormap = {0:'red',
              1 : 'green',
              2 : 'blue',
              3 : 'yellow',
              4 : 'cyan',
              5 : 'purple'}

colormode = 'colour mode'
shapesmap = {0 : heart,
             1 : triangle,
             2 : diamond,
             3 : ball,
             4 : club,
             5 : spade}

shapemode = 'shape mode'


def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print("Set the upper color/shape, which fills in all the adjustment squares of that same color/shape")
    print("Do you wanat to play in colorblind mode? Y/N")
    response = input(" >")
    if response.upper() == 'Y' or response.upper() ==  'YES':
        displaymode = shapemode
    else:
        displaymode = colormode

    gameboard = getnewboard()
    movesleft = movespergame
    while True:
        drawboard(gameboard,displaymode)
        print('Move Left : ',movesleft)
        playermove = askforplayermove(displaymode)
        changetile(playermove,gameboard,0,0)
        movesleft -=1

        if haswon(gameboard):
            displaymode(gameboard,displaymode)
            print('You have won')
            break
        elif movesleft == 0:
            displaymode(gameboard,displaymode)
            print('You have run out of moves')
            break

def getnewboard():
    board = {}
    for x in range(boardwidth):
        for y in range(boardheight):
            board[(x,y)] = random.choice(tiletypes)

    for i in range(boardwidth*boardheight):
        x = random.randint(0,boardwidth-2)
        y = random.randint(0,boardheight-1)
        board[(x+1,y)] = board[(x,y)]
    return board


def drawboard(board,displaymode):
    bext.fg('white')
    print(downright+(leftright*boardwidth)+downleft)

    for y in range(boardheight):
        bext.fg('white')
        if y==0:
            print('>',end='')
        else:
            print(updown,end='')
        
        for x in range(boardwidth):
            bext.fg(colormap[board[(x,y)]])
            if displaymode == colormode:
                print(block,end='')
            elif displaymode == shapemode:
                print(shapesmap[board[(x,y)]],end='')

        bext.fg('white')
        print(updown)
    print(upright+(leftright*boardwidth)+upleft)


def askforplayermove(displaymode):
    while True:
        bext.fg('white')
        print('choose one of ',end='')

        if displaymode == colormap:
            for color_key, color_value in colormap.items():
                bext.fg(color_value)
                print(f'({color_key}){color_value}', end='')

        elif displaymode == shapemode:
            for shape_key, shape_value in shapesmap.items():
                bext.fg(colormap[shape_key])
                print(f'({shape_key}){shape_value}', end='')
        bext.fg('white')
        print('or QUIT')
        response = input('> ')
        if response.upper() == 'QUIT':
            print("THanks visit again")
            sys.exit()
        if displaymode == colormode and response in tuple('RGBYCP'):
            return{'R' : 0,
                   'G' : 1,
                   'B' : 2,
                   'Y' : 3,
                   'C' : 4,
                   'P' : 6
                   }[response]
        if displaymode == shapemode and response in tuple('HTDBCS'):
            return{'H' : 0,
                   'T' : 1,
                   'D' : 2,
                   'B' : 3,
                   'C' : 4,
                   'S' : 5}[response]


def changetile(tiletype,board,x,y,chartochange = None):
    if x == 0 and y == 0:
        chartochange = board[(x,y)]
        if tiletype == chartochange:
            return
    
    board[(x,y)] = tiletype

    if x>0 and board[(x-1,y)] == chartochange:
        changetile(tiletype,board,(x-1),y,chartochange)
    if y > 0 and board[(x,y-1)] == chartochange:
        changetile(tiletype,board,(x),(y-1),chartochange)
    if x < boardwidth-1 and board[(x+1,y)] ==chartochange:
        changetile(tiletype,board,x+1,y,chartochange)
    if y < boardwidth-1 and board[(x+1,y)] ==chartochange:
        changetile(tiletype,board,x,y+1,chartochange) 


def haswon(board):
    tile = board[(0,0)]
    for x in range(boardwidth):
        for y in range(boardheight):
            if board[(x,y)] != tile:
                return False
        
    return True

if __name__ == '__main__':
    main()