def multiply(x: int, y: int):
    if y < 0:
        return - multiply(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply(x, y - 1)


if __name__ == "__main__":
    first_number = int(input('Enter your First Number : '))
    second_number = int(input('Enter your Second Number : '))
    print(multiply(first_number, second_number));
