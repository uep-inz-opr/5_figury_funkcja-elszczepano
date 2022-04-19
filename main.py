import math

i = int( input() )

figures = []

# Collect documents
for index in range(0, i):
    dimensions = input().split( " " )

    figures.append(map(int, dimensions))


def calculate():
    sum = 0;

    for figure in figures:
        if( len(figure) == 1 ):
            sum += circle( figure[ 0 ] )

            continue;
        if( len(figure) == 2 ):
            sum += rectangle( figure[ 0 ], figure[ 1 ] )
            
            continue;
        if( len(figure) == 3 ):
            sum += triangle( figure[ 0 ], figure[ 1 ], figure[ 2 ] )
            
            continue;
    print( "Błąd: można podać maksymalnie 3 liczby" )

    exit(0)

def rectangle(width, height):
    return width * height

def circle(radius):
    return math.pi * radius * radius

def triangle(a,b,c):
    s = (a+b+c)/2
    return math.sqrt(s(s-a)*(s-b)*(s-c))

calculate()