# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 06:57:27 2025

@author: Odiljon
"""

import matplotlib.pyplot as plt
import numpy as np
import time
from IPython.display import display, clear_output

def linear_search_visual(array, target):
    fig, ax = plt.subplots()
    ax.set_title("Chiziqli qidiruv")
    
    for i in range(len(array)):
        clear_output(wait=True)
        bars = ax.bar(range(len(array)), array, color=["red" if j == i else "blue" for j in range(len(array))])
        display(fig)
        time.sleep(0.5)
        
        if array[i] == target:
            bars[i].set_color("green")
            clear_output(wait=True)
            display(fig)
            print(f"{target} element {i} indeksda topildi")
            return i
    
    print(f"{target} element topilmadi")
    return -1

# ishlashi
array = [20, 32, 58, 27, 19, 21, 5]
target = 27
linear_search_visual(array, target)
