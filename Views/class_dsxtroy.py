# creating a class named destructor
class destructor:

# initializing the class
   def __init__(self):
      print ("Object gets created")

# calling the destructor
   def __del__(self):
      print ("Object gets destroyed")

# create an object
Object = destructor()

# deleting the object
del Object