# Star Simulation Game

I created this game as one of several mini-games in the VR experience for the MUI project, letting you and your partner compete against each other.

## Installation and Execution

### Prerequisites

- **Python 3.x**: Make sure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).
- **Pygame Library**: The game requires the Pygame library for Python.

### Installing Pygame

Open your command prompt or terminal and run the following command to install Pygame:

```bash
pip install pygame
```

### Downloading the Game

#### Option 1: Direct Download

1. **Download the Repository**:

   - Click on the green **"Code"** button at the top of the repository page.
   - Select **"Download ZIP"**.
   - Save the ZIP file to your computer.

2. **Extract the ZIP File**:

   - Locate the downloaded ZIP file.
   - Right-click and select **"Extract All..."** or use your preferred extraction tool.
   - Choose a destination folder and extract the files.

### Running the Game

1. **Navigate to the Game Directory**:

   Open your terminal or command prompt and navigate to the directory where `star_simulation.py` is located:

   ```bash
   cd path/to/star_simulation
   ```

2. **Run the Game Script**:

   Execute the game by running:

   ```bash
   python star_simulation.py
   ```

   If you have multiple versions of Python installed, you might need to specify `python3`:

   ```bash
   python3 star_simulation.py
   ```

## How to Play

- **Objective**: Steer your spaceship through space, avoiding collisions with stars to achieve the highest score possible.

### Controls

- **Mouse Movement**:

  - Move your mouse to control the spaceship's position on the screen.
  - The spaceship is represented by a red circle.
  - The mouse cursor is hidden during gameplay for better immersion.

- **Mouse Scroll Wheel**:

  - **Scroll Up**: Increase your speed through the starfield.
  - **Scroll Down**: Decrease your speed.

- **Restarting the Game**:

  - If you collide with a star and the game ends, click the **left mouse button** anywhere on the screen to restart.

### Gameplay Tips

- **Avoid the Stars**: Maneuver your spaceship to dodge incoming stars. Collision with a star ends the game.
- **Speed Control**: Adjust your speed using the scroll wheel to navigate through dense star fields or to challenge yourself.
- **Score Tracking**:

  - Your current score is displayed at the top-right corner.
  - The **High Score** is also displayed, so you can aim to beat your previous best.

- **Collision Detection Delay**: There's a short delay at the start of the game before collisions are activated. Use this time to position your spaceship.

### Adjusting Game Settings

If needed, you can modify game settings by editing the `star_simulation.py` file:

- **Screen Resolution**:

  - Locate the following lines at the beginning of the file:

    ```python
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    ```

  - Change these values to match your screen's resolution.

- **Performance Optimization**:

  - If the game runs slowly, reduce the number of stars:

    ```python
    NUM_STARS = 5000  # Try reducing to 3000 or 2000
    ```

- **Ship Sensitivity**:

  - Adjust the ship's responsiveness to mouse movement:

    ```python
    ship_speed = 0.05  # Increase for more sensitivity, decrease for less
    ```

## Enjoy the Game!