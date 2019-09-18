import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def render(game,current):
    r= game['rooms']
    c=r[current]
    print('\n\nWelcome to {name}'.format(name=c['name']))
    print(c['desc'])

    '''print out the description of the current location'''


def getInput():
    toReturn=input('\nWhat would you like to do? ').strip().upper()
    return toReturn


def update(selection,game,current):
    '''check if we need to move to a new location, etc. '''
    for e in game['rooms'][current]['exits']:
        if e['verb'] == selection:
            if e['target'] == 'NoExit':
                print("You can't go that way")
            else:
                current = e['target']
    return current


def main():
    game = {}
    with open('bdream.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'WELCOME'
    quit = False
    while not quit:
       render(game,current)
       selection=getInput()
       if selection == "QUIT":
           print("Thanks for playing!")
           break
       current=update(selection,game,current)

    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()