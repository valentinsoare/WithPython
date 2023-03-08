#!/usr/bin/python


import threading


def do_work():
    print(f"Starting Work")
    i = 0
    for _ in range(2_000_000):
        i += 1
    # time.sleep(2)
    print(f'Finish Work')


def main():
    for _ in range(5):
        t = threading.Thread(target=do_work, args=())
        t.start()


if __name__ == '__main__':
    main()
