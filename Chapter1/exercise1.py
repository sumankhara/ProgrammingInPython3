import sys

zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]

one = ["   *   ", "  **   ", "   *   ", "   *   ", "   *   ", "   *   ", "  ***  "]

two = ["   ****", " *   * ", "    *  ", "   *   ", "  *    ", " *     ", "*******"]

three = ["******", "     *", "     *", "  ****", "     *", "     *", "******"]

four = ["*     *", "*     *", "*     *",  "*******", "      *", "      *", "      *"]

five = ["*******", "*      ", "*      ", "*******", "      *", "      *", "*******"]

six = ["*******", "*      ", "*      ", "*******", "*     *", "*     *", "*******"]

seven = ["*******", "      *", "      *", "      *", "      *", "      *", "      *"]

eight = ["*******", "*     *", "*     *", "*******", "*     *", "*     *", "*******"]

nine = ["*******", "*     *", "*     *", "*******", "      *", "      *", "*******"]

Digits = [zero, one, two, three, four, five, six, seven, eight, nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            for char in digit[row]:
                if char == '*':
                    line += str(number)
                else:
                    line += char
            line += "   "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as error:
    print(error, "in", digits)
