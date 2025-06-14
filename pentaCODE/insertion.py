from flask import Flask, jsonify, request, render_template  # Added render_template
import random

class Insertion_Sorting:
    def __init__(self):
        self.list = []

    def add_data(self, data):
        self.list.append(data)
    
    def insertion_sort(self):
        steps = []  # Store steps for the frontend
        current_value = self.list[0]
        for i in range(0, len(self.list)):
            if current_value == self.list[0]:
                current_value = self.list[i + 1]
                continue
            while current_value < self.list[self.list.index(current_value) - 1]:
                if self.list[self.list.index(current_value)] <= self.list[self.list.index(current_value) - 1]:
                    steps.append((list(self.list), f"Swapped {self.list[self.list.index(current_value)]} and {self.list[self.list.index(current_value)-1]}"))
                    y = self.list.index(current_value) - 1
                    if y == -1:
                        y = 0
                        break
                    self.list[self.list.index(current_value)], self.list[y] = self.list[y], self.list[self.list.index(current_value)]
                    y = 0        
            if i + 1 != len(self.list):
                current_value = self.list[i + 1]
        steps.append((list(self.list), "Sorting complete!"))
        return steps
    

