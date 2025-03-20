import tkinter as tk
import time

def binary_search_visual(array, target):
    root = tk.Tk()
    root.title("Ikkilik(Binary) qidiruv")
    
    canvas_width = max(900, len(array) * 80)  # Adjust canvas width dynamically
    canvas_height = 400  # Increased height for better visualization
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()
    
    bar_width = 50
    bar_spacing = 20
    y_offset = 250  # Adjusted for centering vertically
    
    bars = []
    for i, num in enumerate(array):
        x1 = i * (bar_width + bar_spacing) + 50
        x2 = x1 + bar_width
        y1 = y_offset - num * 2
        y2 = y_offset
        bar = canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
        text = canvas.create_text((x1 + x2) / 2, y1 - 10, text=str(num), font=("Arial", 12))
        index_text = canvas.create_text((x1 + x2) / 2, y2 + 20, text=str(i), font=("Arial", 12))  # Show index below
        bars.append((bar, text, index_text))
    
    steps = []
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        steps.append((left, mid, right))
        if array[mid] == target:
            break
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    step_index = 0
    
    def update():
        nonlocal step_index
        if step_index >= len(steps):
            return
        left, mid, right = steps[step_index]
        step_index += 1
        
        for i in range(len(array)):
            canvas.itemconfig(bars[i][0], fill="blue")
        
        for i in range(0, left):
            canvas.itemconfig(bars[i][0], fill="gray")  # Left ignored part
        for i in range(right + 1, len(array)):
            canvas.itemconfig(bars[i][0], fill="gray")  # Right ignored part
        
        canvas.itemconfig(bars[mid][0], fill="yellow")  # Middle element
        
        if array[mid] == target:
            canvas.itemconfig(bars[mid][0], fill="green")  # Found target
    
    def prev_step():
        nonlocal step_index
        if step_index > 1:
            step_index -= 2  # Move back two steps to stay in sync
            update()
    
    next_button = tk.Button(root, text="Keyingi qadam", command=update)
    next_button.pack(side=tk.RIGHT)
    
    back_button = tk.Button(root, text="Oldingi qadam", command=prev_step)
    back_button.pack(side=tk.LEFT)
    
    root.mainloop()

# ishlashi
array = [19, 20, 21, 27, 31, 34, 51]
target = 21
binary_search_visual(array, target)