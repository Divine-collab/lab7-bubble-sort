"""
ASCII Terminal Visualization Module

Provides terminal-based visualizations for bubble sort animation.
Handles screen clearing, progress bars, and formatted output.
"""

import time
import os
from typing import List

from bubble_sort import bubble_sort


def clear_screen() -> None:
    """
    Clear the terminal screen for in-place animation.
    
    Uses the 'clear' command for macOS/Linux systems and ANSI escape codes
    to move cursor to home position. This allows for in-place animation where
    the display updates at the same location rather than scrolling.
    """
    os.system('clear')
    # ANSI escape sequence: \033[H moves cursor to home (top-left)
    print('\033[H', end='')


def create_ascii_bar(numbers: List[int], sorted_count: int) -> str:
    """
    Create an ASCII bar visualization showing sorting progress.
    
    Displays a progress bar showing which elements are in their final sorted
    positions. Uses filled (█) and empty (░) Unicode block characters.
    
    Args:
        numbers: The list being sorted
        sorted_count: Number of elements that are in their final positions
    
    Returns:
        A formatted string with the progress bar and percentage
        
    Example:
        >>> create_ascii_bar([3, 1, 4, 1, 5], 2)
        'Progress: |██████░░░░░░░░░░░░░░░░░░░░░░| 40% sorted'
    """
    total = len(numbers)
    
    # Handle edge case of empty list
    if total == 0:
        return "Progress: |░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0% sorted"
    
    # Calculate percentage of sorted elements
    percent = int((sorted_count / total) * 100)
    
    # Create visual bar (30 characters total)
    bar_length = 30
    filled_length = int(bar_length * (sorted_count / total))
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    
    return f"Progress: |{bar}| {percent}% sorted"


def display_list(numbers: List[int]) -> None:
    """
    Print the list in a readable format.
    
    Args:
        numbers: A list of integers to display
    """
    print(", ".join(str(num) for num in numbers))


def bubble_sort_animated(numbers: List[int], delay: float = 0.15) -> List[int]:
    """
    Sort a list using bubble sort with real-time in-place ASCII bar animation.
    
    Performs bubble sort while clearing and redrawing the screen at each swap,
    creating the visual effect of an animated progress bar. Displays:
    - Current pass number
    - Running count of swaps and comparisons
    - Current state of the array
    - ASCII progress bar showing percentage of sorted elements
    
    The animation updates in-place (same screen location) rather than scrolling,
    providing a clean visualization of the sorting process.
    
    Args:
        numbers: A list of integers to sort
        delay: Time in seconds to pause between screen updates (default 0.15)
    
    Returns:
        The sorted list of integers
        
    Note:
        Early termination optimization: If a complete pass through the list
        occurs with no swaps, the sorting is complete and the function exits,
        improving performance for nearly-sorted lists.
    """
    n = len(numbers)
    swaps = 0
    comparisons = 0
    
    for pass_num in range(n - 1):
        swapped_in_pass = False
        # After each pass, one more element is guaranteed to be in final position
        sorted_count = pass_num
        
        for i in range(n - 1 - pass_num):
            comparisons += 1
            
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swaps += 1
                swapped_in_pass = True
                
                # Update sorted count: elements at the end are locked in place
                sorted_count = pass_num + 1
                
                # Display animation frame
                clear_screen()
                print(f"Pass: {pass_num + 1} | Swaps: {swaps} | Comparisons: {comparisons}")
                print(f"Current array: {numbers}")
                print(create_ascii_bar(numbers, sorted_count))
                time.sleep(delay)
        
        # Early termination: if no swaps in this pass, list is sorted
        if not swapped_in_pass:
            clear_screen()
            print(f"✓ SORT COMPLETE!")
            print(f"Final array: {numbers}")
            print(f"Total Swaps: {swaps} | Total Comparisons: {comparisons}")
            print(create_ascii_bar(numbers, n))
            return numbers
    
    # Display final sorted state
    clear_screen()
    print(f"✓ SORT COMPLETE!")
    print(f"Final array: {numbers}")
    print(f"Total Swaps: {swaps} | Total Comparisons: {comparisons}")
    print(create_ascii_bar(numbers, n))
    return numbers
