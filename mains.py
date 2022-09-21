import sys
def print_name():
    print('Hi','Hello',sys.argv[1])
    print(__name__)
if __name__== '__main__':
    print_name()