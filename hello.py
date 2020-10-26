import sys

greeting = 'Hello'

if __name__ == '__main__':
    print('{} {}'.format(greeting, sys.argv[1] if len(sys.argv) > 1 else 'World!'))
