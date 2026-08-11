from fastapi import FastAPI

#Made the fastApi Object
app = FastAPI()

# If we want to run the application we need to create a route for it. 
# A route is a path that the user can access in the browser. 
# We can create a route by using the @app.get() decorator. 
# The @app.get() decorator is used to create a route that responds to GET requests. 
# The route is defined by the path that is passed as an argument to the decorator. 
# In this case, we are creating a route for the root path ("/"). 
# The function that is defined below the decorator is called when the route is accessed. 
# The function should return a response that will be sent back to the user.
@app.get("/")
def greet():
    return ("Welcome to fastApi application!")

@app.get("/products")
def get_all_products():
    return ("This is the products page!")