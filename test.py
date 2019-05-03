import time
from _datetime import datetime


def main():
    today = datetime.now().strftime('%Y-%m-%d')
    print(today)


if __name__ == '__main__':
    main()
