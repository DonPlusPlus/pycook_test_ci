#!/usr/bin/env python


class codetestcodeutils(object):

  def unpack_seq_to_seperate_vars(self):
    """
          1.1. Unpacking a Sequence into Separate Variables
          Problem
          -----------------------
          You have an N-element tuple or sequence that you would like to
          unpack into a collection of N variables.
          Solution
          -----------------------
          Any sequence (or iterable) can be unpacked into variables using a simple assignment operation.
          The only requirement is that the number of variables and structure match the sequence. For example:
    """

    a = (1, 2)
    data_flat = [1, 2, 3]
    data_nested  = ["Don Johnson",(6,23,1795),"Pasadena"]
    x,y = a
    hello = "hello"
    one, two, three = data_flat
    name, date_of_birth, location = data_nested
    w,o,r,l,d = hello
