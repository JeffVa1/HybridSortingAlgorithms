from typing import List, Any, Dict
from HybridSort import insertion_sort, merge_sort, hybrid_sort, inversions_count, find_match
from random import seed, sample, randint


def test_insertion_sort():
    # Test with basic set of integers.
    data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
    print("Original: ", data)
    result = data
    insertion_sort(result)
    expected = sorted(data)
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

    # Test with basic set of strings.
    data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
    print("Original: ", data)
    result = data
    insertion_sort(result)
    expected = sorted(data)
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

    # Test with already sorted data.
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Original: ", data)
    result = data
    insertion_sort(result)
    expected = data
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

    # Test empty.
    data = []
    print("Original: ", data)
    result = data
    insertion_sort(result)
    expected = []
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

    # Check that function does not return anything
    data = [5, 6, 3, 2]
    print("Original: ", data)
    result = insertion_sort(data)
    expected = None
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

def test_merge_sort():
    data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
    print("Original: ", data)
    result = data
    merge_sort(result)
    expected = sorted(data)
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

    # Test with basic set of strings.
    data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
    print("Original: ", data)
    result = data
    merge_sort(result)
    expected = sorted(data)
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

    # Test with already sorted data.
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Original: ", data)
    result = data
    merge_sort(result)
    expected = data
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

    # Test empty.
    data = []
    print("Original: ", data)
    result = data
    merge_sort(result)
    expected = []
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

def test_hybrid_sort():
    # Test with small threshold.
    data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
    print("Original: ", data)
    threshold = 2
    result = data
    hybrid_sort(result, threshold)
    expected = sorted(data)
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

    # Test with max threshold.
    print("Original: ", data)
    threshold = 9
    result = data
    hybrid_sort(result, threshold)
    expected = sorted(data)
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

    # Test with threshold out of bounds.
    print("Original: ", data)
    threshold = 20
    result = data
    hybrid_sort(result, threshold)
    expected = sorted(data)
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

    print("Original: ", data)
    threshold = -9
    result = data
    hybrid_sort(result, threshold)
    expected = sorted(data)
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

    # Check that function does not return anything
    print("Original: ", data)
    data = [5, 6, 3, 2]
    threshold = 3
    result = hybrid_sort(data, threshold)
    expected = None
    print("Result: ", result)
    print("Expected: ", expected)
    print(result == expected)
    print()

def test_inversion_count():
    # Even Length List

    print("TEST 1")
    data = [2, 4, 3, 1]
    inversions = inversions_count(data)
    print("Inversions: ", inversions)
    print(inversions == 4)
    print("-----------------------")
    print()

    print("TEST 2")
    data = [4, 3, 2, 1]
    inversions = inversions_count(data)
    print("Inversions: ", inversions)
    print(inversions == 6)
    print("-----------------------")
    print()

    print("TEST 3")
    data = [1, 2, 3, 4]
    inversions = inversions_count(data)
    print("Inversions: ", inversions)
    print(inversions == 0)
    print("-----------------------")
    print()

    print("TEST 4")
    # Odd Length List
    data = [2, 4, 1, 3, 5]
    inversions = inversions_count(data)
    print("Inversions: ", inversions)
    print(inversions == 3)
    print("-----------------------")
    print()

    print("TEST 5")
    data = [5, 4, 3, 2, 1]
    inversions = inversions_count(data)
    print("Inversions: ", inversions)
    print(inversions == 10)
    print("-----------------------")
    print()

    print("TEST 6")
    data = [1, 2, 3, 4, 5]
    inversions = inversions_count(data)
    print("Inversions: ", inversions)
    print(inversions == 0)
    print("-----------------------")
    print()

    print("TEST 7")
    # Random Tests
    seed(1130)
    data = [randint(0, 100) for _ in range(10)]
    inversions = inversions_count(data)
    print("Inversions: ", inversions)
    print(inversions == 30)
    print("-----------------------")
    print()

    print("TEST 8")
    in_order = sorted(data)
    print(in_order)
    in_order_inversions = inversions_count(in_order)
    print("Inversions: ", in_order_inversions)
    print(in_order_inversions == 0)
    print("-----------------------")
    print()

    print("TEST 9")
    reverse = sorted(data, reverse=True)
    print(reverse)
    reverse_inversions = inversions_count(reverse)
    print("Inversions: ", reverse_inversions)
    print(reverse_inversions == 45)
    print("-----------------------")
    print()

    print("TEST 10")
    data = [randint(0, 100) for _ in range(11)]
    print(data)
    inversions = inversions_count(data)
    print("Inversions: ", inversions)
    print(inversions == 27)
    print("-----------------------")
    print()

    print("TEST 11")
    in_order = sorted(data)
    print(in_order)
    in_order_inversions = inversions_count(in_order)
    print("Inversions: ", in_order_inversions)
    print(in_order_inversions == 0)
    print("-----------------------")
    print()

    print("TEST 12")
    reverse = sorted(data, reverse=True)
    print(reverse)
    reverse_inversions = inversions_count(reverse)
    print("Inversions: ", reverse_inversions)
    print(reverse_inversions == 55)
    print("-----------------------")
    print()

