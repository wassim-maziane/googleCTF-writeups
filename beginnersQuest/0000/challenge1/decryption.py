#!/usr/bin/python3
import string
enc ="Vhi Nixgnije tkplwr zu a tglpcltzasgtmu sldsxatlvisf czrhij. Ik ks e eoig sshhzutmuakgd zwrjkor gf kje Gsejcr gapygr, azitj uwws r uirylv uhmxt mclyw tf gngjygv tlw eevivw mvuseye. WNAK{yek_xikyy_nktl_at}"
dec = ""
alphabet = list(string.ascii_lowercase)
key = "caesar"
i = 0
for character in enc:
    if character.lower() in alphabet:
        offset = alphabet.index(key[i])
        i = (i + 1) % len(key)
        charIndex = alphabet.index(character.lower())
        dec += alphabet[(charIndex - offset) % 26] 
    else:
        dec += character
print(dec)
