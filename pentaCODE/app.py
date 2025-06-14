from flask import Flask, request, render_template, jsonify
from LinkList import Linked
from Stack import Stack, shunting_yard_with_steps
from Queue import Queue, Deque
from binarytree import BinaryTree
from Graph import Graph
from bubble import Bubble_Sort
from insertion import Insertion_Sorting
from selection import Selection_Sorting
from merge import Merge_Sorting
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', show_welcome=True, route_name='main')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Manage Movie Watchlist
movie_list = Linked()


@app.route('/movies')
def movies():
    return render_template('linklistindex.html')


@app.route('/add_beginning', methods=['POST'])
def add_beginning():
    movie = request.form['movie']
    if movie_list.search(movie):
        return jsonify({"error": "This movie already exists in the list.", "movies": movie_list.printLinkedList()}), 400
    movie_list.insert_at_beginning(movie)
    return jsonify({"movies": movie_list.printLinkedList()})

@app.route('/add_end', methods=['POST'])
def add_end():
    movie = request.form['movie']
    if movie_list.search(movie):
        return jsonify({"error": "This movie already exists in the list.", "movies": movie_list.printLinkedList()}), 400
    movie_list.insert_at_end(movie)
    return jsonify({"movies": movie_list.printLinkedList()})

@app.route('/remove_beginning', methods=['POST'])
def remove_beginning():
    if not movie_list.printLinkedList():
        return jsonify({"error": "Cannot remove from beginning. The list is empty.", "movies": []}), 400
    removed = movie_list.remove_beginning()
    return jsonify({"removed": removed, "movies": movie_list.printLinkedList()})

@app.route('/remove_end', methods=['POST'])
def remove_end():
    if not movie_list.printLinkedList():
        return jsonify({"error": "Cannot remove from end. The list is empty.", "movies": []}), 400
    removed = movie_list.remove_at_end()
    return jsonify({"removed": removed, "movies": movie_list.printLinkedList()})

@app.route('/remove_movie', methods=['POST'])
def remove_movie():
    movie = request.form['movie']
    if not movie_list.search(movie):
        return jsonify({"error": "Movie not found in the list.", "movies": movie_list.printLinkedList()}), 404
    removed = movie_list.remove_at(movie)
    return jsonify({"removed": removed, "movies": movie_list.printLinkedList()})

@app.route('/search_movie', methods=['POST'])
def search_movie():
    movie = request.form['movie']
    found = movie_list.search(movie)
    return jsonify({"found": found})


# Shunting Yard Algorithm
stack = Stack()

# Stack Operations
@app.route('/stack')
def stack_page():
    return render_template('stackindex.html')

@app.route('/convert_postfix', methods=['POST'])
def convert_postfix():
    expression = request.form.get('expression')
    if not expression:
        return jsonify({"error": "No expression provided."}), 400
    try:
        postfix, steps = shunting_yard_with_steps(expression)
        return jsonify({"postfix": postfix, "steps": steps})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

#Queue

# Initialize data structures
queue = Queue()
deque = Deque()

# API Endpoints

@app.route('/queuedequeue')
def queuedequeue():
    return render_template('queue.html')

@app.route('/queue/enqueue', methods=['POST'])
def enqueue():
    data = request.json
    item = data.get("item")
    queue.enqueue(item)
    return jsonify({"message": f"Enqueued {item}", "queue": queue.queue})

@app.route('/queue/dequeue', methods=['POST'])
def dequeue():
    item = queue.dequeue()
    return jsonify({"dequeued": item, "queue": queue.queue})

@app.route('/queue/size', methods=['GET'])
def queue_size():
    return jsonify({"queue": queue.queue})

@app.route('/deque/size', methods=['GET'])
def deque_size():
    return jsonify({"deque": deque.items})


@app.route('/deque/add_left', methods=['POST'])
def add_left():
    data = request.json
    item = data.get("item")
    deque.add_left(item)
    return jsonify({"message": f"Added {item} to the left", "deque": deque.items})

@app.route('/deque/add_right', methods=['POST'])
def add_right():
    data = request.json
    item = data.get("item")
    deque.add_right(item)
    return jsonify({"message": f"Added {item} to the right", "deque": deque.items})

@app.route('/deque/remove_left', methods=['POST'])
def remove_left():
    item = deque.remove_left()
    return jsonify({"removed_left": item, "deque": deque.items})

@app.route('/deque/remove_right', methods=['POST'])
def remove_right():
    item = deque.remove_right()
    return jsonify({"removed_right": item, "deque": deque.items})




# Binary Tree
binary_tree = BinaryTree(10)

@app.route('/binary')
def binary():
    return render_template('binary.html')

@app.route('/insert_left', methods=['POST'])
def insert_left():
    data = request.json
    current_value = data.get('current_value')
    new_value = data.get('new_value')
    
    # Find the current node
    current_node = binary_tree.search(binary_tree.root, current_value)
    if current_node:
        binary_tree.insert_left(current_node, new_value)
        return jsonify({"message": f"Inserted {new_value} to the left of {current_value}"}), 200
    else:
        return jsonify({"message": "Node not found"}), 404

