from tkinter import *
from tkinter import ttk
from colors import *
import random

# Creating the window
window = Tk()
window.title("Sorting Algorithms Visual")
window.maxsize(900, 500)
window.config(bg = white)

algorithm_name = StringVar()
user_algorithm = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]

# Fills the list with random numbers
def generate_data():
    global data

    data = []
    for i in range(0, 50):
        random_num = random.randint(1, 50)
        data.append(random_num)

    draw_data(data, [blue for i in range(len(data))])

# Displays the data on the screen
def draw_data(data, color_array):
    canvas.delete("all")

    width = 800
    canvas_height = 400

    x_width = width / (len(data) + 1)
    offset = 8
    spacing = 5
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill = color_array[i])

    window.update_idletasks()

# Function will call user's choice of sorting algorithm
def user_choice():
    global data

    if algorithm_menu.get() == "Bubble Sort":
        bubble_sort(data, draw_data)
    elif algorithm_menu.get() == "Selection Sort":
        selection_sort(data, draw_data)
    elif algorithm_menu.get() == "Insertion Sort":
        insertion_sort(data, draw_data)
    elif algorithm_menu.get() == "Merge Sort":
        merge_sort(data, draw_data)
    else:
        quick_sort(data, draw_data)

# Implementing bubble sort algorithm
def bubble_sort(data, draw_data):
    lst = data
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
                draw_data(data, [purple for i in range(len(data))])

# Implementing selection sort algorithm
def selection_sort(data, draw_data):
    lst = data
    for i in range(len(lst)-1, 0, -1):
        pos = 0
        for j in range(1, i+1):
            if lst[j] > lst[pos]:
                pos = j
        temp = lst[i]
        lst[i] = lst[pos]
        lst[pos] = temp
        draw_data(data, [dark_gray for i in range(len(data))])

# Implementing insertion sort algorithm
def insertion_sort(data, draw_data):
    lst = data
    for i in range(1, len(lst)):
        current = lst[i]
        position = i
        while position > 0 and lst[position - 1] > current:
            lst[position] = lst[position - 1]
            position = position - 1
        lst[position] = current
        draw_data(data, [dark_blue for i in range(len(data))])

# Implementing merge sort algorithm
def merge_sort(data, draw_data):
    lst = data
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half, draw_data)
        merge_sort(right_half, draw_data)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
        draw_data(data, [light_green for i in range(len(data))])

# Implementing quick sort algorithm and its helper functions
def quick_sort(data, draw_data):
    lst = data
    quick_sort_helper(lst, 0, len(lst) - 1)
    draw_data(data, [red for i in range(len(data))])


def quick_sort_helper(lst, first, last):
    if first < last:
        split_point = partition(lst, first, last)
        quick_sort_helper(lst, first, split_point - 1)
        quick_sort_helper(lst, split_point + 1, last)


def partition(lst, first, last):
    pivot_value = lst[first]
    left_mark = first + 1
    right_mark = last

    done = False

    while not done:
        while left_mark <= right_mark and lst[left_mark] <= pivot_value:
            left_mark += 1
        while lst[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            temp = lst[left_mark]
            lst[left_mark] = lst[right_mark]
            lst[right_mark] = temp

    temp = lst[first]
    lst[first] = lst[right_mark]
    lst[right_mark] = temp

    return right_mark

# User interface
ui_frame = Frame(window, width = 1000, height = 500, bg = white)
ui_frame.grid(row = 0, column = 0, padx = 0, pady = 0)

# Using combobox with grid to be able to select whichever algorithm it needs to run
algorithm_menu = ttk.Combobox(ui_frame, text = algorithm_name, values = user_algorithm)
algorithm_menu.grid(row = 0, column = 0, padx = 10, pady = 5)
# Setting bubble sort as default value
algorithm_menu.current(0)

# Generate the array
button_0 = Button(ui_frame, text = "Generate Array", command = generate_data, bg = blue)
button_0.grid(row = 0, column = 5, padx = 5, pady = 5)

# Sorting button
button_1 = Button(ui_frame, text = "Sort", command = user_choice, bg = blue)
button_1.grid(row = 0, column = 10, padx = 5, pady = 5)

# Canvas drawing array
canvas = Canvas(window, width = 800, height = 400, bg = white)
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)



window.mainloop()