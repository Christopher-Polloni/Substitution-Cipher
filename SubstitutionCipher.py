import string

plaintext = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypted = ['W', 'D', 'Z', 'E', 'H', 'I', 'U', 'A', 'G', 'R', 'X', 'F', 'Q', 'C', 'V', 'M', 'J', 'N', 'B', 'Y', 'L', 'S', 'K', 'T', 'P', 'O']
frequencyEnglish = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'w', 'm', 'f', 'c', 'g', 'y', 'p', 'b','k', 'v', 'j', 'x', 'q', 'z']

print("Initializing Program...")
infile = open('word count file.txt', 'r')
words = {} # start with empty dict
for line in infile.readlines():
    word, number = line.split()
    words[word] = int(number)
# print (words)
wordlist = list(words.keys())
wordcountlist = list(words.values())


letterCount = {}
for c in string.ascii_lowercase:
    letterCount[c]=0

for word in wordlist:
    count = wordlist.index(word)
    for letter in word:
        letterCount[letter] = letterCount[letter]+wordcountlist[count]

num = []
num = list(letterCount.values())

cipherLetterCount = {}
for i in range(26):
    x = encrypted[i]
    y = num[i]
    cipherLetterCount[x] = y

letterssortedplaintext = []
letterssortedplaintext = sorted(letterCount, key=letterCount.get, reverse=True)
letterssortedencrypted = []
letterssortedencrypted = sorted(cipherLetterCount, key=cipherLetterCount.get, reverse=True)

total = 0
letters = []
letters = list(cipherLetterCount.keys())
numbers = []
numbers = list(cipherLetterCount.values())
percentage = []
for i in range(26):
    total = total + numbers[i]

for i in range(26):
    a = numbers[i]
    b = a/total
    percentage.append(b)

percentagesorted = sorted(percentage, reverse=True)

def print_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("MENU")
    print ("1. View Key")
    print ("2. Encrypt Plaintext")
    print ("3. Decrypt Ciphertext")
    print ("4. Cipher Text Letter Frequency Table")
    print ("5. View Key Generated by Passive Attacker")
    print ("6. Simulate Attack After Letter Frequency Analysis")
    print ("7. Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def encryption():
    quit = 0
    encryptThis = input("Enter your word to encrypt: ")
    cipherText = []
    for c in encryptThis:
        if c in plaintext:
            x = plaintext.index(c)
            y = (encrypted[x])
            cipherText.append(y)
        else:
            quit = 1

    if quit == 1:
        print("All values entered must be lower-case English characters!")
    else:
        print("Your message has been encrypted to the following ciphertext: ")
        print(*cipherText, sep = "")

def decryption():
    quit = 0
    decryptThis = input("Enter your cipher text to decrypt: ")
    plainText = []
    for c in decryptThis:
        if c in encrypted:
            x = encrypted.index(c)
            y = (plaintext[x])
            plainText.append(y)
        else:
            quit = 1

    if quit == 1:
        print("All values entered must be part of the key! (upper-case English characters)")
    else:
        print("Your message has been decrypted to the following plaintext: ")
        print(*plainText, sep = "")

def passiveAttacker():
    quit = 0
    encryptThis = input("Enter your word to encrypt: ")
    print("Alice sends the message: \n" + encryptThis)
    cipherText = []
    for c in encryptThis:
        if c in plaintext:
            x = plaintext.index(c)
            y = (encrypted[x])
            cipherText.append(y)
        else:
            quit = 1

    if quit == 1:
        print("All values entered must be lower-case English characters!")
    else:
        print("Alice's message has been encrypted to the following ciphertext: ")
        print(*cipherText, sep = "")

    plainText = []
    for c in cipherText:
        x = letterssortedencrypted.index(c)
        y = (frequencyEnglish[x])
        plainText.append(y)
    print("Eve only sees the ciphertext. After performing letter frequency analysis on a large body of text, Eve decrypts the message to the following plaintext: ")
    print(*plainText, sep = "")

def cipherTextLetterFrequency():
    print("Ciphertext Letter Frequency")
    for i in range(26):
        print(letters[i]+"\t"+str(round(percentagesorted[i],4)))

def showKey1():
    print ("The key is:")
    print ("Plaintext: " + str(plaintext))
    print ("Encrypted: " + str(encrypted))

def showKey2():
    print("Key generated from letter frequency analysis:")
    print("Encrypted: " + str(letterssortedencrypted))
    print("Plaintext: " + str(frequencyEnglish))

loop=True
while loop:
    print_menu()
    choice=input("Enter your choice: ")

    if choice=='1':
        print ("Option 1 has been selected")
        showKey1()
    elif choice=='2':
        print ("Option 2 has been selected")
        encryption()
    elif choice=='3':
        print ("Option 3 has been selected")
        decryption()
    elif choice=='4':
        print ("Option 4 has been selected")
        cipherTextLetterFrequency()
    elif choice=='5':
        print ("Option 5 has been selected")
        showKey2()
    elif choice=='6':
        print ("Option 6 has been selected")
        passiveAttacker()
    elif choice=='7':
        print ("Option 7 has been selected \nEnding Program")
        loop=False
    else:
        print ("Please use a value of 1-7")
