# import modules
import pizza

toppings_list = ["pepperoni", "mushrooms", "extra cheese", "green peppers"]

# using function from module
pizza.make_pizza(16, *toppings_list)
pizza.make_pizza(12, "mushrooms", "extra cheese")

# importing specific functions
# from module_name import function_name
# from module_name import function_0, function_1, function_2
from pizza import make_pizza

make_pizza(16, *toppings_list)

# keyword as: function alias
# from module_name import function_name as fn
from pizza import make_pizza as mp

mp(16, *toppings_list)

# keyword as: module alias
# import module_name as mn
import pizza as p

p.make_pizza(16, *toppings_list)

# import all module functions
# from module_name import *
from pizza import *

make_pizza(16, *toppings_list)

# function implementation

# def function_name(parameter_0 parameter_1="default_value")

# function_name(value_0 parameter_1="value")

# def function_name(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5):
#     pass
