alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Hello welcome")

def ceaser(original_text, shift_amount, encode_or_decode):

    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter

        else:
            if encode_or_decode == 'encode':
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]

            elif encode_or_decode == 'decode':
                shifted_position = alphabet.index(letter) - shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]

    return cipher_text



should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt your message: ").lower()
    text = input("Enter your message: ").lower()
    shift = int(input("enter the shift number: "))

    result = ceaser(original_text = text, shift_amount = shift, encode_or_decode = direction)

    print(f"Your message is {direction}d as {result}")
    what = input("enter 'yes' to continue or 'no' to exit: ").lower()
    if what == 'no':
        should_continue = False
        print("GOOD BYE")
        break