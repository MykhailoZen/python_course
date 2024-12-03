# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
#  Symbol       Value
#  I             1
#  V             5
#  X             10
#  L             50
#  C             100
#  D             500
#  M             1000
#  For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is
#  simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
#  Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
#  Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
#  principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#  I can be placed before V (5) and X (10) to make 4 and 9.
#  X can be placed before L (50) and C (100) to make 40 and 90.
#  C can be placed before D (500) and M (1000) to make 400 and 900.
#  Given an integer, convert it to a roman numeral.
#
#  Example 1:
#
#  Input: num = 3
#  Output: "III"
#  Explanation: 3 is represented as 3 ones.
#  Example 2:
#
#  Input: num = 58
#  Output: "LVIII"
#  Explanation: L = 50, V = 5, III = 3.
#  Example 3:
#
#  Input: num = 1994
#  Output: "MCMXCIV"
#  Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#  Constraints:
#
#  1 <= num <= 3999


def roman_func(num: int) -> str:
    """
    This function translates arabic numerals into roman
    @param num: arabic numeral
    @return: roman numeral
    """
    roman = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    result = ""
    for key in sorted(roman.keys(), reverse=True):
        while num - key >= 0:
            num = num - key
            result = result + roman[key]
    return result


def get_roman_number_uporoto(num: int) -> str:
    """
    This function translates arabic numerals into roman
    @param num: arabic numeral
    @return: roman numeral
    """
    roman_digits = [
        "",
        "{a}",
        "{a}{a}",
        "{a}{a}{a}",
        "{a}{b}",
        "{b}",
        "{b}{a}",
        "{b}{a}{a}",
        "{b}{a}{a}{a}",
        "{a}{c}",
    ]
    ones = [rd.format(a="I", b="V", c="X") for rd in roman_digits]
    tens = [rd.format(a="X", b="L", c="C") for rd in roman_digits]
    hundreds = [rd.format(a="C", b="D", c="M") for rd in roman_digits]
    millenniums = ["", "M", "MM", "MMM"]
    roman_numbers = []
    for m in millenniums:
        for h in hundreds:
            for t in tens:
                for o in ones:
                    roman_numbers.append(f"{m}{h}{t}{o}")
    return roman_numbers[num]


if __name__ == "__main__":
    print(roman_func(3))
    print(roman_func(58))
    print(roman_func(1994))

    print(get_roman_number_uporoto(3))
    print(get_roman_number_uporoto(58))
    print(get_roman_number_uporoto(1994))
