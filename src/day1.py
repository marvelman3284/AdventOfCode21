def count_increases(arr: list) -> int:
    inc = 0
    for i in range(len(arr)):
        try:
            if arr[i + 1] > arr[i]:
                inc += 1
        except IndexError:
            if arr[i] > arr[i - 1]:
                inc += 1
            break

    return inc


def count_3_increases(arr: list[int]) -> int:
    inc3 = 0
    for i in range(len(arr)):
        try:
            sum1 = arr[i] + arr[i + 1] + arr[i + 2]
            sum2 = arr[i + 1] + arr[i + 2] + arr[i + 3]

            print(f"First({i}): ", arr[i], arr[i + 1], arr[i + 2])
            print("2nd: ", arr[i + 1], arr[i + 2], arr[i + 3])
            if sum2 > sum1:
                inc3 += 1
        except IndexError:
            break

    return inc3


def main():
    inputs = []
    with open("data/day1.txt", "r") as f:
        for i in f.readlines():
            i.replace("\n", "")
            inputs.append(int(i))

    print(count_increases(inputs))

    print(count_3_increases(inputs))


if __name__ == "__main__":
    main()
