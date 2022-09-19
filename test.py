import pytest
from main import type_definition, my_type_definition


def test_type_definition():
    test_data = {
        'Тип3. Праволинейная грамматика': [(['S', 'A', 'B', 'B'], ['aA', 'gB', 'aA', 'b']), ],
        'Тип3. Линейная грамматика.': [(['S', 'A', 'B', 'B'], ['Aa', 'Bg', 'Aa', 'b']), ],
        'Тип2. Контекстно-свободная грамматика.': [(['S', 'S', 'K', 'K'], ['ab', 'aKSb', 'bSb', 'e']), ],
        'Тип1. Контектно-зависимая грамматика.': [(['S', 'S', 'bK', 'K'], ['ab', 'aKSb', 'bSb', 'e']), ],
        'Тип0. Грамматика общего вида.': [(['S', 'S', 'bK', 'K'], ['ab', 'aKSb', 'bSb', 'e']), ]
    }

    for expected_type in test_data:
        for gram in test_data[expected_type]:
            result_type = my_type_definition(gram)
            assert result_type == expected_type
