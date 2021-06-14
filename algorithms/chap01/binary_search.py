from typing import Sequence


def index_of(items: Sequence[int], key: int) -> int:
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if key < items[mid]:
            high = mid - 1
        elif key > items[mid]:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    import sys
    import time
    from algorithms.utils import Reader

    start = time.time()
    file_reader = Reader.from_file(sys.argv[1])
    whitelist = sorted(file_reader.read_as_int())

    stdin_reader = Reader.from_stdin()
    match_count = 0
    for key in stdin_reader.read_as_int():
        if index_of(whitelist, key) == -1:
            match_count += 1
            print(key)
    elapsed = time.time() - start
    print(f"{match_count} matches {elapsed:.3f} seconds")
