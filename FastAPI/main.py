from typing import Optional


def say_hi(name: Optional[int]):
    val = 2*name
    print(f"Hey {val}!")
    print("Hi {0}, my name is {1}".format("Adi", True))


if __name__ == "__main__":
    say_hi(2)