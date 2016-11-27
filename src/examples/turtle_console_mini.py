#!/usr/bin/env python

"""
Logo-style turtle example (console mode).
"""

import argparse
import os.path
import sys
import time

sys.path.append(os.path.join(os.path.split(__file__)[0], '..'))

import mippy

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Turtle example (console mode).')
    mippy.add_arguments(parser)
    args = parser.parse_args()

    gt = mippy.GattTool(args.adaptor, args.device, logging=False)

    mip = mippy.Mip(gt)

    turtle = mippy.Turtle(mip)
    print
    print "OK"
    mip.playSound(0x4d)

    while True:
        try:
            user_input = raw_input('> ')
            words = user_input.split()
            if len(words) > 0:
                command = words[0]
            else:
                command = ""
            if len(words) > 1 and is_number(words[1]):
                param = float(words[1])
            else:
                param = ""
            if command == "forward":
                turtle.forward(param/100)
                mip.playSound(0x4d)
                print "OK"
            elif command == "left":
                param *= 105.0/90.0
                turtle.left(param)
                mip.playSound(0x4d)
                print "OK"
            elif command == "right":
                param *= 105.0/90.0
                turtle.right(param)
                mip.playSound(0x4d)
                print "OK"
            else:
               mip.playSound(0x4e)
               print "?"
        except EOFError:
            break

