import numpy as np

from uv_tutorial_lib import hello

def add(x: list[float], y: list[float]) -> float:
    return np.sum(x) + np.sum(y)

def main():
    print("Hello from uv-tutorial-app!")
    print(f"The result of add is: {add([1, 2], [3, 4]) = }")
    print(hello())


if __name__ == "__main__":
    main()