@app.route('/insert_right', methods=['POST'])
def insert_right():
    data = request.json
    current_value = data.get('current_value')
    new_value = data.get('new_value')
    
    # Find the current node
    current_node = binary_tree.search(binary_tree.root, current_value)
    if current_node:
        binary_tree.insert_right(current_node, new_value)
        return jsonify({"message": f"Inserted {new_value} to the right of {current_value}"}), 200
    else:
        return jsonify({"message": "Node not found"}), 404

@app.route('/delete_node', methods=['POST'])
def delete_node():
    data = request.json
    key = data.get('key')
    
    # Perform deletion
    binary_tree.root = binary_tree.delete_node(binary_tree.root, key)
    return jsonify({"message": f"Node with value {key} deleted."}), 200

@app.route('/inorder_traversal', methods=['GET'])
def inorder_traversal():
    result = binary_tree.inorder_traversal(binary_tree.root, "")
    return jsonify({"inorder_traversal": result.strip('-')}), 200

@app.route('/evaluate_expression', methods=['POST'])
def evaluate_expression():
    data = request.json
    expression = data.get('expression')  # Expecting a list like ["4", "5", "+", "7", "3", "-", "*"]
    
    # Create expression tree
    binary_tree.create_expression_tree(expression)
    
    # Evaluate the expression tree
    result = binary_tree.evaluate_expression(binary_tree.root)
    
    return jsonify({"result": result}), 200





# Create the train graph
train_graph = Graph()


@app.route('/graph')
def index():
    return render_template('graphindex.html', stations=list(train_graph.vertices.keys()))

@app.route('/shortest_path', methods=['POST'])
def shortest_path():
    data = request.json
    start = data.get('start')
    end = data.get('end')

    if start and end:
        path, distance, edges_in_path = train_graph.get_shortest_path(start, end)
        if path is None:
            return jsonify({"error": "No valid route exists between these stations."}), 404

        # Now, highlight the edges only if both vertices are in the shortest path
        highlighted_edges = []
        for edge in edges_in_path:
            if edge[0] in path and edge[1] in path:
                highlighted_edges.append(edge)

        return jsonify({
            "path": path,
            "distance": f"{distance:.2f}",
            "highlighted_edges": highlighted_edges
        })
    
    return jsonify({"error": "Invalid input."}), 400



# Add edges with weights (LRT 1)
train_graph.add_edge("Fernando Poe Jr.", "Balintawak", 1.870)
train_graph.add_edge("Balintawak", "Monumento", 2.250)
train_graph.add_edge("Monumento", "5th Avenue", 1.087)
train_graph.add_edge("5th Avenue", "R. Papa", 0.954)
train_graph.add_edge("R. Papa", "Abad Santos", 0.660)
train_graph.add_edge("Abad Santos", "Blumentritt", 0.927)
train_graph.add_edge("Blumentritt", "Tayuman", 0.671)
train_graph.add_edge("Tayuman", "Bambang", 0.618)
train_graph.add_edge("Bambang", "Doroteo Jose", 0.648)
train_graph.add_edge("Doroteo Jose", "Carriedo", 0.685)
train_graph.add_edge("Carriedo", "Central Terminal", 0.725)
train_graph.add_edge("Central Terminal", "United Nations", 1.214)
train_graph.add_edge("United Nations", "Pedro Gil", 0.754)
train_graph.add_edge("Pedro Gil", "Quirino", 0.794)
train_graph.add_edge("Quirino", "Vito Cruz", 0.827)
train_graph.add_edge("Vito Cruz", "Gil Puyat", 1.061)
train_graph.add_edge("Gil Puyat", "Libertad", 0.730)
train_graph.add_edge("Libertad", "EDSA", 1.010)
train_graph.add_edge("EDSA", "Baclaran", 0.588)
train_graph.add_edge("Baclaran", "Redemptorist-Aseana", 0.869)
train_graph.add_edge("Redemptorist-Aseana", "MIA Road", 1.303)
train_graph.add_edge("MIA Road", "PITX", 1.141)
train_graph.add_edge("PITX", "Ninoy Aquino Avenue", 1.393)
train_graph.add_edge("Ninoy Aquino Avenue", "Dr. Santos", 1.646)


