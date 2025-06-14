from flask import Flask, jsonify, request, render_template  # Added render_template
import random

app = Flask(__name__)

# BubbleSort class as provided by you
class Bubble_Sort():
    def __init__(self):
        self.list = []

    def add_data(self, data):
        self.list.append(data)

    def bubble_sort(self):
        for i in range(len(self.list)-1):
            for j in range(len(self.list)):
                if j == (len(self.list)-1):
                    continue
                elif self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
        return self.list

# Initialize a global instance of BubbleSort
bubble_sort_instance = Bubble_Sort()

@app.route('/bubble')
def bubble():
    return render_template('bubble.html', show_welcome=True)

@app.route('/get_list', methods=['GET'])
def get_list():
    return jsonify(bubble_sort_instance.list)

@app.route('/randomize', methods=['POST'])
def randomize():
    # Get the parameters from the request
    data = request.json
    num_rectangles = data.get('num_rectangles', 10)
    min_value = data.get('min_value', 1)
    max_value = data.get('max_value', 20)
    
    # Generate the new list
    bubble_sort_instance.list = [random.randint(min_value, max_value) for _ in range(num_rectangles)]
    return jsonify(bubble_sort_instance.list)

@app.route('/sort', methods=['POST'])
def sort():
    sorted_list = bubble_sort_instance.bubble_sort()
    return jsonify(sorted_list)
