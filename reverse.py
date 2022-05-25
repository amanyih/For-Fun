def reverse(a):
    word = a
    newword = ""
    for i in range(len(word)-1, -1,-1):
        newword = newword + word[i]
    print(newword)

reverse(input("enter a word: "))