#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = prices[1] - prices[0]
  print(prices)
  # find the difference between one value and all values after it
  # assign that value to profit
  # important to make sure not to check values before the current value
  # probably need to slice the list for that
  for i in range(len(prices)-1):
    for j in prices[i+1:]:
      profit = j - prices[i]

  # is that value larger than the current max_profit?
  # yes: store in max_profit, move on
  # no: disregard, move on
      if profit >= max_profit:
        max_profit = profit
        # print(max_profit)
      else:
        # print(max_profit)
        pass

  # return that value
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))