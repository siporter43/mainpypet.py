# write a function add that takes two arguments and returns the sum of those
# arguments

MENU = {
    "sausage": {
        "name": "Ducky",
        "price": 15
    },
    "pizza": {
        "name": "Mortadella",
        "price": 40
    }
}

def add( y, x):
    return y+x

def power(y, x):
    return pow(y ,x)

def subt(y, x):
    return y-x 

def mult(y, x):
    return y*x
    
def div(y, x):
    return y/x

def hello():
    print(f"hello")

def subtotal(key, quantity):
    # Create a condition that questions whether the key exists
    # breakpoint()
    # Expression exercise using debugger to figure out what it is
    if not MENU.get(key, ):
        # if not case then continue
        return 0
    # Get the price from the menu
    perfect_price = MENU[key]["price"]
    # Multiply price by quantity
    whole_price = perfect_price * quantity
    # Return it
    return whole_price
