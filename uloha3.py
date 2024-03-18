def is_palindrome(num_str):
    return num_str == num_str[::-1]

def next_palindrome(from_num, radix, next_pal):
    if radix < 2 or radix > 36:
        return 0

    num = from_num + 1
    while True:
        num_str = ''
        temp = num

        while temp > 0:
            digit = temp % radix
            num_str += str(digit) if digit < 10 else chr(ord('A') + digit - 10)
            temp //= radix

        if is_palindrome(num_str):
            next_pal[0] = num
            return 1

        if num == float('inf'):
            return 0

        num += 1
from_num = 9
radix = 10
next_pal = [0]

result = next_palindrome(from_num, radix, next_pal)
if result:
    print("Nalezený palindrom v zadané soustavě:", next_pal[0])
else:
    print("Nebyl nalezen žádný palindrom v zadané soustavě.")