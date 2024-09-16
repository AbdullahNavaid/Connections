import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QGridLayout, QStackedWidget)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QColor

class ColorChangingButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("""
            QPushButton {
                background-color: #000000;  # Black color
                color: #ffffff;  # White text
                border: 2px solid #c0c0c0;
                border-radius: 10px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #333333;  # Darker black for hover effect
            }
        """)
        self.setSelected(False)

    def setSelected(self, selected):
        self.selected = selected
        if selected:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #4a90e2;  # Blue color for selected state
                    color: white;
                    border: 2px solid #2a70c2;
                    border-radius: 10px;
                    padding: 5px;
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #000000;  # Black color
                    color: #ffffff;  # White text
                    border: 2px solid #c0c0c0;
                    border-radius: 10px;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #333333;  # Darker black for hover effect
                }
            """)

class ConnectionsGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connections")
        self.setFixedSize(800, 600)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.init_game_data()
        self.create_menu_screen()
        self.create_category_selection_screen()
        self.create_game_screen()

        self.central_widget.setCurrentWidget(self.menu_screen)

    def init_game_data(self):
        self.days = {
            "Programming": {
                "types of loops": ["for", "while", "do", "sentinel"],
                "data types": ["int", "float", "string", "boolean"],
                "container types": ["list", "dictionary", "set", "tuple"],
                "components of a program": ["input", "output", "comments", "header"]
            },
            "Objects": {
                "containers": ["basket", "bin", "chest", "hamper"],
                "circular shapes": ["band", "circle", "hoop", "ring"],
                "___ jam": ["nba", "paper", "pearl", "traffic"],
                "restrict": ["cap", "check", "curb", "limit"]
            },
            "Food": {
                "unit of bread": ["baguette", "bun", "loaf", "roll"],
                "assure, as a win": ["clinch", "guarantee", "lock", "secure"],
                "small imperfection": ["chip", "mark", "nick", "scratch"],
                "head of ___": ["hair", "lettuce", "state", "steam"]
            },
            "Entertainment": {
                "bookstore sections": ["fiction", "humor", "poetry", "travel"],
                "enormous": ["big", "giant", "great", "huge"],
                "___ crane": ["construction", "frasier", "paper", "whooping"],
                "tv shows with happy-sounding names": ["cheers", "euphoria", "felicity", "glee"]
            },
            "Heroes": {
                "superhero last names": ["banner", "prince", "stark", "wayne"],
                "decline": ["ebb", "fade", "flag", "wane"],
                "absolute": ["pure", "sheer", "total", "utter"],
                "express": ["air", "speak", "state", "voice"]
            },
            "Holidays": {
                "thanksgiving food": ["gravy", "pie", "stuffing", "turkey"],
                "seen on valentine's day": ["card", "chocolate", "heart", "rose"],
                "___ button": ["belly", "hot", "panic", "snooze"],
                "sticky situation": ["bind", "pickle", "scrape", "spot"]
            }
        }
        self.current_category = ""
        self.words = []
        self.selected_words = []
        self.mistakes = 0
        self.solved_categories = []

    def create_menu_screen(self):
        self.menu_screen = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Connections")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 36))
        layout.addWidget(title)

        play_button = QPushButton("Play")
        play_button.setFixedSize(200, 100)
        play_button.setFont(QFont("Arial", 24))
        play_button.clicked.connect(self.show_category_selection)
        layout.addWidget(play_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.menu_screen.setLayout(layout)
        self.central_widget.addWidget(self.menu_screen)

    def create_category_selection_screen(self):
        self.category_selection_screen = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Select a Category")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 36))
        layout.addWidget(title)

        grid = QGridLayout()
        for i, category in enumerate(self.days.keys()):
            button = QPushButton(category)
            button.setFixedSize(350, 100)
            button.clicked.connect(lambda _, c=category: self.start_game(c))
            grid.addWidget(button, i // 2, i % 2)

        layout.addLayout(grid)
        self.category_selection_screen.setLayout(layout)
        self.central_widget.addWidget(self.category_selection_screen)

    def create_game_screen(self):
        self.game_screen = QWidget()
        self.game_layout = QVBoxLayout()

        self.word_grid = QGridLayout()
        self.game_layout.addLayout(self.word_grid)

        self.category_layout = QVBoxLayout()
        self.game_layout.addLayout(self.category_layout)

        self.mistakes_label = QLabel("Mistakes: 0")
        self.game_layout.addWidget(self.mistakes_label, alignment=Qt.AlignmentFlag.AlignRight)

        self.game_screen.setLayout(self.game_layout)
        self.central_widget.addWidget(self.game_screen)

    def show_category_selection(self):
        self.central_widget.setCurrentWidget(self.category_selection_screen)

    def start_game(self, category):
        self.current_category = category
        self.init_game()
        self.update_game_screen()
        self.central_widget.setCurrentWidget(self.game_screen)

    def init_game(self):
        self.words = []
        for category in self.days[self.current_category].values():
            self.words.extend(category)
        random.shuffle(self.words)
        self.selected_words = []
        self.mistakes = 0
        self.solved_categories = []

    def update_game_screen(self):
        # Clear existing layouts
        for i in reversed(range(self.word_grid.count())):
            self.word_grid.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.category_layout.count())):
            self.category_layout.itemAt(i).widget().setParent(None)

        # Add word buttons
        for i, word in enumerate(self.words):
            button = ColorChangingButton(word)
            button.setFixedSize(180, 80)
            button.clicked.connect(lambda _, w=word, b=button: self.toggle_word(w, b))
            self.word_grid.addWidget(button, i // 4, i % 4)

        # Add solved categories
        for category in self.solved_categories:
            label = QLabel(f"{category}: {', '.join(self.days[self.current_category][category])}")
            self.category_layout.addWidget(label)

        # Update mistakes
        self.mistakes_label.setText(f"Mistakes: {self.mistakes}")

    def toggle_word(self, word, button):
        if word in self.selected_words:
            self.selected_words.remove(word)
            button.setSelected(False)
        elif len(self.selected_words) < 4:
            self.selected_words.append(word)
            button.setSelected(True)

        if len(self.selected_words) == 4:
            self.check_selection()

    def check_selection(self):
        for category, words_in_category in self.days[self.current_category].items():
            if set(self.selected_words) == set(words_in_category):
                self.solved_categories.append(category)
                for word in self.selected_words:
                    self.words.remove(word)
                self.selected_words.clear()
                if len(self.words) == 0:
                    self.game_over("You won!")
                else:
                    self.update_game_screen()
                return

        self.mistakes += 1
        for i in range(self.word_grid.count()):
            button = self.word_grid.itemAt(i).widget()
            if button.text() in self.selected_words:
                button.setSelected(False)
        self.selected_words.clear()
        if self.mistakes >= 4:
            self.game_over("Game over!")
        else:
            self.update_game_screen()

    def game_over(self, message):
        for i in reversed(range(self.game_layout.count())):
            self.game_layout.itemAt(i).widget().setParent(None)

        game_over_label = QLabel(message)
        game_over_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        game_over_label.setFont(QFont("Arial", 36))
        self.game_layout.addWidget(game_over_label)

        restart_button = QPushButton("Back to Menu")
        restart_button.clicked.connect(self.show_menu)
        self.game_layout.addWidget(restart_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def show_menu(self):
        self.central_widget.setCurrentWidget(self.menu_screen)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConnectionsGame()
    window.show()
    sys.exit(app.exec())
