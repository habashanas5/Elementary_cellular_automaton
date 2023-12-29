import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

def initialize_automaton(dim):
    a = np.zeros(shape=dim)
    a[dim // 2] = 1
    return a

def update_state(a, rules):
    dim = len(a)
    n = np.zeros(shape=dim)
    for i in range(1, dim - 1):
        r = a[i - 1] * 4 + a[i] * 2 + a[i + 1]
        n[i] = rules[r]
    return n

def display_automaton(automaton):
    s = ["#" if cell == 1 else " " for cell in automaton]
    print("".join(s))

def visualize_evolution(screen):
    sn.heatmap(screen)
    plt.show()
#10000001
def automation_elementary():
    dim = 100
    Rules = {0: 0,  # 000
             1: 1,  # 001
             2: 1,  # 010
             3: 0,  # 011
             4: 1,  # 100
             5: 0,  # 101
             6: 1,  # 110
             7: 0,  # 111
             }
    automaton = initialize_automaton(dim)
    screen = [automaton.copy()]

    for t in range(50):
        automaton = update_state(automaton, Rules)
        display_automaton(automaton)
        screen.append(automaton.copy())

    visualize_evolution(screen)

automation_elementary()