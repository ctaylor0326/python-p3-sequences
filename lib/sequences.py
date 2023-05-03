#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        fib_list = []
        print(fib_list)
    elif length == 1:
        fib_list = [0]
        print(fib_list)
    else:
        fib_list = [0, 1]
        for i in range(2, length):
            last = fib_list[-1]
            pent = fib_list[-2]
            next = last + pent
            fib_list.append(next)
        print(fib_list)
