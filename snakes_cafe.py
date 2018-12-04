from textwrap import dedent
import sys


WIDTH = 60

menu = {
    'Appetizers' : {
      'Wings':0,
        'Cookies':0,
        'Spring Rolls':0
    },
    'Entrees': {
        'Salmon':0,
        'Steak':0,
        'Meat Tornado':0,
        'A Literal Garden':0,
    },
    'Desserts': {
        'Ice Cream':0,
        'Cake':0,
        'Pie':0,
    },
    'Drinks': {
        'Coffee':0,
        'Tea':0,
        'Blood of the Innocent':0,
    }
}

def padEdges(str, width, ch =' '):
    """Formatting for wording."""
    str_len = len(str)
    ragged_pad = ''
    if width % 2 != str_len % 2:
        ragged_pad = ch
    return (ch * (((width - str_len)) // 2)) + str + (ch * ((width - str_len) // 2)) + ragged_pad


def greeting():
    """Set greeting for menu."""
    line_1 = '** ' * (WIDTH // 3)
    line_2 = 'Welcome to the Snakes Cafe'
    line_3 = 'Please see our menu below'
    line_4 = 'To quit at any time type "quit"'
    print(dedent(f'''
        {'*' * WIDTH}
        {'**' + padEdges(line_2, WIDTH - 4) + '**'}
        {'**' + padEdges(line_3, WIDTH - 4) + '**'}
        {'**' + padEdges('', WIDTH - 4) + '**'}
        {'**' + padEdges(line_4, WIDTH - 4) + '**'}
        {'*' * WIDTH}
    '''))


def ask():
    """Ask user for order suggestions"""
    print(dedent(f'''
    {'*' * WIDTH}
    {'**' + padEdges('What would you like to order?', WIDTH - 4) + '**'}
    {'*' * WIDTH}
    '''))


def print_menu():
    """Show the menu based on what has been ordered"""
    for course in menu:
        print(course)
        print('-' * len(course))
        for item in menu[course]:
            print(item)
        print('\n')


def process_order(order):
    """Process user selected options"""
    if order == 'quit' or order == 'Quit' or order == 'QUIT':
        exit()
    found = False
    for course in menu:
        if order in menu[course]:
            menu[course][order] += 1
            print(f'You have {menu[course][order]} {order}')
            found = True
            break
    if not found:
        print('Try again, items are Case sensitive')

def exit():
    """Gracefull Exit."""
    print('Thank you for your Order')
    sys.exit()


if __name__ == '__main__':
    greeting()
    print_menu()
    ask()

    order = None

    while order != 'quit':
        order = input()
        process_order(order)
