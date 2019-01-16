

from __future__ import annotations

from typing import Any, List, Optional, Tuple

from prefix_tree import Autocompleter, SimplePrefixTree, CompressedPrefixTree
from autocomplete_engines import LetterAutocompleteEngine, SentenceAutocompleteEngine, MelodyAutocompleteEngine

from prefix_tree import Autocompleter, SimplePrefixTree, CompressedPrefixTree

from autocomplete_engines import LetterAutocompleteEngine, \
    SentenceAutocompleteEngine



def test_empty_simple_prefix_tree() -> None:
    average_tree = SimplePrefixTree('average')
    assert average_tree.is_empty() is True
    assert average_tree.weight == 0.0
    assert average_tree.subtrees == []


def test_insert_to_empty_prefix_tree() -> None:
    tree = SimplePrefixTree('sum')
    assert tree.is_empty() is True
    assert tree.weight == 0.0
    tree.insert('123', 3.0, ['b', 'a', 'g'])
    assert tree.weight == 3.0


def test_insert_in_non_empty() -> None:
    tree = SimplePrefixTree('sum')
    tree.insert(456, 12.0, ['b', 'a', 'g', 'e'])
    tree.insert('123', 3.0, ['b', 'a', 'g'])
    assert tree.weight == 15
    assert tree.__len__() == 2
    assert tree.is_empty() is False
    tree.insert(1, 1.0, ['b', 'a'])
    assert tree.weight == 16.0
    # test average_prefix tree
    avg_tree = SimplePrefixTree('average')
    avg_tree.insert(456, 12.0, ['b', 'a', 'g', 'e'])
    avg_tree.insert('123', 3.0, ['b', 'a', 'g'])
    assert avg_tree.weight == 7.5

def test_remove_() -> None:
    tree = SimplePrefixTree('sum')
    tree.insert(456, 12.0, ['b', 'a', 'c', 'd'])
    tree.insert(12345, 1.0, ['b', 'a', 'c', 'd', 'e'])
    tree.insert('123', 3.0, ['b', 'a', 'g'])
    assert tree.weight == 16.0
    tree.remove(['b', 'a', 'c'])
    assert tree.weight == 3.0
    assert tree.__len__() == 1

def test_autocomplete() -> None:
    tree = SimplePrefixTree('sum')
    tree.insert(456, 12.0, ['b', 'a', 'c', 'd'])
    tree.insert(12345, 1.0, ['b', 'a', 'c', 'd', 'e'])
    tree.insert('123', 3.0, ['b', 'a', 'g'])
    assert tree.autocomplete(['b'], 1) == [(456, 12.0)]
    assert tree.autocomplete(['b'], None) \
           == [(456, 12.0), ('123', 3.0), (12345, 1.0)]


# test letter autocomplete engine

def test_autocomplete_letter_autocompleter() -> None:
    letter_test = \
        LetterAutocompleteEngine({'file': 'data/test_txt.txt',
                                  'autocompleter': 'simple',
                                  'weight_type': 'sum'})
    assert letter_test.autocomplete('you', 1) == [('you', 2.0)]
    assert letter_test.autocomplete('you', None) == [('you', 2.0),
                                                     ('your', 1.0),
                                                    ('youtube', 1.0)]

def test_remove_letter_autocompleter() -> None:
    letter_test = \
        LetterAutocompleteEngine({'file': 'data/test_txt.txt',
                                  'autocompleter': 'simple',
                                  'weight_type': 'sum'})
    assert letter_test.autocomplete('you', 1) == [('you', 2.0)]
    assert letter_test.autocomplete('you', None) == [('you', 2.0),
                                                     ('your', 1.0),
                                                    ('youtube', 1.0)]
    letter_test.remove('your')
    assert letter_test.autocomplete('you', None) == [('you', 2.0),
                                                     ('youtube', 1.0),]
    print('pass')



# test sentence autocomplete


def test_autocomplete_sen_autocompleter() -> None:
    sen_test = \
        SentenceAutocompleteEngine({'file': 'data/test_sentence.csv',
                                  'autocompleter': 'simple',
                                  'weight_type': 'sum'})

    assert sen_test.autocomplete('how many', 1) == [('how many city', 31.0)]
    assert sen_test.autocomplete('how many', None) == [('how many city', 31.0),
                                                       ('how many people', 30.0)
                                                       ]


def test_remove_autocomplete_sentence() -> None:
    sen_test = \
        SentenceAutocompleteEngine({'file': 'data/test_sentence.csv',
                                    'autocompleter': 'simple',
                                    'weight_type': 'sum'})

    assert sen_test.autocomplete('how many', 1) == [('how many city', 31.0)]
    assert sen_test.autocomplete('how many', None) == [('how many city', 31.0),
                                                       ('how many people', 30.0)
                                                       ]
    sen_test.remove('how many city')
    assert sen_test.autocomplete('how many', None) == [('how many people', 30.0)]





if __name__ == '__main__':
    import pytest
    pytest.main(['tests.py'])


