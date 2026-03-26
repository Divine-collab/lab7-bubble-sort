# Bubble Sort Visualizer

A comprehensive educational implementation of the **Bubble Sort algorithm** in Python with **dual visualization modes**: terminal-based ASCII animation and interactive **Pygame 2D graphics** visualization. Perfect for learning sorting algorithms with real-time visual feedback.

## 🎯 Project Overview

Bubble Sort is a foundational sorting algorithm that repeatedly steps through a list, compares adjacent elements, and swaps them if they are in the wrong order. This project provides:

- ✅ **Core Algorithm**: Optimized bubble sort with early termination
- ✅ **ASCII Terminal Animation**: Real-time progress visualization in the terminal
- ✅ **Pygame 2D Graphics**: Beautiful interactive bar chart visualization (60 FPS)
- ✅ **Comprehensive Testing**: 5 unit tests covering all scenarios
- ✅ **Interactive Menu**: Choose your visualization mode at runtime
- ✅ **Educational Focus**: Detailed documentation with complexity analysis

## 📊 Algorithm Explanation

### How Bubble Sort Works

1. **Pass Through the List**: Compare each pair of adjacent elements
2. **Swap if Needed**: If the left element is greater than the right element, swap them
3. **Bubble Effect**: Larger elements "bubble up" to the end of the list with each pass
4. **Repeat**: After each pass, the largest unsorted element is in its correct position
5. **Optimize**: Stop early if no swaps occur in a pass (list is already sorted)

### Complexity Analysis

| Scenario | Time Complexity | Space Complexity |
|----------|-----------------|------------------|
| **Best Case** (already sorted) | O(n) with early termination | O(1) |
| **Average Case** (random list) | O(n²) | O(1) |
| **Worst Case** (reverse sorted) | O(n²) | O(1) |
| **Space** (in-place sorting) | — | O(1) |

**Key Insight**: Early termination optimization makes bubble sort efficient for nearly-sorted lists, reducing best-case complexity from O(n²) to O(n).

## 📁 Project Structure

```
lab7-bubble-sort/
├── main.py                 # Core algorithm + interactive menu system
├── pygame_viz.py           # Pygame 2D graphics visualization module
├── test_bubble_sort.py     # Comprehensive unit test suite (5 tests)
├── requirements.txt        # Project dependencies
├── README.md               # This file
├── JOURNAL.md              # Development log (chronological)
└── REPORT.md               # Project report
```

## 🚀 Quick Start

### Installation

**Step 1: Clone or download the project**

```bash
cd lab7-bubble-sort
```

**Step 2: Install dependencies (optional but recommended)**

```bash
pip install -r requirements.txt
```

This installs Pygame for the 2D graphics visualization. Core functionality works without it.

### Running the Project

```bash
python3 main.py
```

This launches an **interactive menu** where you can choose:

```
BUBBLE SORT VISUALIZER

Choose a visualization mode:
1. ASCII Bar Animation (Terminal)
2. Pygame 2D Graphics Visualization (Recommended)
3. Run ASCII Animation Demo
4. Exit
```

### Running Tests

```bash
python3 test_bubble_sort.py
```

Expected output:
```
test_already_sorted_list ... ok
test_edge_cases ... ok
test_list_with_duplicates ... ok
test_random_unsorted_list ... ok
test_reverse_sorted_list ... ok

Ran 5 tests in 0.000s
OK
```

## 🎨 Visualization Modes

### Mode 1: ASCII Bar Animation (Terminal)

**Best for**: Learning without graphics, presentations, terminal-only environments

**Features**:
- Real-time in-place terminal animation
- Unicode progress bar (█ for filled, ░ for empty)
- Live statistics: pass count, swap count, comparison count
- Current array state display
- Fast, lightweight, no external dependencies

**Example Output**:
```
BUBBLE SORT - IN-PLACE ASCII BAR ANIMATION
Pass: 1 | Swaps: 2 | Comparisons: 3
Current array: [2, 5, 8, 1]
Progress: |████░░░░░░░░░░░░░░░░░░░░░░░░| 25% sorted
```

**How to Use**:
- Select option 1 from main menu
- Enter array (or press Enter for default)
- Watch the animation!

### Mode 2: Pygame 2D Graphics ⭐ RECOMMENDED

**Best for**: Interactive learning, presentations, visualizing larger arrays

**Features**:
- 60 FPS smooth real-time animation
- Color-coded bar visualization:
  - 🔵 **Blue**: Normal unsorted elements
  - 🔴 **Red**: Currently comparing elements
  - 🟢 **Green**: Recently swapped elements (highlight)
  - 🔵 **Light Blue**: Elements in final sorted positions
