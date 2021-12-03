def get_eplison_bits(arr: list, idx: int) -> int:
    zero = 0
    one = 0
    for i in arr:
        if i[idx] == "0":
            zero += 1
        if i[idx] == "1":
            one += 1

    if zero < one:
        return 0
    elif zero > one:
        return 1
    else:
        return -1


def get_oxy_bits(arr: list, idx: int) -> int:
    zero = 0
    one = 0
    for i in arr:
        if i[idx] == "0":
            zero += 1
        if i[idx] == "1":
            one += 1

    if zero == one:
        return 1
    if zero > one:
        return 0
    elif one > zero:
        return 1
    else:
        return -1


def get_co2_bits(arr: list, idx: int) -> int:
    zero = 0
    one = 0
    for i in arr:
        if i[idx] == "0":
            zero += 1
        if i[idx] == "1":
            one += 1

    if zero == one:
        return 0
    if zero < one:
        return 0
    elif one < zero:
        return 1
    else:
        return -1


def get_gamma_bits(arr: list, idx: int) -> int:
    zero = 0
    one = 0
    for i in arr:
        if i[idx] == "0":
            zero += 1
        if i[idx] == "1":
            one += 1

    if zero > one:
        return 0
    elif one > zero:
        return 1
    else:
        return -1


def get_gamma_rate(arr: list) -> int:
    gamma = ""
    for i in range(len(arr[0])):
        gamma += str(get_gamma_bits(arr, i))

    return int(gamma, 2)


def get_eplison_rate(arr: list) -> int:
    eplison = ""
    for i in range(len(arr[0])):
        eplison += str(get_eplison_bits(arr, i))

    return int(eplison, 2)


def get_oxy_rating(arr: list) -> int:

    for i in range(len(arr[0])):

        if len(arr) == 1:
            break

        arr = [x for x in arr if x[i] == str(get_oxy_bits(arr, i))]

    return int(arr[0], 2)


def get_co2_rating(arr: list) -> int:
    for i in range(len(arr[0])):

        if len(arr) == 1:
            break

        arr = [x for x in arr if x[i] == str(get_co2_bits(arr, i))]

    return int(arr[0], 2)


def main():

    with open("data/day3.txt", "r") as f:
        inputs = [x.replace("\n", "") for x in f.readlines()]

    gamma = get_gamma_rate(inputs)
    eplison = get_eplison_rate(inputs)

    co2 = get_co2_rating(inputs)
    oxy = get_oxy_rating(inputs)

    print(gamma * eplison)
    print(co2 * oxy)


if __name__ == "__main__":
    main()
