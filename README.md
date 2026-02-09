# Auto-Clicker

A simple yet effective Python script that automates mouse clicks at random intervals. It features automated idle detection, stopping the clicking process as soon as you move the mouse.

## Features

- **Automated Clicking**: Performs a left mouse click every 3 to 6 minutes (randomized).
- **Idle Detection**: Automatically stops the script if the mouse cursor is moved from its initial position.
- **Activity Logging**: Prints the timestamp of each click to the console.
- **Two Implementations**: 
    - `main.py` (Recommended): Uses `pynput` for better event handling.
    - `main_alternative.py`: Uses `pyautogui` as an alternative.

## Requirements

- Python 3.x
- `pynput` (for `main.py`)
- `pyautogui` (for `main_alternative.py`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/auto-click.git
   cd auto-click
   ```

2. Install the required dependencies based on the script you want to run:

   For `main.py` (Recommended):
   ```bash
   python3 -m pip install pynput
   ```

   For `main_alternative.py`:
   ```bash
   python3 -m pip install pyautogui
   ```

## Usage

### Running the Recommended Script

1. Open your terminal.
2. Run the script:
   ```bash
   python3 main.py
   ```
3. The script will initialize in 10 seconds. Do not move your mouse during this time.
4. Once initialized, it will click every 3-6 minutes.
5. To stop the script, simply move your mouse.

### Running the Alternative Script

1. Open your terminal.
2. Run the script:
   ```bash
   python3 main_alternative.py
   ```
3. The behavior is similar to the main script.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