- Interactive controls:
  - **SPACE**: Pause/Resume sorting
  - **R**: Reset to original array
  - **ENTER**: Step through one comparison (when paused)
  - Close window: Exit
- Statistics overlay showing:
  - Current pass number
  - Total swaps count
  - Total comparisons count
  - Sorting status (Running/Paused/Complete)
- Adaptive bar sizing for arrays of any size (5-100+ elements)
- Value labels for small arrays (≤20 elements)

**How to Use**:
- Select option 2 from main menu
- Enter array size or press Enter for default
- Watch the visualization!
- Use SPACE to pause and inspect current state

### Mode 3: ASCII Animation Demo

**Best for**: Quick demonstration without manual input

**Features**:
- Pre-configured test cases showing:
  - Small list (5 elements)
  - Standard list (7 elements)
  - Already-sorted list (demonstrates early termination)
- Automatic animation with 2-second pauses between tests

## 💻 Code Examples

### Using the Core Algorithm Directly

```python
from main import bubble_sort

# Basic usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # [11, 12, 22, 25, 34, 64, 90]
```

### Using ASCII Animation

```python
from main import bubble_sort_animated

numbers = [5, 2, 8, 1, 9]
bubble_sort_animated(numbers, delay=0.1)  # 0.1s between animation frames
```

Adjust `delay` for animation speed:
- `0.01` - Very fast (for fast systems)
- `0.1` - Default (recommended)
- `0.5` - Slow (for presentations)

### Using Pygame Visualization

```python
from pygame_viz import visualize_bubble_sort

numbers = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
visualize_bubble_sort(numbers, width=1200, height=600)
```

Parameters:
- `numbers`: List of integers to sort
- `width`: Window width (default 1200px)
- `height`: Window height (default 600px)

## 🧪 Test Suite

Five comprehensive tests ensure correctness:

| Test | Purpose | Input Example |
|------|---------|---|
| `test_random_unsorted_list` | Standard sorting | `[64, 34, 25, 12, 22, 11, 90]` |
| `test_already_sorted_list` | Verify no unnecessary work | `[1, 2, 3, 4, 5]` |
| `test_reverse_sorted_list` | Worst-case scenario | `[5, 4, 3, 2, 1]` |
| `test_list_with_duplicates` | Handle equal values | `[3, 1, 3, 2, 1, 3]` |
| `test_edge_cases` | Empty, single, two elements | `[]`, `[1]`, `[2, 1]` |

All tests use Python's built-in `unittest` module.

## 🔧 Implementation Details

### Early Termination Optimization

```python
for pass_num in range(len(numbers) - 1):
    swapped = False
    for i in range(len(numbers) - 1 - pass_num):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True
    
    if not swapped:  # If no swaps occurred, list is sorted
        break
```

**Why This Works**: If an entire pass occurs without any swaps, the list is guaranteed to be sorted.

**Impact**: Reduces best-case from O(n²) to O(n) for nearly-sorted data.

### Pygame Visualization Architecture

The `BubbleSortVisualizer` class handles:
- **Step-by-step sorting**: One comparison per frame
- **Color management**: Dynamic bar coloring based on state
- **Interactive controls**: Event handling for pause/resume/reset
- **Statistics tracking**: Live counters for passes, swaps, comparisons
- **Adaptive rendering**: Scales to different array sizes and window dimensions

## 📦 Installation with Dependencies

### Requirements

The project has the following dependency structure:

**Core Requirements**:
- Python 3.6 or higher
- Standard library only (unittest, time, os modules)

**Optional**:
- Pygame 2.0.0+ (for 2D graphics visualization)

### Installation Methods

**Method 1: Using requirements.txt (Recommended)**

```bash
pip install -r requirements.txt
```

This installs Pygame for the complete feature set.

**Method 2: Core Only (No Pygame)**

No additional installation needed. Run with ASCII visualization only:

```bash
python3 main.py
# Choose option 1 or 3 (ASCII modes)
```

**Method 3: Manual Pygame Installation**

```bash
pip install pygame>=2.0.0
```

Or with conda:

```bash
conda install pygame
```

### Troubleshooting Installation

If Pygame fails to install:
1. Ensure Python 3.6+ is installed: `python3 --version`
2. Upgrade pip: `pip install --upgrade pip`
3. Try user installation: `pip install pygame --user`
4. **The project works fine without Pygame** - use ASCII visualization

