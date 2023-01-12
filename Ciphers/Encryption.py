key = int(input("Enter key (Like 5: gap of the encrypted and original charachter) : "))
str = list(i for i in input())

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in str:
    if i.isalpha():
        if i.islower():
            print(letters[(letters.index(i) + key) % 26], end="")
        else:
            print(letters[(letters.index(i.lower()) + key) % 26].upper(), end="")
    else:
        print(i,end="")
