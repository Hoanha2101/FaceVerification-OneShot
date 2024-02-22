from utils import *

distance, door_open_flag = verify("images/nga.png", "hoan", database, model)

print("(", distance, ",", door_open_flag, ")")

