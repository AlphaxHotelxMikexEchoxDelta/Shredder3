
class Chiffrement:

    # la cle comme pour le mot ne doit contenir QUE des lettres, et eviter les espacements ;)
    # Prolybe prend pas en compte les chiffres...
    def Prolybe( word ):

        final = []
        tab_polybe = []

        x = 0
        for p in range(0,5):
            tab_polybe.append([ chr(x) for x in range(97,123) if( x != 106 ) ][x:x+5])
            x = x+5

        for letter in word.lower():
            
            for y in range(len(tab_polybe)):
                for x in range(len(tab_polybe[y])):

                    if letter == tab_polybe[y][x]:
                        final.append( str(y+1)+str(x+1) )
                
            if letter == "j":
                final.append("24")
                        
        return final

    def pos_to_pos(tabu,tabx,x):
        for u in range(0,len(tabx[0])):
            if tabu[0][u] == tabx[0][x] :
                    return u

    # Attention ! la key ne doit pas contenir deux fois la meme lettre     
    def Scytale( word, key ):
        
        final = []
        tab_scytale = []
        tab_scytale.append( list(key) )
        
        while word:
            tab_scytale.append( word[:len(key)] )
            for o in word[:len(key)]:
                word.remove(o)

        from random import randint
        if len(tab_scytale[-1]) != len(key):
            for i in range( len(key) - len(tab_scytale[-1]) ):
                tab_scytale[-1].append(str(randint(11,55)))

        # l'erreur viens d'ici
        final.append( sorted(tab_scytale[0]) )
        # et là
        for f in range(1,len(tab_scytale)):
            final.append([])
            for t in range(0,len(key)):
                final[f].append(t)
                
        for i in range(1,len(final)):
            for y in range(0,len(final[i])):
                final[i][Chiffrement.pos_to_pos(final,tab_scytale,y)] = tab_scytale[i][y]

        return final
    
    def ROTN( key ):

        final = []
        from random import randint
        n = randint(1,25)

        alphabet = [ chr(i) for i in range(97,123) ]
        rotn = [ i for i in [ chr(i) for i in range(97,123) ][n:] ]
        for i in [ chr(i) for i in range(97,123) ][:n]:
            rotn.append(i)

        for y in range(0,26):
            for i in range(0,len(key)):
                
                if key[i] == alphabet[y]:
                    final.append(rotn[y])

        return final