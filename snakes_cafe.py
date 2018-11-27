from textwrap import dedent
import sys

#global variables and arrays
quitting = False
WIDTH = 50
CATEGORIES = ['Appetizers', 'Entrees', 'Desserts', 'Drinks']
APPS = ['wings', 'cookies', 'spring rolls']
DESR = ['ice cream', 'cake', 'pie']
ENTR = ['salmon', 'steak', 'meat tornado', 'a literal garden']
DRIN= ['coffee', 'tea', 'blood of the innocent']


def welcome():
    """Function for creating a greeting and menu for the user
    set variables for the menu
    create the order menu
    """

    welcome_string1 = 'Welcome to the Snakes Cafe!'
    wlecome_string2 = 'Please see our menu below.'
    quit_string = 'To quit at any time, type "quit".'
    question_string = 'What would you like to order?'

    print(dedent(f'''
        {'*' * WIDTH}
        {'**' + (' ' * (((WIDTH - len(welcome_string1)) -6) // 2)) + welcome_string1 + (' ' * ((WIDTH - len(welcome_string1)) // 2)) + '**'}
        {'**' + (' ' * (((WIDTH - len(wlecome_string2)) -8) // 2)) + wlecome_string2 + (' ' * ((WIDTH - len(wlecome_string2)) // 2)) + '**'}
        {'**' + (' ' * (WIDTH - 4)) + '**'}
        {'**' + (' ' * (((WIDTH - len(quit_string)) -6) // 2))     + quit_string     + (' ' * ((WIDTH - len(quit_string)) // 2)) + '**'}
        {'*' * WIDTH}
        {' ' * WIDTH}
        #Need to do a nested loop here to simplify code
        {CATEGORIES[0]}
        {'_' * len(CATEGORIES[0])}
        {'Wings'}
        {'Cookies'}
        {'Spring Rolls'}
        {CATEGORIES[1]}
        {'_' * len(CATEGORIES[1])}
        {'Salmon'}
        {'Steak'}
        {'Meat Tornado'}
        {'A Literal Garden'}
        {CATEGORIES[2]}
        {'_' * len(CATEGORIES[2])}
        {'Ice Cream'}
        {'Cake'}
        {'Pie'}
        {CATEGORIES[3]}
        {'_' * len(CATEGORIES[3])}
        {'Coffee'}
        {'Tea'}
        {'Blood of the Innocent'}
        {'*' * WIDTH}
        {'**' + (' ' * (((WIDTH - len(question_string)) -6) // 2)) + question_string + (' ' * ((WIDTH - len(question_string)) // 2)) + '**'}
        {'*' * WIDTH}
    '''))
    return


def run_program():
    """Function for starting the application
    """
    welcome()
    while quitting is False:
        user_answer = str.lower(input())
        check_user_input(user_answer)
    exit()

def check_user_input(user_answer):
    """Function for checking user answer and testing against the arrays
    """
    if user_answer == 'quit':
        exit()
    else:

        if (user_answer in APPS) or (user_answer in ENTR) or (user_answer in DESR) or (user_answer in DRIN) :
            print('Order of ' + user_answer + ' has been added to your meal')
            add_to_order()
        else:
            print('Sorry. That item is not on the menu yet!')
    return


def add_to_order():
    print('total the order')


def exit():
    print('Thank you for your Order')
    sys.exit()


run_program()
