#decorators are a way of taking a function and adding additional features, it takes a function as input and outputs a modified function 
#this scenario where functions are treated as values is under the functional programming paradigm

def announce(f):
    def wrapper():
        print('about to run the function...')
        f()
        print('done')
    return wrapper

#this whole thing can be called a decorator

#we use the @ to wrap a function in a decorator
@announce
def hello():
    print('Hello, world!')

hello()