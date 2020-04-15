#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  need = recipe
  have = ingredients
  
  # need to divide each key:value pair in have ingredients by matching key:value pair in recipe ingredients

  # should buuild some error catching in case user is missing an ingredient entirely in the "have" dictionary

  # round down

  # find smallest value from each key value pair

  # return that number


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))