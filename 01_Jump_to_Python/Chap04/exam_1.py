import sys

args = sys.argv[1:]

def greet_users(args):
    for i in args:
        up = i[0].upper()
        other = i[1:]
        i = up + other

        print("Hello, %s!" %i)
        # print("Hello, %s%s!" %(i[0].upper(), i[1:]))

greet_users(args)