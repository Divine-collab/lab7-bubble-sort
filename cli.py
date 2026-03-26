"""
Command-Line Interface and Menu System

Handles user interaction, menu options, and demo runs.
Coordinates between different visualization modules.
"""

import sys
import time
from typing import List

from ascii_viz import bubble_sort_animated, clear_screen

try:
    from pygame_viz import visualize_bubble_sort
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False


def get_array_from_user(default: List[int]) -> List[int]:
    """
    Prompt user for a comma-separated list of numbers or use default.
    
    Args:
        default: Default array to use if user presses Enter
    
    Returns:
        List of integers from user or default
    """
    user_input = input("\nEnter numbers separated by spaces (or press Enter for default): ").strip()
    
    if user_input:
        try:
            return [int(x) for x in user_input.split()]
        except ValueError:
            print("Invalid input! Using default array.")
            return default
    
    return default


def show_main_menu() -> None:
    """Display the main menu and handle user choice."""
    print("=" * 60)
    print("BUBBLE SORT VISUALIZER")
    print("=" * 60)
    
    while True:
        print("\nChoose a visualization mode:")
        print("1. ASCII Bar Animation (Terminal)")
        print("2. Pygame 2D Graphics Visualization" + (" (Recommended)" if PYGAME_AVAILABLE else " (Not installed)"))
        print("3. Run ASCII Animation Demo")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            _run_ascii_mode()
        elif choice == "2":
            _run_pygame_mode()
        elif choice == "3":
            run_ascii_demo()
        elif choice == "4":
            print("\nGoodbye!")
            sys.exit(0)
        else:
            print("Invalid choice! Please enter 1-4.")


def _run_ascii_mode() -> None:
    """Run ASCII bar animation mode."""
    default_array = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    test_array = get_array_from_user(default_array)
    
    print(f"\nOriginal: {test_array}")
    print("\nStarting ASCII animation (use delay parameter to adjust speed)...\n")
    bubble_sort_animated(test_array, delay=0.1)


def _run_pygame_mode() -> None:
    """Run Pygame 2D graphics visualization mode."""
    if not PYGAME_AVAILABLE:
        print("\n❌ Pygame is not installed. Please run: pip install pygame")
        return
    
    default_array = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 32, 12, 67, 89, 23]
    test_array = get_array_from_user(default_array)
    
    print(f"\nOriginal: {test_array}")
    print("Launching Pygame visualization...")
    print("Controls: SPACE=Pause, R=Reset, ENTER=Step (when paused)\n")
    visualize_bubble_sort(test_array)


def run_ascii_demo() -> None:
    """Run the ASCII animation demonstration with multiple test cases."""
    print("=" * 60)
    print("BUBBLE SORT - IN-PLACE ASCII BAR ANIMATION")
    print("=" * 60)
    
    # Test 1: Small list demonstration
    print("\n[Test 1] Small List (Fast Animation)")
    print("Original: [5, 2, 8, 1]")
    test_1 = [5, 2, 8, 1]
    time.sleep(1)
    bubble_sort_animated(test_1, delay=0.3)
    time.sleep(2)
    
    # Test 2: Standard list demonstration
    print("\n[Test 2] Standard List (Medium Animation)")
    print("Original: [64, 34, 25, 12, 22, 11, 90]")
    test_2 = [64, 34, 25, 12, 22, 11, 90]
    time.sleep(1)
    bubble_sort_animated(test_2, delay=0.1)
    time.sleep(2)
    
    # Test 3: Already sorted list (early termination)
    print("\n[Test 3] Already Sorted List (Early Termination)")
    print("Original: [1, 2, 3, 4, 5]")
    test_3 = [1, 2, 3, 4, 5]
    time.sleep(1)
    bubble_sort_animated(test_3, delay=0.3)
    time.sleep(2)
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETE!")
    print("=" * 60)
