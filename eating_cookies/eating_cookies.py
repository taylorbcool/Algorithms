#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
cache = {}

def eating_cookies(n, cache=cache):
  # check cache
  if cache is not None:
    if n in cache:
      return cache[n]
  
  # set result to base case
  result = 1

  if n == 2:
    result = 2
  elif n > 2:
    result = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

  if cache is not None:
    cache[n] = result

  return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')