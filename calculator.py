import operator
from operator import truediv


def main():
    num_1 = int(
        input(": "),
    )
    operation = str(
        input("OPERATION : "),
    )
    num_2 = int(
        input(": "),
    )

    if operation != "+" and "-" and "*" and "/":
        print("ERROR : operation invalid")
    if operation == "+":
        print("ANSWER = ", operator.add(num_1, num_2))
    if operation == "-":
        print("ANSWER = ", operator.sub(num_1, num_2))
    if operation == "*":
        print("ANSWER = ", operator.mul(num_1, num_2))
    if operation == "/":
        print("ANSWER = ", operator.truediv(num_1, num_2))


if __name__ == "__main__":
    main()
