# Script to correct errors for Lab 1.
# Convert from meters to feet and inches.
# The program should repeatedly input a length in meters
# and then print that length in feet and inches.

more = input('Do you wish to input another length in meters? ').upper( )
while more[0] == 'Y':
    
    meter = float(input('Enter length in meters: '))
    gets = ('Enter length in meters: ', meter)
    f = meter * 3.28084
    feet = int(f)
    inches = int(12.0 * (f - feet))
	
    print('The length is', end=' ')
    if feet == 1:
        print(str(feet) + ' foot', end=' ')
    else:
        print(str(feet) + ' feet', end= ' ')

	
    if inches == 1:
        print(str(inches) + ' inch.')
    elif (inches > 1):
        print(str(inches) + ' inches.')
    else:
        print( )
	
    more = input('Do you wish to input another length in meters: ').upper( )
