# # create a script that turns any string into morse code
#
# 1. ask for the string

string_to_convert = input("What would you like to convert?\n")
print(string_to_convert)
# 2. build a list or dictionary for the morse code items
#
morse_dictionary = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/', # Space between words is often represented by a slash in written form
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.'
}
# 3. chop the string into slices
#
# 4. spit out the morse code for each letter
morse_message = []
for char in string_to_convert.upper():
    # 5. add it to a list
    if char in morse_dictionary:
        morse_message.append(morse_dictionary[char])
    else:
        print(f"Character in '{char}' in not found in Morse Dictionary")

# 6. print the list
print(' '.join(morse_message))
