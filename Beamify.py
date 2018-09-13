import random
import sys

colors = [ 'White', 'Brown', 'Red', 'Blue', 'Green', 'Yellow' ]

def run():
    if len( sys.argv ) != 2:
        print( 'Supports one argument: input filter file' )
        sys.exit( 0 )

    with open( sys.argv[ 1 ] ) as inFilter:
        with open( sys.argv[ 1 ] + '.out', 'w' ) as outFilter:
            for line in inFilter.readlines():
                if 'PlayEffect' not in line:
                    outFilter.write( line )
                    if line.startswith( 'Show #' ):
                        outFilter.write( '\tPlayEffect %s\n' % random.choice( colors ) )
                    elif line.startswith( 'Hide #' ):
                        outFilter.write( '\tPlayEffect %s Temp\n' % random.choice( colors ) )

if __name__ == '__main__':
    run()
