def binary_search_no_edges(numbers, target):
  start = -1
  end = len(numbers)

  while start + 1 < end:
    distance = end - start
    mid = start + distance // 2

    if target == numbers[mid]:
      return mid
    elif target > numbers[mid]:
      start = mid
    elif target < numbers[mid]:
      end = mid

  return -1
