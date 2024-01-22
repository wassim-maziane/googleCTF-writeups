#!/usr/bin/python3
import string
enc = "Naljnl, Pnrfne jnf n fxvyyrq pbzzhavpngbe, naq ur hfrq n inevrgl bs zrgubqf gb xrrc uvf zrffntrf frperg sebz uvf rarzvrf. Bar bs gurfr zrgubqf jnf gur Pnrfne pvcure, n fvzcyr grpuavdhr gb boshfpngr pbzzhavpngvbaf. SYNT{ebgngr_gung_nycunorg}"
dec = ""
alphabet = list(string.ascii_lowercase)
offset = (alphabet.index('s') - alphabet.index('f')) % 26
for character in enc:
    if character.lower() in alphabet:
        charIndex = alphabet.index(character.lower())
        dec += alphabet[(charIndex - offset) % 26] 
    else:
        dec += character
print(dec)
