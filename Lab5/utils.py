def process_item(x):
    """

        1) a) Write a module named utils.py that contains one function called process_item. The function will have one
        parameter, x, and will return the least prime number greater than x. When run, the module will request an input from
        the user, convert it to a number and it will display the output of the process_item function.

    """
    if x <= 1 or x + 1 == 2:
        return 2

    prime = 0
    while not prime:
        for i in range(2, int((x + 1) / 2 + 1)):
            if (x + 1) % i == 0:
                x = x + 1
                prime = -1
                break
        prime = 0 if prime == -1 else 1

    return x + 1


if __name__ == '__main__':
    x = int(input("Enter number: "))
    print(process_item(x))
else:
    print(f"{__name__} module loaded...")




