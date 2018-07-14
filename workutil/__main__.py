import sys
from .classmodule import GoogleMap
from .funcmodule import *

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    gm = GoogleMap()
    print(gm.from_work_to_home())

if __name__ == '__main__':
    main()
