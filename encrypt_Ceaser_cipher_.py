def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  
            is_upper = char.isupper()
            
            char_code = ord(char) + shift
            if is_upper:
                if char_code > ord('Z'):
                    char_code -= 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
            
            encrypted_char = chr(char_code)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    
    return encrypted_message

message = input("Please enter the message that you want to encrypt : ")
shift_amount = 2
encrypted_message = encrypt(message, shift_amount)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")