#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # n == number of plays per round
  plays = ['rock', 'paper', 'scissors']
  # empty list of lists
  possible = [[]]

  if n == 0:
    return possible
  
  # for each permutation create a sublist
  for i in range(n):
    sublist = []

    # append the correct number of r, p, or s based on n
    for j in possible:
      sublist.append(j + ['rock'])
      sublist.append(j + ['paper'])
      sublist.append(j + ['scissors'])
    possible = sublist

  return possible


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')