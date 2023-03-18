letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    try:
        key = int(input("Enter Gap : "))
        str = list(i for i in input("Enter String : "))

        print("\n1. Encryption\n2. Decryption\n3. Exit")
        op = int(input("Enter Type : "))

        # Encryption Process
        if op == 1:
            print("Encrypted String : ", end="")
            for i in str:
                if i.isalpha():
                    if i.islower():
                        print(letters[(letters.index(i) + key) % 26], end="")
                    else:
                        print(letters[(letters.index(i.lower()) + key) % 26].upper(), end="")
                else:
                    print(i,end="")
            print("\n")

        # Decryption Process   
        elif op == 2:
            print("Decrypted String : ", end="")
            for i in str:
                if i.isalpha():
                    if i.islower():
                        print(letters[(letters.index(i) - key) % 26], end="")
                    else:
                        print(letters[(letters.index(i.lower()) - key) % 26].upper(), end="")
                else:
                    print(i,end="")
            print("\n")
            
        elif op == 3:
            exit(0)
            
        else:
            print("Invalid Option..\n")
            
    except:
        print("Invalid Input..\n")
