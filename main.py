import serial
import time
import os

# --- CONFIGURATION ---
COM_PORT = 'COM5'  # Update this to match your port
BAUD_RATE = 9600


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    try:
        arduino = serial.Serial(port=COM_PORT, baudrate=BAUD_RATE, timeout=1)
        time.sleep(2)
    except serial.SerialException:
        print(f"Error: Could not connect to {COM_PORT}.")
        return

    while True:
        clear_screen()
        print("=== Arduino LED Controller ===")
        print("[R] Red ON/OFF")
        print("[G] Green ON/OFF")
        print("[B] Blue ON/OFF")
        print("[A] All ON")
        print("[O] All OFF")
        print("[X] Exit")
        print("==============================")

        user_input = input("Enter Choice: ").strip()

        # 1. Check for empty input
        if not user_input:
            continue

        # 2. UNIFIED ERROR HANDLING (The Change)
        # If input is too long OR the character isn't in our allowed list
        # We treat it exactly the same.
        valid_commands = ['R', 'G', 'B', 'A', 'O', 'X']

        # Check length > 1  OR  First letter not in allowed list (case insensitive)
        if len(user_input) > 1 or user_input[0].upper() not in valid_commands:
            print("Invalid command.")
            time.sleep(1.0)  # Pause so user can see the message
            continue

        # 3. Process the valid single character
        command = user_input[0]

        # Exit Logic
        if command.upper() == 'X':
            print("Turning off all LEDs...")
            arduino.write(b'O')
            time.sleep(0.5)
            print("Terminating application...")
            arduino.close()
            break

        # Send to Arduino
        # Since we already filtered invalid inputs above, we know this is safe to send.
        arduino.write(command.encode())
        print(f"Command '{command}' sent.")

        time.sleep(0.5)


if __name__ == "__main__":
    main()