#!/usr/bin/python3
"""implementing a log parsing sys using generated facts
"""
import sys


def log_parser(status_code_dict, size):
    """This function accepts a dictionary and an integer which will
       first be sorted and then be printed accordingly
       Args:
            status_code_dict: Contain status code and it counts
            size: Total file size
    """
    print("File size: {}".format(size))
    for code, count in sorted(status_code_dict.items()):
        if count != 0:
            print("{}: {}".format(code, count))


counter = 0
file_size = 0
status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
try:
    for line in sys.stdin:
        parser = line.split()[::-1]  # reverse log info
        if counter < 10 and len(parser) > 2:
            counter += 1  # incrementing the count
            file_size += int(parser[0])
            if parser[1] in status_code.keys():
                status_code[parser[1]] += 1
        if counter == 10:
            log_parser(status_code, file_size)
            counter = 0
finally:
    log_parser(status_code, file_size)
