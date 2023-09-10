from chiffrement import Chiffrement as CC

key = "magic"
word = "rdv au pommier"

final = []
for i in CC.Scytale( CC.Prolybe( word ), key )[1:]:
    for y in i:
        final.append(y)

crypt_word = ".".join(final)

crypt_key = "".join( CC.ROTN( CC.Scytale( CC.Prolybe( word ), key )[0] ) )

print("key -> ", crypt_key, "\nword -> ", crypt_word)