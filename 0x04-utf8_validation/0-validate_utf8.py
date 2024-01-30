#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """ checks if UTF-8 encoding is valid"""
    i = 0
    while i < len(data):
        byte = data[i]
       
        if (byte & 0x80) == 0x00:
            """for 1 byte character 0xxxxxxx"""
            i += 1
            
        elif (byte & 0xE0) == 0xC0:
            """for 2 byte character 110xxxxx"""
            if i + 1 >= len(data) or (data[i + 1] & 0xC0) != 0x80:
                return False
            i += 2
        elif (byte & 0xF0) == 0xE0:
            """for 3 byte character: 1110xxxx"""
            if i + 2 >= len(data) or (data[i + 1] & 0xC0) != 0x80 or (
                    data[i + 2] & 0xC0) != 0x80:
                return False
            i += 3
        elif (byte & 0xF8) == 0xF0:
            """for 4 byte character 11110xxx"""
            if i + 3 >= len(data) or (data[i + 1] & 0xC0) != 0x80 or (
                 data[i + 2] & 0xC0) != 0x80 or (data[i + 3] & 0xC0) != 0x80:
                return False
            i += 4
        else:
            return False
    return True
