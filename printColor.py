from colorama import init
from termcolor import colored

init()  # enable ANSI colors for MS Windows


def printColor(color, *args):
    colorIt = True
    for arg in args:
        text = colored(arg, color, attrs=['reverse'])
        if colorIt:
            print(text)
        else:
            print(arg)


if __name__ == '__main__':
    printColor('green', 'Hello, world! in green reverse', 'second str\n\n')

    printColor('grey', 'Hello, world! in grey reverse')
    printColor('red', 'Hello, world! in red reverse')
    printColor('green', 'Hello, world! in green reverse')
    printColor('yellow', 'Hello, world! in yellow reverse')
    printColor('blue', 'Hello, world! in blue reverse')
    printColor('magenta', 'Hello, world! in magenta reverse')
    printColor('cyan', 'Hello, world! in cyan reverse')
    printColor('white', 'Hello, world! in white reverse')

    t = colored('Hello, world! in no color reverse', attrs=['reverse'])
    print(t)
