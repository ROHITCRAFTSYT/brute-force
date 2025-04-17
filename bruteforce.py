import subprocess
import time

def adb_input_digit(digit):
    keyevent_map = {
        '0': '7',
        '1': '8',
        '2': '9',
        '3': '10',
        '4': '11',
        '5': '12',
        '6': '13',
        '7': '14',
        '8': '15',
        '9': '16'
    }
    keyevent = keyevent_map[digit]
    subprocess.run(['adb', 'shell', 'input', 'keyevent', keyevent], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def input_code(code):
    for digit in code:
        adb_input_digit(digit)
        time.sleep(0.15)  # delay between digits
    # Press Enter to submit
    subprocess.run(['adb', 'shell', 'input', 'keyevent', '66'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def check_success():
    # Placeholder for detection logic.
    # You could implement screenshot comparison or log reading here.
    # For now, just wait a bit to let Fire Stick respond.
    time.sleep(1)
    # Return False to continue brute forcing
    return False

def main():
    for i in range(100000):
        code = f"{i:05d}"
        print(f"Trying code: {code}")
        input_code(code)
        if check_success():
            print(f"Code found: {code}")
            break
        else:
            # Optional: add delay to avoid lockout
            time.sleep(0.5)

if __name__ == "__main__":
    main()