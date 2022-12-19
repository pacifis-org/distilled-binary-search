def binary_search_recursion(numbers, target, start, end):
  if start >= end:
    return -1

  distance = end - start
  mid = start + distance // 2

  if target == numbers[mid]:
    return mid
  elif target > numbers[mid]:
    return binary_search_recursion(numbers, target, mid + 1, end)
  elif target < numbers[mid]:
    return binary_search_recursion(numbers, target, start, mid)

def binary_search(numbers, target):
  return binary_search_recursion(numbers, target, 0, len(numbers))
