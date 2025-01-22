# Connections Game

This repository contains a fun and interactive **Connections Game** built using **Python** and **PyQt6**. Test your skills in identifying groups of related words while enjoying a visually appealing and engaging interface.


---

## Features
- Multiple categories to choose from (e.g., Programming, Food, Entertainment, etc.).
- Interactive word selection with a colour-coded button system:
  - Dark blue-grey for unselected words.
  - Red for selected words.
  - Green for solved categories.
- Dynamic mistake tracking.
- Customisable UI with a polished look and feel.
- Game over and victory screens.

---

## How to Play
1. Launch the game and navigate to the main menu.
2. Select a category from the available options.
3. Identify groups of four related words by clicking on the buttons.
   - Select exactly 4 words that you believe are related.
   - If correct, they are removed from the grid, and the category is displayed on the screen.
   - If incorrect, a mistake is recorded.
4. Solve all categories before reaching the maximum number of mistakes (4 mistakes).
5. Win by completing all groups or lose if you make too many mistakes.

---

## Installation
1. Clone the repository to your local machine:
   ```bash
   https://github.com/AbdullahNavaid/Connections.git
   ```
2. Install the required dependencies:
   ```bash
   pip install PyQt6
   ```
3. Run the game:
   ```bash
   python connections_game.py
   ```

---

## Game Flow
### Menu Screen:
- Displays the game title and a "Play" button.

### Category Selection:
- Allows players to choose a category from a grid of buttons.

### Game Screen:
- Displays a 4x4 grid of words and tracks mistakes.
- Allows players to select and submit groups of related words.
- Updates dynamically as categories are solved.

### End Game:
- Displays a victory or game over message with an option to return to the main menu.

---

## Technologies Used
- **Python**: Core programming language.
- **PyQt6**: For creating the graphical user interface (GUI).

---


