"""
Pygame-based Bubble Sort Visualizer
Provides real-time 2D graphics visualization of bubble sort algorithm with interactive controls.
"""

import pygame
import sys
from typing import List, Tuple
from copy import deepcopy


class BubbleSortVisualizer:
    """Real-time bubble sort visualization using Pygame."""
    
    def __init__(self, numbers: List[int], width: int = 1200, height: int = 600, fps: int = 30):
        """
        Initialize the visualizer with display configuration.
        
        Args:
            numbers: List of integers to sort
            width: Window width in pixels (default 1200)
            height: Window height in pixels (default 600)
            fps: Target frames per second (default 30 for slower animation)
        """
        self.numbers = deepcopy(numbers)
        self.original_numbers = deepcopy(numbers)
        self.width = width
        self.height = height
        self.fps = fps
        
        # State tracking
        self.comparing_indices: Tuple[int, int] = (-1, -1)
        self.swap_indices: Tuple[int, int] = (-1, -1)
        self.swap_timer = 0
        self.is_sorted = False
        self.is_paused = False
        self.sorting_complete = False
        
        # Statistics
        self.passes = 0
        self.swaps = 0
        self.comparisons = 0
        self.current_pass = 0
        self.step_delay = 0  # Delay counter for slower step progression
        
        # Pygame setup
        pygame.init()
        self.display = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Bubble Sort Visualizer - Press SPACE to pause, R to reset, ENTER to step")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
        # Colors
        self.COLOR_BG = (30, 30, 30)
        self.COLOR_BAR = (70, 130, 180)
        self.COLOR_COMPARING = (255, 100, 100)
        self.COLOR_SWAP = (100, 255, 100)
        self.COLOR_SORTED = (100, 150, 255)
        self.COLOR_TEXT = (255, 255, 255)
        
        # Bar rendering
        self.bar_area_top = 80
        self.bar_area_height = self.height - self.bar_area_top - 100
        self.calc_bar_dimensions()
    
    def calc_bar_dimensions(self):
        """Calculate bar width based on number count."""
        n = len(self.numbers)
        if n > 0:
            self.bar_width = (self.width - 40) // n
            self.bar_width = max(1, min(self.bar_width, 50))  # Clamp between 1 and 50
            self.max_value = max(self.numbers) if self.numbers else 100
            self.bar_height_factor = self.bar_area_height / (self.max_value if self.max_value > 0 else 1)
        else:
            self.bar_width = 1
            self.bar_height_factor = 1
    
    def draw(self):
        """Render the current frame with enhanced visuals."""
        self.display.fill(self.COLOR_BG)
        
        # Draw semi-transparent background panel for title
        pygame.draw.rect(self.display, (20, 20, 40), (0, 0, self.width, 70))
        
        # Draw title with better styling
        title = self.font_large.render("🔄 Bubble Sort Visualization", True, self.COLOR_TEXT)
        self.display.blit(title, (20, 20))
        
        # Draw array info
        array_size_text = self.font_small.render(f"Array Size: {len(self.numbers)}", True, (150, 200, 255))
        self.display.blit(array_size_text, (self.width - 250, 20))
        
        # Draw statistics with better formatting
        stats_text = f"Pass: {self.current_pass:2d} | Swaps: {self.swaps:3d} | Comparisons: {self.comparisons:4d}"
        stats = self.font_small.render(stats_text, True, (200, 200, 200))
        self.display.blit(stats, (20, self.height - 60))
        
        # Draw status message with enhanced styling
        if self.sorting_complete:
            status = "✅ SORT COMPLETE! Press R to reset"
            color = (100, 255, 100)
        elif self.is_paused:
            status = "⏸️  PAUSED - Press SPACE to resume, ENTER to step one"
            color = (255, 200, 100)
        else:
            status = "▶️  Sorting in progress..."
            color = (100, 200, 255)
        
        status_text = self.font_small.render(status, True, color)
        self.display.blit(status_text, (20, self.height - 30))
        
        # Draw control hints at bottom - change based on sort state
        if self.sorting_complete:
            hints = self.font_small.render("Controls: R=Reset | Q/ESC=Exit", True, (100, 100, 100))
        else:
            hints = self.font_small.render("Controls: SPACE=Pause | R=Reset | ENTER=Step (when paused)", True, (100, 100, 100))
        self.display.blit(hints, (20, self.height - 30))
        
        # Draw bars with enhanced animation
        self._draw_bars()
        
        pygame.display.flip()
    
    def _draw_bars(self):
        """Draw the bar chart representation with enhanced visuals."""
        start_x = 20
        
        for i, value in enumerate(self.numbers):
            x = start_x + i * self.bar_width
            bar_height = int(value * self.bar_height_factor)
            y = self.bar_area_top + (self.bar_area_height - bar_height)
            
            # Determine bar color with gradient effect
            if self.sorting_complete:
                # Gradient from blue to cyan when sorted
                color = (100 + (i % 50), 150 + (i % 100), 200 + (i % 55))
            elif i in self.swap_indices and self.swap_timer > 0:
                # Different colors for the two elements being swapped
                pulse = (self.swap_timer / 30.0) * 50  # Adjusted for new swap_timer of 30
                if i == self.swap_indices[0]:
                    # First element: Yellow/Orange
                    color = (255, 200 + int(pulse / 2), 50)
                else:
                    # Second element: Cyan/Light Blue
                    color = (100 + int(pulse), 255, 200 + int(pulse / 2))
            elif i in self.comparing_indices:
                # Different colors for the two elements being compared
                if i == self.comparing_indices[0]:
                    # First element: Orange/Red
                    color = (255, 150, 50)
                else:
                    # Second element: Pink/Magenta
                    color = (255, 100, 200)
            else:
                # Base bar color - light blue
                color = (70, 130, 180)
            
            # Draw bar with border for better definition
            pygame.draw.rect(self.display, color, (x, y, self.bar_width - 2, bar_height))
            
            # Draw border for visibility
            pygame.draw.rect(self.display, (40, 40, 60), (x, y, self.bar_width - 2, bar_height), 1)
            
            # Draw value label (for small arrays)
            if len(self.numbers) <= 25:
                value_text = self.font_small.render(str(value), True, self.COLOR_TEXT)
                text_width = value_text.get_width()
                text_x = x + (self.bar_width - text_width) // 2
                text_y = y - 25 if bar_height > 50 else y + bar_height + 5
                self.display.blit(value_text, (text_x, text_y))
    
    def handle_events(self):
        """Handle user input. Returns False to quit."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.is_paused = not self.is_paused
                elif event.key == pygame.K_r:
                    self.reset()
                elif event.key == pygame.K_RETURN:
                    if self.is_paused:
                        self.step_sort()
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    # Only exit if sort is complete
                    if self.sorting_complete:
                        return False
        
        return True
    
    def step_sort(self):
        """Execute one comparison/swap step."""
        if self.sorting_complete:
            return
        
        n = len(self.numbers)
        
        # Initialize or continue sorting
        if not hasattr(self, 'sort_state'):
            self.sort_state = {'pass_num': 0, 'i': 0, 'swapped': False}
        
        state = self.sort_state
        
        # Inner loop - compare adjacent elements
        if state['i'] < n - 1 - state['pass_num']:
            self.comparing_indices = (state['i'], state['i'] + 1)
            self.comparisons += 1
            
            if self.numbers[state['i']] > self.numbers[state['i'] + 1]:
                # Perform swap
                self.numbers[state['i']], self.numbers[state['i'] + 1] = \
                    self.numbers[state['i'] + 1], self.numbers[state['i']]
                self.swap_indices = (state['i'], state['i'] + 1)
                self.swap_timer = 30  # Increased from 15 for slower animation
                self.swaps += 1
                state['swapped'] = True
            
            state['i'] += 1
        else:
            # End of inner loop - move to next pass
            self.current_pass += 1
            state['pass_num'] += 1
            state['i'] = 0
            
            if not state['swapped'] or state['pass_num'] >= n - 1:
                # Sorting complete
                self.sorting_complete = True
                self.comparing_indices = (-1, -1)
                self.swap_indices = (-1, -1)
            else:
                state['swapped'] = False
    
    def run(self):
        """Main visualization loop."""
        running = True
        
        while running:
            running = self.handle_events()
            
            # Update animation
            if self.swap_timer > 0:
                self.swap_timer -= 1
            
            # Step through sorting (unless paused) with delay for slower animation
            if not self.is_paused and not self.sorting_complete:
                self.step_delay += 1
                if self.step_delay >= 2:  # Step every 2 frames at 30 FPS = slower progression
                    self.step_sort()
                    self.step_delay = 0
            
            self.draw()
            self.clock.tick(self.fps)
        
        pygame.quit()
        sys.exit()
    
    def reset(self):
        """Reset visualization to initial state."""
        self.numbers = deepcopy(self.original_numbers)
        self.comparing_indices = (-1, -1)
        self.swap_indices = (-1, -1)
        self.swap_timer = 0
        self.sorting_complete = False
        self.is_paused = False
        self.passes = 0
        self.swaps = 0
        self.comparisons = 0
        self.current_pass = 0
        
        if hasattr(self, 'sort_state'):
            delattr(self, 'sort_state')
        
        self.calc_bar_dimensions()


def visualize_bubble_sort(numbers: List[int], width: int = 1200, height: int = 600):
    """
    Launch interactive Pygame visualization of bubble sort.
    
    Args:
        numbers: List of integers to sort
        width: Window width (default 1200px)
        height: Window height (default 600px)
    
    Controls:
        - SPACE: Pause/Resume sorting
        - R: Reset to original array
        - ENTER: Step through one comparison (when paused)
        - Q or ESC: Exit (only available after sort completes)
    """
    visualizer = BubbleSortVisualizer(numbers, width, height)
    visualizer.run()


if __name__ == "__main__":
    # Demo with sample array
    test_array = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 32, 12, 67, 89, 23]
    visualize_bubble_sort(test_array)
