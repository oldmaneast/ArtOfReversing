def tor(number):
    if number < 0 or number > 3999:
        return ""
    if number < 1:
        return ""
    if number >= 1000:
        return "M" + tor(number - 1000)
    if number >= 900:
        return "CM" + tor(number - 900)
    if number >= 500:
        return "D" + tor(number - 500)
    if number >= 400:
        return "CD" + tor(number - 400)
    if number >= 100:
        return "C" + tor(number - 100)
    if number >= 90:
        return "XC" + tor(number - 90)
    if number >= 50:
        return "L" + tor(number - 50)
    if number >= 40:
        return "XL" + tor(number - 40)
    if number >= 10:
        return "X" + tor(number - 10)
    if number >= 9:
        return "IX" + tor(number - 9)
    if number >= 5:
        return "V" + tor(number - 5)
    if number >= 4:
        return "IV" + tor(number - 4)
    if number >= 1:
        return "I" + tor(number - 1)
    return ""

def dor(s):
    return ''.join([chr(ord(char) + 1) for char in s[::-1]]).lower()

num = 16

while True:

    roman_numeral = tor(num)
    reversed_string = dor(roman_numeral)
    if reversed_string == 'wymddd':
        break
    num = num + 1

print(f'Your number is {num}')

