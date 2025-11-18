from itertools import count

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text,shift_amount):

    encryptedtext=""
    for c in original_text:
        count = 0
        for x in alphabet:#instead of looping again to get the index
            count += 1#we can use the alphabet.index(c) as mam did in the solution.py
            if alphabet[count - 1] == c:#check it out, it saves a lot of time for the compiler i guess
                if 0<=(count-1+shift_amount)<26:
                    encryptedtext += alphabet[count - 1 + shift_amount]
                elif (count-1+shift_amount)>=26:
                    countx=(count-1+shift_amount)-26
                    encryptedtext +=alphabet[countx]
    print(encryptedtext)
def decrypt(original_text,shift_amount):

    decryptedtext=""
    for c in original_text:
        count = 0
        for x in alphabet:
            count +=1
            if alphabet[count-1]==c:
                if -26<=(count-1-shift_amount)<26:
                    decryptedtext += alphabet[count - 1 - shift_amount]
                elif (count-1-shift_amount)<-26:
                    countx=(count-1-shift_amount)+26
                    decryptedtext +=alphabet[countx]
    print(decryptedtext)
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.


# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
opinion="yes"
while opinion=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    if direction == "decode":
        decrypt(text, shift)
    opinion=input('do you wish to continue?, "yes" or "no" : ')
