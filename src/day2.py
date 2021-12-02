def split_arr(arr: list) -> list[str]:
    for i, j in enumerate(arr):
        arr[i] = j.split(" ") 

    return arr

def get_pos_w_aim(arr:list) -> int:
    horz = 0
    depth = 0
    aim = 0
    for i in arr:
        if i[0] == "forward":
            horz += int(i[1])
            depth += int(i[1]) * aim
        elif i[0] == "down":
            aim += int(i[1])
        elif i[0] == "up":
            aim -= int(i[1])

    return horz * depth


def get_pos(arr: list) -> int:
    horz = 0
    vert = 0
    for i in arr:
        if i[0] == "forward":
            horz += int(i[1])
        elif i[0] == "down":
            vert += int(i[1])
        elif i[0] == "up":
            vert -= int(i[1])

    return horz*vert

def main():
    inputs = []

    with open('data/day2.txt', 'r') as f:
        for i in f.readlines():
            i = i.replace("\n", "")
            inputs.append(i)

    print(get_pos_w_aim(split_arr(inputs)))

if __name__ == "__main__":
    main()
