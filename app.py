from flask import Flask, request, jsonify

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

def binary_search(video_titles, target):
    left, right = 0, len(video_titles) - 1
    while left <= right:
        mid = (left + right) // 2
        if video_titles[mid] == target:
            return mid
        elif video_titles[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def merge_sort(video_titles):
    if len(video_titles) > 1:
        mid = len(video_titles) // 2
        left_half = video_titles[:mid]
        right_half = video_titles[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                video_titles[k] = left_half[i]
                i += 1
            else:
                video_titles[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            video_titles[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            video_titles[k] = right_half[j]
            j += 1
            k += 1

@app.route('/search', methods=['GET'])
def search_videos():
    query = request.args.get('title')
    if query is None:
        return jsonify({"error": "No title provided"}), 400

    index = binary_search(video_titles, query)
    if index != -1:
        return jsonify({"title": video_titles[index]}), 200
    else:
        return jsonify({"message": "Video not found"}), 404

@app.route('/sort', methods=['GET'])
def sort_videos():
    global video_titles
    sorted_videos = video_titles[:]
    merge_sort(sorted_videos)
    return jsonify({"sorted_titles": sorted_videos}), 200

if __name__ == '__main__':
    app.run(debug=True)
