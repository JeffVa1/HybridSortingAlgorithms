"""
Author - Jeffrey Valentic
Hybrid Sorting
"""
from typing import List, Any, Dict


def hybrid_sort(data: List[Any], threshold: int) -> None:
    """
    Calls merge_sort with a threshold.
    """
    merge_sort(data, threshold)


def inversions_count(data: List[Any]) -> int:
    """
    calls merge_sort to sort data and returns inversion count.
    """
    return merge_sort(data)


def merge_sort(data: List[Any], threshold: int = 0) -> int:
    """
    Sorts data using a hybrid of merge sort and insertion sort.
    Inputs: Data, threshold
    Output: Inversion Count
    NOTE:   While the size of sublists are greater than the threshold, mergesort will be used.
            While the size of sublists are less than or equal to threshold, insertion sort will be used.
    """

    def merge(lst1: List[Any], lst2: List[Any], mid) -> int:
        l_ind = 0
        r_ind = 0
        combined = []
        inversion_count = 0
        while l_ind < len(lst1) and r_ind < len(lst2):
            if lst1[l_ind] <= lst2[r_ind]:
                combined.append(lst1[l_ind])
                l_ind += 1
            else:
                combined.append(lst2[r_ind])
                inversion_count += mid - l_ind
                r_ind += 1

        while l_ind < len(lst1):
            combined.append(lst1[l_ind])
            l_ind += 1
        while r_ind < len(lst2):
            combined.append(lst2[r_ind])
            r_ind += 1

        for ind in range(len(combined)):
            data[ind] = combined[ind]

        return inversion_count

    #START OF MERGE SORT
    inversions = 0
    if len(data) > 1:
        split_ind = int(len(data) / 2)
        left = data[:split_ind]
        right = data[split_ind:]

        if len(left) <= threshold:
            insertion_sort(left)
        if len(right) <= threshold:
            insertion_sort(right)

        if len(left) > threshold:
            inversions += merge_sort(left, threshold)
        if len(right) > threshold:
            inversions += merge_sort(right, threshold)

        inversions += merge(left, right, split_ind)

    if threshold > 0:
        return 0
    else:
        return inversions

def insertion_sort(data: List[Any]) -> None:
    """
    Uses insertion sort algorithm to sort the input (Data)
    """
    for i in range(1, len(data)):
        cur_val = data[i]
        prev_ind = i-1
        while cur_val < data[prev_ind] and prev_ind >= 0:
            data[prev_ind+1] = data[prev_ind]
            prev_ind -= 1

        data[prev_ind+1] = cur_val

def find_match(user_interests: List[str], candidate_interests: Dict[str, List]) -> str:
    """
    Finds candidate with least amount of inversions to match interests with user
    INPUTS: user_interests (lst), candidate_interests (Dict[str, List])
    OUTPUT: Str, name of matched user.
    """
    best_match = ("nobody", 100000000)
    for k in candidate_interests:
        candidate_num_lst = [user_interests.index(candidate_interests[k][i]) for i in range(len(candidate_interests[k]))]
        cur_diff = inversions_count(candidate_num_lst)
        if cur_diff < best_match[1]:
            best_match = (k, cur_diff)

    return best_match[0]
