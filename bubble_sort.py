"""
Core Bubble Sort Algorithm Implementation

This module contains the pure algorithm without any UI dependencies.
Provides both basic sorting and step-by-step sorting for animation.

Time Complexity:
    - Best case: O(n) when list is already sorted (with early termination)
    - Average case: O(n²)
    - Worst case: O(n²) when list is reverse sorted

Space Complexity: O(1) - sorts in place
"""

from typing import List, Tuple, Generator, Dict, Any


def bubble_sort(numbers: List[int]) -> List[int]:
    """
    Sort a list of integers using the bubble sort algorithm with early termination.
    
    Algorithm: Repeatedly iterates through the list, comparing adjacent elements
    and swapping them if they are in the wrong order. After each pass, the largest
    unsorted element moves to its correct position. Includes early termination
    optimization - exits when a complete pass occurs with no swaps.
    
    Args:
        numbers: A list of integers to sort
    
    Returns:
        The sorted list of integers (sorted in place, also returned)
    
    Example:
        >>> bubble_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    # Outer loop - maximum n-1 passes needed
    for pass_num in range(len(numbers) - 1):
        swapped = False  # Track if any swaps occur in this pass
        
        # Inner loop - compare adjacent pairs
        for i in range(len(numbers) - 1):
            # Compare and swap if elements are out of order
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        
        # Early termination optimization: if no swaps occurred, list is sorted
        if not swapped:
            break
    
    return numbers


def bubble_sort_step_generator(numbers: List[int]) -> Generator[Tuple[List[int], Dict[str, Any]], None, None]:
    """
    Generator that yields step-by-step sorting state for visualization.
    
    Yields after each comparison, allowing visualizations to animate
    the sorting process frame-by-frame.
    
    Args:
        numbers: A list of integers to sort
    
    Yields:
        Tuple containing:
            - copy of numbers at current state
            - dict with keys: 'comparing_indices', 'swap_indices', 'pass_num', 
              'comparisons', 'swaps', 'is_complete'
    
    Example:
        >>> for state, stats in bubble_sort_step_generator([3, 1, 2]):
        ...     print(stats['comparisons'])
    """
    from copy import deepcopy
    
    n = len(numbers)
    numbers = deepcopy(numbers)
    comparisons = 0
    swaps = 0
    pass_num = 0
    
    for pass_num in range(n - 1):
        swapped = False
        
        for i in range(n - 1 - pass_num):
            comparisons += 1
            comparing_indices = (i, i + 1)
            swap_indices = ()
            
            yield (
                deepcopy(numbers),
                {
                    "comparing_indices": comparing_indices,
                    "swap_indices": (),
                    "pass_num": pass_num,
                    "comparisons": comparisons,
                    "swaps": swaps,
                    "is_complete": False,
                }
            )
            
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swaps += 1
                swapped = True
                swap_indices = (i, i + 1)
                
                yield (
                    deepcopy(numbers),
                    {
                        "comparing_indices": (),
                        "swap_indices": swap_indices,
                        "pass_num": pass_num,
                        "comparisons": comparisons,
                        "swaps": swaps,
                        "is_complete": False,
                    }
                )
        
        # Early termination check
        if not swapped:
            break
    
    # Final complete state
    yield (
        deepcopy(numbers),
        {
            "comparing_indices": (),
            "swap_indices": (),
            "pass_num": pass_num,
            "comparisons": comparisons,
            "swaps": swaps,
            "is_complete": True,
        }
    )
