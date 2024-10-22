import itertools

totalWordsList = []
encryptedWords = []
decryptedWords = []


def encrypt(word):
    wordList = list(word)
    chars = "`1234567890-=qwertyuiop[]a sdfg hjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?"
    charList = list(chars)
    newword = ""
    for i in range(len(wordList)):
        for j in range(len(charList)):
            if wordList[i] == charList[j]:
                wordList[i] = charList[j-5]
                newword = newword + wordList[i]
                break
    totalWordsList.append(word + ": " + newword)
    encryptedWords.append(newword)
    return "You have encrypted " + "'" + word + "'" + ": " + newword

def decrypt(word):
    wordList = list(word)
    chars = "`1234567890-=qwertyuiop[]a sdfg hjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?"
    newword = ""
    for i in range(len(wordList)):
        for iter, j in enumerate(itertools.cycle(chars)):
            if wordList[i] == j:
                wordList[i] = chars[iter+5]
                newword = newword + wordList[i]
                break
    totalWordsList.append(word + ": " + newword)
    decryptedWords.append(newword)
    return "You have decrypted " + "'" + word + "'" + ": " + newword


def giveWordList():
    print("Total words list: ", end=" ")
    print(totalWordsList)

def encrypted():
    print("Encrypted words list: ", end=" ")
    print(encryptedWords)

def decrypted():
    print("Decrypted words list: ", end=" ")
    print(decryptedWords)

print("NOTE: This program will only encrypt and decrypt words that were previously encrypted/decrypted by it.")
while True:
    que = input("Do you want to encrypt or decrypt a word? ")
    while not (que.lower() == "encrypt" or que.lower() == "decrypt"):
        print("invalid input")
        que = input("Do you want to encrypt or decrypt a word? ")

    if que.lower() == "encrypt":
        enc = input("Enter a phrase or word to encrypt: ")
        print(encrypt(enc))
    if que.lower() == "decrypt":
        dec = input("Enter a phrase or word to decrypt: ")
        print(decrypt(dec))

    another = input("Would you like to encrypt or decrypt something else? 'yes' or 'no': ")
    if another == "no":
        break

ask = input("Would you like to see all the words you encrypted and decrypted? 'yes' or 'no' ")
while not (ask.lower() == "yes" or ask.lower() == "no"):
    print("invalid input")
    ask = input("Would you like to see all the words you encrypted and decrypted? 'yes' or 'no' ")

if ask.lower() == "yes":
    giveWordList()
    encrypted()
    decrypted()
if ask.lower() == "no":
    print("Thank you for using this tool")