def test_find_match():
    winnie_the_pooh_interests_ = ['Hunny', 'Playing Poohsticks', 'Adventures', 'Poems', 'Mornings']
    candidate_interests = {
        "Eeyore": ['Mornings', 'Poems', 'Adventures', 'Playing Poohsticks', 'Hunny'],
        "Piglet": ['Poems', 'Playing Poohsticks', 'Mornings', 'Adventures', 'Hunny'],
        'Tigger': ['Adventures', 'Mornings', 'Hunny', 'Poems', 'Playing Poohsticks'],
        'Rabbit': ['Playing Poohsticks', 'Hunny', 'Adventures', 'Poems', 'Mornings']
    }

    best_match = find_match(winnie_the_pooh_interests_, candidate_interests)
    print()
    print(best_match)
    print(best_match == 'Rabbit')

    prince_charming_interests = ['one glass slipper', 'hide and seek', 'gardens', 'magic',
                                 'horseback riding', 'ruling a kingdom', 'clocks']
    candidate_interests = {
        'Drizella': ['ruling a kingdom', 'magic', 'hide and seek', 'one glass slipper',
                     'clocks', 'gardens', 'horseback riding'],
        'Anastasia': ['magic', 'one glass slipper', 'ruling a kingdom', 'gardens',
                      'clocks', 'hide and seek', 'clocks'],
        'Cinderella': ['horseback riding', 'magic', 'one glass slipper', 'clocks',
                       'gardens', 'hide and seek', 'ruling a kingdom'],
        'Princess Chelina of Zaragosa': ['ruling a kingdom', 'gardens', 'horseback riding',
                                         'magic', 'clocks', 'hide and seek', 'one glass slipper'],
        'Captain of the Guard': ['horseback riding', 'one glass slipper', 'hide and seek', 'magic',
                                 'gardens', 'clocks', 'ruling a kingdom']
    }

    best_match = find_match(prince_charming_interests, candidate_interests)
    print()
    print(best_match)
    print(best_match == 'Captain of the Guard')

    snow_white_interests = ['cleaning after 7 dwarves', 'singing with animals', 'washing hands', 'cooking']

    candidate_interests = {
        "The Prince": ['cleaning after 7 dwarves', 'singing with animals', 'cooking', 'washing hands'],
        "Doc": ['cleaning after 7 dwarves', 'washing hands', 'cooking', 'singing with animals'],
        "Grumpy": ['cleaning after 7 dwarves', 'washing hands', 'singing with animals', 'cooking'],
        "Happy": ['washing hands', 'cleaning after 7 dwarves', 'cooking', 'singing with animals'],
        "Sleepy": ['cooking', 'washing hands', 'cleaning after 7 dwarves', 'singing with animals'],
        "Sneezy": ['cooking', 'cleaning after 7 dwarves', 'singing with animals', 'washing hands'],
        "Bashful": ['singing with animals', 'washing hands', 'cooking', 'cleaning after 7 dwarves'],
        "Dopy": ['singing with animals', 'cleaning after 7 dwarves', 'washing hands', 'cooking']
    }

    best_match = find_match(snow_white_interests, candidate_interests)
    print()
    print(best_match)
    print(best_match == "The Prince")


#test_insertion_sort()
#test_merge_sort()
#test_hybrid_sort()
#test_inversion_count()
#test_find_match()