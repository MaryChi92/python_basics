def main(argv):
    program, revenue = argv
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        revenue = f'{revenue}\n'
        f.write(revenue)


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
