#crypto
def cypherc(word):
    word=word.lower()
    newword = ""
    for i in word:
        d = i.isalpha()
        if d:
            a = ord(i)
            if a <120:
                b = a + 3
            else:
                b = a -23
            c = chr(b)
        else:
            c = i
        newword = newword + c
    print(newword)

def cypherd(word):
    word = word.lower()
    newword=""
    for i in word:
        d = i.isalpha()
        if d:
            a = ord(i)
            if a > 99:
                b = a - 3
            else:
                b = a + 23
            c = chr(b)
        else:
            c = i
        newword = newword + c
    print(newword)
cypherd("wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj")
print("")
print("...welcome..")
print("")
useri = input("encrypt/decrypt: ")
useri = useri.lower()

if useri == "encrypt":
    en = input("enter: ")
    cypherc(en)
elif useri == "decrypt":
    en = input("enter: ")
    cypherd(en)
else:
    print("can't you spell dummy .. dummy")

