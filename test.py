from chiffrement import Chiffrement as CC

key = "magic"
word = "rdv au pommier"

#z = CC.Scytale( CC.Prolybe( word ), key )[1:]
    
x = "".join( CC.ROTN( CC.Scytale( CC.Prolybe( word ), key )[0] ) )

final = []
for i in CC.Scytale( CC.Prolybe( word ), key )[1:]:
    for y in i:
        final.append(y)

print(".".join(final))