# 🎮 Connect 4 AI

This project is a Python-based implementation of the classic **Connect 4** game featuring a graphical interface and an AI opponent powered by the **minimax algorithm** with alpha-beta pruning. It's a fun demonstration of applying adversarial search and game theory to a real-world turn-based game.

## 🧠 Features

- Two-player mode: Play against a friend or the computer.
- AI opponent using **Minimax with Alpha-Beta Pruning**.
- Visual board display using **Pygame**.
- Adjustable search depth for AI difficulty tuning.
- Clean, modular code ideal for learning and experimentation.

## 🏗️ Technologies Used

- Python 3
- Pygame
- NumPy

## 🚀 How to Run

1. **Clone the repo**:
   ```bash
   git clone https://github.com/mthupukari/Connect-4-ai.git
   cd Connect-4-ai
   ```

2. **Install dependencies**:
   ```bash
   pip install pygame numpy
   ```

3. **Run the game**:
   ```bash
   python connect4.py
   ```

## 🕹️ Controls

- Click on a column to drop your piece.
- The board will alternate turns between player and AI.
- First player to align four pieces horizontally, vertically, or diagonally wins.

## ⚙️ Project Structure

```
Connect-4-ai/
├── connect4.py        # Main game loop and Pygame GUI
├── minimax.py         # AI logic using Minimax with alpha-beta pruning
├── game.py            # Core game logic and utility functions
├── README.md          # Project description and setup guide
```

## 🧩 Future Improvements

- Add difficulty levels with adjustable search depth.
- Include a leaderboard or scoring system.
- Enhance UI with animations and sound effects.
- Enable networked multiplayer functionality.

## 👨‍💻 Author

**Mahit Thupukari**  
[GitHub](https://github.com/mthupukari)

---

Enjoy the game and feel free to contribute!
