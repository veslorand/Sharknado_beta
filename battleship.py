
def map_size(size=5):
    battlemap = [["O" for x in range(size)] for y in range(size)]
    return battlemap


class ShipSize:
    def __init__(self, orientation, size):
        self.orientation = orientation
        self.size = size


def get_map_size():
    while True:
        try:
            size = int(input("Write the size of the map where you want to play: "))
            return size
        except ValueError:
            print("It is not a number!")


def print_map(battlemap):
    for x in range(len(battlemap)):
        for y in range(len(battlemap[x])):
            print(battlemap[x][y], end=" ")
        print()


def main():
    size = get_map_size()
    battlemap = map_size(size)
    print_map(battlemap)


if __name__ == "__main__":
    main()
