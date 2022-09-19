from typing import List, Tuple


def only_one_non_terminal_symbol_in_left(left):
    for symbol in left:
        if len(symbol) == 1 and symbol.isupper():
            continue
        else:
            return False
    return True


def terminal_in_front_of_non_terminal_or_only_terminal(right):
    for symbol in right:
        if len(symbol) == 1 and not symbol[0].isupper():
            continue
        elif symbol[1].isupper() and len(symbol) <= 2:
            continue
        else:
            return False
    return True


def non_terminal_in_front_of_terminal_or_only_terminal(right):
    for symbol in right:
        if len(symbol) == 1 and not symbol.isupper():
            continue
        elif symbol[0].isupper() and len(symbol) <= 2:
            continue
        else:
            return False
    return True


def left_le_right(left, right):
    for left_symbol, right_symbol in zip(left, right):
        if len(left_symbol) > len(right_symbol):
            return False
    return True


def my_type_definition(grammar: Tuple[List]):
    left, right = grammar

    if only_one_non_terminal_symbol_in_left(left):
        if terminal_in_front_of_non_terminal_or_only_terminal(right):
            return 'Тип3. Праволинейная грамматика'
        elif non_terminal_in_front_of_terminal_or_only_terminal(right):
            return 'Тип3. Линейная грамматика.'
        else:
            return 'Тип2. Контекстно-свободная грамматика.'
    else:
        if left_le_right(left, right):
            return 'Тип1. Контектно-зависимая грамматика.'

        else:
            return 'Тип0. Грамматика общего вида.'


if __name__ == '__main__':
    gram = (['S', 'A', 'B', 'B'], ['aA', 'gB', 'aA', 'b'])
    print(my_type_definition(gram))
