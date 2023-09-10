
class Dechiffrement:

    def Prolybe( word ):

        final = []
        tab_polybe = []

        x = 0
        for p in range(0,5):
            tab_polybe.append([ chr(x) for x in range(97,123) if( x != 106 ) ][x:x+5])
            x = x+5

        for letter in word.split(".") :

            for y in range(len(tab_polybe)):
                for x in range(len(tab_polybe[y])):
                
                    if letter == str(y+1)+str(x+1):
                        final.append( tab_polybe[y][x] )
        
        return final