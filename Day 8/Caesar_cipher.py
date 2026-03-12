

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]


direction = input("Type 'encode' or 'decode' to encrypt or decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n "))

temp = []

def encrypt(original_text, shift_amount, encry):
    chiper_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet)
        chiper_text += alphabet[shifted_position]


    print(chiper_text)


encrypt(text, shift)