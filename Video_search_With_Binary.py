def binary_search(video_titles, target):
    left, right = 0, len(video_titles) - 1
    while left <= right:
        mid = (left + right) // 2
        if video_titles[mid] == target:
            return mid
        elif video_titles[mid] < target:
            left = mid + 1
        else:
            right = mid + 1
    return -1