
def solution(n):
    numerals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman_num = ''
    while n > 0:
        for number, numeral in numerals:
            while n >= number:
                roman_num = roman_num + numeral
                n = n - number

    return roman_num
            


print (solution(4999))
