from itertools import islice

def main(argv):
    if len(argv) == 1:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            print(f.read())
    elif len(argv) == 2:
        program, num = argv
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            read_from_line = islice(f, int(num) - 1, None)
            for i in read_from_line:
                print(i)
    elif len(argv) == 3:
        program, num_start, num_end = argv
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            read_from_line = islice(f, int(num_start) - 1, int(num_end))
            for i in read_from_line:
                print(i)



if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