# LRT 2
train_graph.add_edge("Antipolo", "Marikina–Pasig", 2.232)
train_graph.add_edge("Marikina–Pasig", "Santolan", 1.795)
train_graph.add_edge("Santolan", "Katipunan", 1.970)
train_graph.add_edge("Katipunan", "Anonas", 0.955)
train_graph.add_edge("Anonas", "Araneta Center–Cubao(LRT)", 1.438)
train_graph.add_edge("Araneta Center–Cubao(LRT)", "Betty Go-Belmonte", 1.164)
train_graph.add_edge("Betty Go-Belmonte", "Gilmore", 1.075)
train_graph.add_edge("Gilmore", "J. Ruiz", 0.928)
train_graph.add_edge("J. Ruiz", "V. Mapa", 1.234)
train_graph.add_edge("V. Mapa", "Pureza", 1.357)
train_graph.add_edge("Pureza", "Legarda", 1.389)
train_graph.add_edge("Legarda", "Recto", 1.050)
train_graph.add_edge("Recto", "Doroteo Jose", 0.030)

# LRT 3 (MRT Line)
train_graph.add_edge("North Avenue", "Quezon Avenue", 1.200)
train_graph.add_edge("Quezon Avenue", "GMA–Kamuning", 1.000)
train_graph.add_edge("GMA–Kamuning", "Araneta Center–Cubao(MRT)", 1.900)
train_graph.add_edge("Araneta Center–Cubao(MRT)", "Santolan–Annapolis", 1.500)
train_graph.add_edge("Santolan–Annapolis", "Ortigas", 2.300)
train_graph.add_edge("Ortigas", "Shaw Boulevard", 0.800)
train_graph.add_edge("Shaw Boulevard", "Boni", 1.000)
train_graph.add_edge("Boni", "Guadalupe", 0.800)
train_graph.add_edge("Guadalupe", "Buendia", 2.000)
train_graph.add_edge("Buendia", "Ayala", 0.950)
train_graph.add_edge("Ayala", "Magallanes", 1.200)
train_graph.add_edge("Magallanes", "Taft Avenue", 2.050)

# Transfer points
train_graph.add_edge("Doroteo Jose", "Recto", 0.030)
train_graph.add_edge("Araneta Center–Cubao(LRT)", "Araneta Center–Cubao(MRT)", 0.050)


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



# Selection
selection_sort_instance = Selection_Sorting()

@app.route("/selection")
def selection():
    return render_template('selection.html', show_welcome=True)

@app.route("/get_selection_list", methods=["GET"])
def get_selection_list():
    return jsonify(selection_sort_instance.get_list())

@app.route("/randomize_selection", methods=["POST"])
def randomize_selection():
    data = request.get_json()
    num_rectangles = data.get("num_rectangles", 10)
    min_value = data.get("min_value", 1)
    max_value = data.get("max_value", 20)
    
    random_list = [random.randint(min_value, max_value) for _ in range(num_rectangles)]
    selection_sort_instance.list = random_list
    
    return jsonify(random_list)

@app.route("/sort_selection", methods=["POST"])
def sort_selection():
    selection_sort_instance.selection_sort()
    return jsonify(selection_sort_instance.get_list())


# Insertion 
insertion_sort_instance = Insertion_Sorting()

@app.route('/insertion')
def insertion():
    return render_template('insertion.html', show_welcome=True)

@app.route('/get_insertion_list', methods=['GET'])
def get_insertion_list():
    return jsonify(insertion_sort_instance.list)

@app.route('/randomize_insertion', methods=['POST'])
def randomize_insertion():
    # Get the parameters from the request
    data = request.json
    num_rectangles = data.get('num_rectangles', 10)
    min_value = data.get('min_value', 1)
    max_value = data.get('max_value', 20)
    
    # Generate the new list for Insertion Sort
    insertion_sort_instance.list = [random.randint(min_value, max_value) for _ in range(num_rectangles)]
    return jsonify(insertion_sort_instance.list)

@app.route('/sort_insertion', methods=['POST'])
def sort_insertion():
    # Perform Insertion Sort
    sorted_list = insertion_sort_instance.insertion_sort()
    return jsonify(sorted_list)




# Merge
# Initialize a global instance of Merge_Sorting
merge_sort_instance = Merge_Sorting()

@app.route('/merge')
def merge():
    return render_template('merge.html', show_welcome=True)

@app.route('/get_merge_list', methods=['GET'])
def get_merge_list():
    return jsonify(merge_sort_instance.list)

@app.route('/randomize_merge', methods=['POST'])
def randomize_merge():
    data = request.json
    num_rectangles = data.get('num_rectangles', 10)
    min_value = data.get('min_value', 1)
    max_value = data.get('max_value', 20)
    
    merge_sort_instance.list = [random.randint(min_value, max_value) for _ in range(num_rectangles)]
    merge_sort_instance.steps = []  # Reset steps on randomization
    return jsonify(merge_sort_instance.list)

@app.route('/sort_merge', methods=['POST'])
def sort_merge():
    merge_sort_instance.steps = []  # Clear previous steps
    merge_sort_instance.merge_sort()  # Start the merge sort (in place)
    return jsonify(merge_sort_instance.list)  # Return the final sorted list

@app.route('/get_merge_steps', methods=['GET'])
def get_merge_steps():
    return jsonify(merge_sort_instance.steps)



if __name__ == '__main__':
    app.run(debug=True)

