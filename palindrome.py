word = input("word: ")
rev = ""
for i in range(len(word)-1,-1,-1):
    rev = rev + word[i]
def palindrome(word):
    rev = ""
    for i in range (len(word)-1,-1,-1):
        rev = rev + word[i]
    if word == rev:
        print("ya")
    else:
        print("nah")
palindrome(word)