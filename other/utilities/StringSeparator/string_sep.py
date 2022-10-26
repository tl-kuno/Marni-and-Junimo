def string_seperator(string):
    num_printed = 0
    for char in string:
        if num_printed < 99 and char != " ":
            print(char, end='')
            num_printed += 1
        else:
            num_printed = 0
            print(char)


def main():
    string_to_process = input("Enter string to separate: ")
    string_seperator(string_to_process)


if __name__ == '__main__':
    main()
