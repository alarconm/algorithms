
def binary_search(el, list, start=0, end=None):

    if end is None:
        end = len(list) - 1
    if start > end:
        return False

    midpoint = (start + end)//2

    if list[midpoint] == el:
        return midpoint

    elif el < list[midpoint]:
        end = midpoint - 1
        return binary_search(el, list, start, end)

    elif el > list[midpoint]:
        start = midpoint + 1
        return binary_search(el, list, start, end)