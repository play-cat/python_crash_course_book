# task 8-15 3D printing
from printing_functions import print_models

unprinted_design = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_design, completed_models)

# task 8-16 import

# import pizza
# import pizza as p
# from pizza import make_pizza
# from pizza import make_pizza as mp
from pizza import *

make_pizza(12, "topping_0", "topping_1", "topping_2")
