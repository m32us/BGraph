#!/usr/bin python

def listed_binary(n):
    if n == 0:
        yield ""
    else:
        for bit in ('0', '1'):
            yield from (sbit+bit for sbit in listed_binary(n-1))

# print(list(listed_binary(5)))