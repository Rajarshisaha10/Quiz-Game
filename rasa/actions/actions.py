# Import the custom action class from your separate file
from .order_food import ActionOrderFood
from .basics import ActionGetTime
from .granny import Actionstart_granny

# The Action Server will automatically find and register any Action subclasses
# that are imported into this file. You don't need to do anything else here.
# Just make sure your imports are correct.