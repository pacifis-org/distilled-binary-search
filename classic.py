def binary_search(numbers, target):
  start = 0
  end = len(numbers)
	
  while start < end:
    distance = end - start
    mid = start + distance // 2

    if target == numbers[mid]:
      return mid
    elif target > numbers[mid]:
      start = mid + 1
    elif target < numbers[mid]:
      end = mid

  return -1
