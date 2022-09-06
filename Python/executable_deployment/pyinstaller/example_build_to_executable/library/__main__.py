import argparse

from library.bar import example1
from library.foo import example2

from array_sum_example.array_sum_example import array_sum

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--echo", default="echo echo")
    args = parser.parse_args()

    print(f"{args.echo}")
    print()
    print("test")
    example1()
    example2()
    print("\nC IMPORT\n")
    array_sum()
    input()
