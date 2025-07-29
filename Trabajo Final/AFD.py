#!/usr/bin/python3

from sys import exit


def getString():
    text = input('Enter a string: ')
    return text


def table1():
    print('|--------|----------------------|\n|        |  Simbolo de entrada  |\n| Estado |-----------|----------|\n|        |     a     |     b    |')
    print('|--------|-----------|----------|\n|   A    |     B     |     C    |\n|   B    |     B     |     C    |\n|   C    |     B     |     C    |')
    print('|--------|-----------|----------|')


def table2():
    print('|--------|----------------------|\n|        |  Simbolo de entrada  |\n| Estado |-----------|----------|\n|        |     a     |     b    |')
    print('|--------|-----------|----------|\n|   A    |     B     |     A    |\n|   B    |     A     |     C    |\n|   C    |     -     |     D    |')
    print('|   D    |     D     |     C    |\n|--------|-----------|----------|')


def menu():
    while True:
        option = int(input('Select an automaton: \n1) (a|b)*\n2) (aa|b)*(a|bb)*\n3) Exit\n'))
        if option > 2:
            exit()
        return option


def validation(text):
    valid = ['a','b']
    for i in range(len(text)):
        if not text[i] in valid:
            print('Caracter no valido', text[i])
            exit()


def automaton1(text):
    table1()
    aceptation = ['A','B','C']
    state = 'A'
    print('State:',state)
    for i in range(len(text)):
        if state == 'A':
            print('Character:',text[i])
            if text[i] == 'a':
                print('Transition from A to B')
                state = 'B'
            if text[i] == 'b':
                print('Transition from A to C')
                state = 'C'
        elif state == 'B':
            print('Character:',text[i])
            if text[i] == 'a':
                print('Transition from B to B')
                state = 'B'
            if text[i] == 'b':
                print('Transition from B to C')
                state = 'C'
        elif state == 'C':
            print('Character:',text[i])
            if text[i] == 'a':
                print('Transition from C to B')
                state = 'B'
            if text[i] == 'b':
                print('Transition from C to C')
                state = 'C'
        print('State:',state)

    # Versión de la tabla reducida
    
    #for i in range(len(text)):
    #   if state == 'A':
    #       if text[i] == 'a':
    #           state = 'A'
    #       if text[i] == 'b':
    #           state = 'A'   
    
    if state in aceptation:
        return print('Acceptance state reached.')


def automaton2(text):
    table2()
    aceptation = ['A','B','D']
    state = 'A'
    print('State:', state)
    for i in range(len(text)):
        if state == 'A':
            print('Character:', text[i])
            if text[i] == 'a':
                print('Transition from A to B')
                state = 'B'
            if text[i] == 'b':
                print('Transition from A to A')
                state = 'A'
        elif state == 'B':
            print('Character:', text[i])
            if text[i] == 'a':
                print('Transition from B to A')
                state = 'A'
            if text[i] == 'b':
                print('Transition from B to C')
                state = 'C'
        elif state == 'C':
            print('Character:', text[i])
            if text[i] == 'a':
                print('No transition. Error')
                exit()
            if text[i] == 'b':
                print('Transition from C to D')
                state = 'D'
        elif state == 'D':
            print('Character:', text[i])
            if text[i] == 'a':
                print('Transition from D to D')
                state = 'D'
            if text[i] == 'b':
                print('Transition from D to C')
                state = 'C'
        print('State:', state)
    
    if state in aceptation:
        return print('Acceptance state reached.')
    else:
        return print('A state of acceptance is not reached. Invalid string.')


def main():
    option = menu()    
    text = getString()
    validation(text)
    if option == 1:
        automaton1(text)
    else: 
        automaton2(text)


if __name__ == "__main__":
    main()
