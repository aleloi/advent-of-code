import enum
input_text = open("input05.txt").readlines()
# import collections

def seat(re_li):
    # "FBFBBFFRLR" ==> 44 * 8 + 5
    offset = 0
    pow2 = 2**6
    for x in re_li[:7]:
        if x == 'B':
            offset += pow2
        pow2 //= 2
    pos_length = offset

    pow2 = 4
    offset = 0
    for x in re_li[7:]:
        if x == 'R':
            offset += pow2
        pow2 //= 2
    return pos_length * 8 + offset

# print(seat("FBFBBFFRLR"))

class Seat(enum.Enum):
    EMPTY = enum.auto()
    OCCUPIED = enum.auto()

    @classmethod
    def from_bool(cls, self_occupied):
        return cls.OCCUPIED if self_occupied else cls.EMPTY

def main():
    seats = set(seat(x) for x in input_text)
    compressed = []
    first_pos_in_streak, last_seat_status = -1, Seat.EMPTY

    for s in range(0, 128*8):
        curr_seat_status = Seat.from_bool(s in seats)
        if last_seat_status != curr_seat_status:
            compressed.append(
                (first_pos_in_streak, s-1, last_seat_status))
            first_pos_in_streak = s
            last_seat_status = curr_seat_status
    compressed.append((first_pos_in_streak, s, last_seat_status))
    for fro, to, stat in compressed:
        print("[{}, {}]: {}".format(fro, to, stat))
        

if __name__ == "__main__":
    main()
