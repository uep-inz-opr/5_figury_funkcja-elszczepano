import math

i = int( input() )

figures = []

# Collect documents
for index in range(0, i):
    dimensions = input().split( " " )
    figures.append(dimensions)

def calculate():
    sum = 0;

    for figure in figures:
        figureDimensions = list(map(float, figure))
        
        if( len(figureDimensions) == 1 ):
            sum += circle( figureDimensions[ 0 ] )

            continue;
        if( len(figureDimensions) == 2 ):
            sum += rectangle( figureDimensions[ 0 ], figureDimensions[ 1 ] )
            
            continue;
        if( len(figureDimensions) == 3 ):
            sum += triangle( figureDimensions[ 0 ], figureDimensions[ 1 ], figureDimensions[ 2 ] )
            
            continue;
        print( "Błąd: można podać maksymalnie 3 liczby" )

        exit(0)

def rectangle(width, height):
    return width * height

def circle(radius):
    return math.pi * radius * radius

def triangle(a,b,c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

calculate()