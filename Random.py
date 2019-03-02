import math
shape = str(input('Please insert shape: '))
if shape == 'triangle':
    fstSide = float(input('Give me first side /w natural number: '))
    while fstSide < 0:
        fstSide = float(input('Again. Give me first side /w natural number: '))
    sndSide = float(input('Give me second side /w natural number: '))
    while sndSide < 0:
        sndSide = float(input('Again. Give me second side /w natural number: '))
    trdSide = float(input('Give me third side: '))
    while trdSide < 0:
        trdSide = float(input('Again. Give me third side /w natural number: '))
    print('Your triangle have the first side of',
          fstSide, 'cm, second of', sndSide, 'cm and third of', trdSide, 'cm')
    perimeter = fstSide+sndSide+trdSide
    p = perimeter/2
    area = math.sqrt(p*(p-fstSide)*(p-sndSide)*(p-trdSide))
    print('Triangle perimeter is', perimeter, 'cm')
    print('Triangle area is', area, 'cm^2')
elif shape == 'square':
    side = float(input('Give me side /w natural number: '))
    while side < 0:
        side = float(input('Again. Give me side /w natural number: '))
    print('Your square side is', side, 'cm')
    perimeter = side*4
    area = side*side
    print('Square perimeter is ', perimeter, 'cm')
    print('Square area is ', area, 'cm^2')
elif shape == 'rectangle':
    fstSide = float(input('Give me first side: '))
    while fstSide < 0:
        fstSide = float(input('Give me first side /w natural number: '))
    sndSide = float(input('Give me second side: '))
    while sndSide < 0:
        sndSide = float(input('Give me second side /w natural number: '))
    perimeter = fstSide*2+sndSide*2
    area = fstSide*sndSide
    print('Rectangle perimeter is', perimeter, 'cm')
    print('Rectangle area is', area, 'cm^2')
else:
    print('I dont know that shape you are talking about')
