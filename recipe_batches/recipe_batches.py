#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # need = recipe
  # have = ingredients
  possible_list = []
  
  
  # need to divide each key:value pair in "have" dictionary by matching key:value pair in "recipe" dictionary
  # iterate over "have" dictionary to extract both key and value pair
  # match to corresponding key and value pair in "need" dictionary
  for key in recipe.keys():
    # make sure all recipe parts exist in ingredients
    if key in ingredients:
      # math up and round down
      possible = math.floor(ingredients[key] / recipe[key])
      # put possible into possible_list
      possible_list.append(possible)
    # if recipe part does not exist in ingredients, return 0
    else:
      return 0
  
  # return that number
  return min(possible_list)
    


  # should build some error catching in case user is missing an ingredient entirely in the "have" dictionary





if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))