## 🎓 Learning Outcomes

This project demonstrates:

- ✅ **Sorting Algorithm Design**: Understanding bubble sort mechanics
- ✅ **Algorithm Optimization**: Early termination and complexity analysis
- ✅ **Python Best Practices**: Type hints, docstrings, code organization
- ✅ **Testing Methodology**: Unit testing with unittest module
- ✅ **Data Visualization**: Both terminal and graphics-based approaches
- ✅ **Interactive Programming**: Pygame event handling and rendering
- ✅ **Software Engineering**: Professional code structure and documentation

## 🚀 Future Enhancements

Potential improvements to explore:

- ✅ **Pygame 2D Graphics Visualization** (COMPLETED)
- Add reverse sorting option: `bubble_sort(numbers, reverse=True)`
- Performance benchmarking with timing comparisons
- Implement other algorithms (Quick Sort, Merge Sort, Insertion Sort)
- Side-by-side algorithm comparison visualizer
- Sound effects for swaps and comparisons
- Export visualization as video (MP4/GIF)
- Web-based visualization using Plotly or D3.js
- Mobile app version

## 📝 Files Explained

### `main.py` (232 lines)
Core sorting implementation and interactive menu system.

**Main Functions**:
- `bubble_sort(numbers: list[int]) -> list[int]`: Core algorithm with early termination
- `bubble_sort_animated(numbers: list[int], delay: float = 0.1)`: ASCII animation
- `bubble_sort_visualized()`: Legacy visualization function
- `main()`: Interactive menu system
- Helper functions: `clear_screen()`, `create_ascii_bar()`, `display_list()`

### `pygame_viz.py` (238 lines)
Pygame 2D graphics visualization module.

**Main Class**:
- `BubbleSortVisualizer`: Full Pygame implementation
  - `draw()`: Render current frame
  - `handle_events()`: Process user input
  - `step_sort()`: Execute one sorting step
  - `run()`: Main event loop

**Main Function**:
- `visualize_bubble_sort(numbers, width, height)`: Launch visualizer

### `test_bubble_sort.py` (45 lines)
Comprehensive unit test suite using Python's unittest framework.

**Test Cases**:
- `test_random_unsorted_list`: Sorting random data
- `test_already_sorted_list`: Verify efficiency with sorted data
- `test_reverse_sorted_list`: Worst-case scenario
- `test_list_with_duplicates`: Handling duplicate values
- `test_edge_cases`: Empty list, single element, two elements

### `requirements.txt`
Project dependencies specification.

**Contents**:
- `pygame>=2.0.0`: For 2D graphics visualization

## 📊 Performance Notes

### Array Size Impact

| Array Size | Time (ASCII) | Time (Pygame) | Use Case |
|-----------|---|---|---|
| 5 elements | <100ms | ~500ms | Quick demo |
| 15 elements | ~500ms | ~2-3s | Typical learning |
| 50 elements | ~5-10s | ~20-30s | Detailed study |
| 100+ elements | >30s | >60s | Algorithm study |

**Recommendations**:
- Use **ASCII mode** for speed testing
- Use **Pygame** for visual learning (10-30 elements)
- For performance analysis, disable visualization

## ❓ FAQ

**Q: Do I need to install Pygame?**
A: No. Core functionality works with just Python 3.6+. Install `requirements.txt` for the full feature set.

**Q: Can I use custom arrays?**
A: Yes. The menu prompts you to enter numbers separated by spaces.

**Q: Why is bubble sort slow?**
A: Bubble sort is O(n²) on average. It's excellent for learning, but not efficient for large datasets. See Future Enhancements for other algorithms.

**Q: What Python versions are supported?**
A: Python 3.6+. Tested on Python 3.9 and 3.14.

**Q: Can I run this in the cloud?**
A: Yes for tests/ASCII. Pygame requires a display, so graphical visualization requires a graphics server.

**Q: How do I contribute?**
A: This is an educational project. Feel free to fork, modify, and extend it for learning!

## 📚 References

- [Bubble Sort - Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)
- [Big O Notation - Complexity Analysis](https://en.wikipedia.org/wiki/Big_O_notation)
- [Python unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Type Hints (PEP 484)](https://www.python.org/dev/peps/pep-0484/)

## 👤 Author

**Divine Byishimo**

## 📄 License

Educational project - Free to use and modify for learning purposes.

---

**Last Updated**: March 26, 2026  
**Project Status**: Complete with dual visualization modes ✅  
**Total LOC**: ~520 lines (algorithm + tests + visualization)
