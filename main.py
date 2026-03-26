"""
Bubble Sort Visualizer - Main Entry Point

A comprehensive educational implementation of the Bubble Sort algorithm
with dual visualization modes: terminal-based ASCII animation and interactive
Pygame 2D graphics visualization.

Project Structure:
    - bubble_sort.py: Core algorithm (no UI dependencies)
    - ascii_viz.py: Terminal-based visualization
    - pygame_viz.py: Interactive 2D graphics visualization
    - cli.py: Command-line interface and menu system
    - main.py: Entry point (this file)

Usage:
    python main.py          # Start interactive menu
    
Educational Focus:
    - Learn bubble sort algorithm with real-time visualization
    - Choose between ASCII terminal or Pygame 2D graphics
    - Interactive controls: pause, reset, step through
    - Statistics tracking: passes, swaps, comparisons
"""

from cli import show_main_menu


if __name__ == "__main__":
    show_main_menu()

