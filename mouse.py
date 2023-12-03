import pyautogui

# Continuously print the coordinates of the mouse cursor
print("Move your mouse to the desired position.")
print("Press Ctrl+C to stop.")

try:
    while True:
        # Get and display the current mouse coordinates
        x, y = pyautogui.position()
        position_str = f"X: {x}, Y: {y}"
        print(position_str, end="\r")
except KeyboardInterrupt:
    print("\nCoordinates stopped.")
