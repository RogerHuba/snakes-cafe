from textwrap import dedent
import sys
print('This is the run test!')

run = True
WIDTH = 60
BANK = [
    {
        'appetizer_one': 'wings',
        'appetizer_two': 'cookies',
        'appetizer_three': 'spring Rolls',
    },
    {
        'entree_one': 'salmon',
        'entree_two': 'steak',
        'entree_three': 'meat tornado',
        'entree_four': 'a literal garden',
    },
    {
        'dessert_one': 'ice cream',
        'dessert_two': 'cake',
        'dessert_three': 'pie',
    },
    {
        'drinks_one': 'coffee',
        'drinks_two': 'tea',
        'drinks_thress': 'blood of the innocent',
    },
]


def welcome():
    """Function for creating a greeting and menu for the user
    set variables for the menu
    create the order menu
    """

    welcome_string1 = 'Welcome to the Snakes Cafe!'
    wlecome_string2 = 'Please see our menu below.'
    quit_string = 'To quit at any time, type quit.'

    print(dedent(f'''
        {'*' * WIDTH}
        {(' ' ** ((WIDTH - len(welcome_string1)) // 2)) + welcome_string1 + (' ' ** ((WIDTH - len(welcome_string1)) // 2))}
        {(' ' ** ((WIDTH - len(wlecome_string2)) // 2)) + wlecome_string2 + (' ' ** ((WIDTH - len(wlecome_string2)) // 2))}
 #       {' '}
        {(' ' ** ((WIDTH - len(quit_string)) // 2)) + quit_string + (' ' ** ((WIDTH - len(quit_string)) // 2))}
        {'*' * WIDTH}
    '''))

    while run is True:
        print('Ask the question to do the thing!')


    # {(' ' * ((WIDTH - len(appetizer_one)) // 2)) + appetizer_one + (' ' * ((WIDTH - len(appetizer_one)) // 2))}
    # {(' ' * ((WIDTH - len(appetizer_two)) // 2)) + appetizer_two + (' ' * ((WIDTH - len(appetizer_two)) // 2))}
    # {(' ' * ((WIDTH - len(appetizer_three)) // 2)) + appetizer_three + (' ' * ((WIDTH - len(appetizer_three)) // 2))}
    # {(' ' * ((WIDTH - len(entree_one)) // 2)) + entree_one + (' ' * ((WIDTH - len(entree_one)) // 2))}
    # {(' ' * ((WIDTH - len(entree_two)) // 2)) + entree_two + (' ' * ((WIDTH - len(entree_two)) // 2))}
    # {(' ' * ((WIDTH - len(entree_three)) // 2)) + entree_three + (' ' * ((WIDTH - len(entree_three)) // 2))}
    # {(' ' * ((WIDTH - len(entree_four)) // 2)) + entree_four + (' ' * ((WIDTH - len(entree_four)) // 2))}
    # {(' ' * ((WIDTH - len(drink_one)) // 2)) + drink_one + (' ' * ((WIDTH - len(drink_one)) // 2))}
    # {(' ' * ((WIDTH - len(drink_two)) // 2)) + drink_two + (' ' * ((WIDTH - len(drink_two)) // 2))}
    # {(' ' * ((WIDTH - len(drink_three)) // 2)) + drink_three + (' ' * ((WIDTH - len(drink_three)) // 2))}



def check_user_input():
    return



def run_program():
    welcome()
    return


def total_order():
    return



def wrong_item():
    return



def exit():
    return

run_program()
