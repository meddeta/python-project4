################
#EECS 1015 - Lab 5
# Author: Melika Sherafat
# Email: melika.sherafatt@gmail.com
# Student ID: 218970871
# Section B

import random


def main():
    print("\n--------- TASK 1: Random List -------------")
    import random

    def generateRandomList(list_size, maximum_integer_value):
        return random.sample(range(0, maximum_integer_value + 1), list_size)

    def computeAverage(listl):
        ans = 0
        for i in listl:
            ans += i
        ans = ans / len(listl)
        return ans;

    list_size = int(input("Input list size: ").rstrip())
    max_int = int(input("Input max int: ").rstrip())
    print("generated list")
    l = generateRandomList(list_size, max_int)
    print(l)
    print("Average value = " + str("{:.4f}".format(computeAverage(l))))
    print("\n--------- TASK 2: Phone number to text ---")

    def stringToCharLst(inputString):
        ans = []
        for s in inputString:
            ans.append(s)
        return ans

    def charsToWord(list):
        value_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
                      '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '-': 'dash'
                      }
        ans = []
        for s in list:
            ans.append(value_dict[s])
        return ans

    print("Enter phone number as XXX-XXX-XXXX")
    phone_number = input("Type here: ").rstrip()
    chars = stringToCharLst(phone_number)
    words = charsToWord(chars)
    print(chars)
    print(words)
    ans_str = ""
    for w in words:
        ans_str = ans_str + w + "->"
    print(ans_str[:-2])

    input("Press enter to exit.")


if __name__ == "__main__":
    main()