def cipher(text, shift, operation):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result
def main ():
    while True:
        print("1 .Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice =input("choose one please:")
        if choice =='3':
            break
        if choice in ['1','2']:
            message =input("Give me please your message :")
            shift =int(input("Give me the shift value"))
            if choice =='1':
                encrypted_message=cipher(message,shift,'encrypt')
                print("your encrypted message is",encrypted_message)
            elif choice =='2':
                decrypted_message = cipher(message,shift,"decrypt")
                print("your encrypted message is",decrypted_message)
        else:
            print("invalid choice")
if __name__=="__main__":
    main()
    

        
