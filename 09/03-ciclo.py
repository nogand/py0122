#!/usr/bin/env python3
import sys

for archivo in sys.argv[1:] :
  with open(archivo, 'r') as fp:
    while True:
      cur_line = fp.readline().rstrip('\n')
      # If the result is an empty string
      if cur_line == '':
        # We have reached the end of the file
        break
      print(cur_line)
