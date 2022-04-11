import math
import numpy as np


def main():
    intervals = []
    intervals = np.linspace(0, 2*math.pi, 1000)

    for entry in intervals:
        print("Sin (x) = : ", math.sin(entry))
        print("x = :", entry)


if __name__ == "__main__":
	main()
