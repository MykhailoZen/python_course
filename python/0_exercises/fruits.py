from typing import Tuple, Dict
from collections import defaultdict


def count_fruits_0(fruits: Tuple[str, ...]) -> Dict[str, int]:
    """
    This function calculates the number of fruits in the first way.
    The fruit key order by first inclusion in the tuple.
    @param fruits: tuple of fruits
    @return: the result of the calculation containing pairs of the name of the fruit and its quantity
    """
    dict_count = {}
    for fruit in fruits:
        if fruit not in dict_count:
            dict_count[fruit] = 1
        else:
            dict_count[fruit] += 1
    return dict_count


def count_fruits_1(fruits: Tuple[str, ...]) -> Dict[str, int]:
    """
    This function calculates the number of fruits in the second way.
    The fruit key order by first inclusion in the tuple.
    @param fruits: tuple of fruits
    @return: the result of the calculation containing pairs of the name of the fruit and its quantity
    """
    dict_counts = {}
    for fruit in fruits:
        dict_counts.update({fruit: 1}) if fruit not in dict_counts.keys() \
            else dict_counts.update({fruit: dict_counts[fruit] + 1})
    return dict_counts


def count_fruits_2(fruits: Tuple[str, ...]) -> Dict[str, int]:
    """
    This function calculates the number of fruits in the third way.
    The fruit key order is random.
    @param fruits: tuple of fruits
    @return: the result of the calculation containing pairs of the name of the fruit and its quantity
    """
    dict_counts = {}
    for fruit in set(fruits):
        dict_counts[fruit] = fruits.count(fruit)
    return dict_counts


def count_fruits_3(fruits: Tuple[str, ...]) -> Dict[str, int]:
    """
    This function calculates the number of fruits in the fourth way.
    @param fruits: tuple of fruits
    @return: the result of the calculation containing pairs of the name of the fruit and its quantity
    """
    results = defaultdict(int)
    for item in fruits:
        results[item] += 1
    return dict(results)


if __name__ == '__main__':
    fruits_1 = ("Apple", "Apricot", "Apple", "Apricot", "Lemon", "Apple", "Apricot", "Lemon", "Avocado", "Banana")
    print(f"Fruit counts (first way): {count_fruits_0(fruits_1)}")
    print(f"Fruit counts (second way): {count_fruits_1(fruits_1)}")
    print(f"Fruit counts (third way): {count_fruits_2(fruits_1)}")
    print(f"Fruit counts (fourth way): {count_fruits_3(fruits_1)}")
