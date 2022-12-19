def binary_search_both_edges(numbers, target):
  start = 0
  end = len(numbers) - 1

  while start <= end:
    distance = end - start
    mid = start + distance // 2

    if target == numbers[mid]:
      return mid
    elif target > numbers[mid]:
      start = mid + 1
    elif target < numbers[mid]:
      end = mid - 1

  return -1
