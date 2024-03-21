import shutil, sys

updownchar = chr(9474)
leftrightchar = chr(9472)
downrightchar = chr(9484)
downleftchar = chr(9488)
uprightchar = chr(9492)
upleftchar = chr(9496)
updownrightchar = chr(9500)
updownleftchar = chr(9508)
downleftrightchar = chr(9516)
upleftrightchar = chr(9524)
crosschar = chr(9532)

canvas_width, canvas_height = shutil.get_terminal_size()

canvas_width -=1
canvas_height -=5

canvas = {}
cursorX = 0
cursorY = 0

def getCanvasString(canvasdata,cs,cy):
    canvasStr = ''
    for rowNum in range(canvas_height):
        for columnNum in range(canvas_width):
            if columnNum == cs and rowNum == cy:
                canvasStr +='@'
                continue

            cell = canvasdata.get((columnNum,rowNum))
            if cell in (set(['W','S']),set(['W']),set(['S'])):
                canvasStr +=updownchar
            elif cell in (set(['A','D']),set(['A']),set(['D'])):
                canvasStr +=leftrightchar
            elif cell in set(['S','D']):
                canvasStr +=downrightchar
            elif cell in set(['A','S']):
                canvasStr +=downleftchar
            elif cell in set(['W','D']):
                canvasStr +=uprightchar
            elif cell in set(['W','A']):
                canvasStr +=upleftchar
            elif cell in set(['W','S','D']):
                canvasStr +=updownrightchar
            elif cell in set(['W','S','A']):
                canvasStr +=updownleftchar
            elif cell in set(['A','S','D']):
                canvasStr +=downleftrightchar
            elif cell in set(['W','A','D']):
                canvasStr +=upleftrightchar
            elif cell in set(['W','A','S','D']):
                canvasStr +=crosschar
        canvasStr +='\n'
    return canvasStr


moves = []

while True:
    print(getCanvasString(canvas,cursorX,cursorY))
    print("Enter W,A,S,D to move, C for clear, and F to save, or QUIT")
    response = input('> ').upper()

    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    elif response == 'H':
        print('Enter W,A,S and D to move the cursor and')
        print('draw a line going right and sssdddwwwaaa draws a box')
        print(" ")
        print('You can save your drawing to a text file by entering F.')
        input('Press ENter to return to the program')
        continue
    elif response =='C':
        canvas= {}
        moves.append('C')
    elif response == 'F':
        try:
            print('Enter the file name to save : ')
            filename = input('> ')

            if not filename.endwith('.txt'):
                filename+=".txt"
            with open(filename,'W',encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas,None,None))
        except:
            print('Error : could not save the file...')

    for command in response:
        if command not in ('W','A','S','D'):
            continue
        moves.append(command)

        if canvas =={}:
            if command in ('W','S'):
                canvas[(cursorX,cursorY)] = set(['W','S'])
            elif command in ('A','D'):
                canvas[(cursorX,cursorY)] = set(['A','D'])
        if command == 'W' and cursorY>0:
            cursorY -= 1
        elif command =='S' and cursorY< canvas_height -1:
            cursorY = cursorY + 1
        elif command == 'A' and cursorX > 0:
            canvas[(cursorX,cursorY)].add(command)
            cursorX = cursorX -1
        elif command == 'D' and cursorX < canvas_width-1:
            cursorX = cursorX + 1
        
        if (cursorX,cursorY) not in canvas:
            canvas[(cursorX,cursorY)] = set()

        if command == 'W':
            canvas[(cursorX,cursorY)].add('S')
        elif command == 'S':
            canvas[(cursorX,cursorY)].add('W')
        elif command == 'A':
            canvas[(cursorX,cursorY)].add('D')
        elif command == 'D':
            canvas[(cursorX,cursorY)].add('A') 