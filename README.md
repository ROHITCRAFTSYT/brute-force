# Fire Stick Parental Control Brute Force Script

This Python script automates brute forcing the 5-digit parental control PIN on an Amazon Fire Stick using ADB (Android Debug Bridge). It inputs every possible 5-digit code from `00000` to `99999` sequentially.

## Disclaimer

This tool is intended **only** for authorized security testing on devices you own or have explicit permission to test. Unauthorized use against devices you do not own or have permission to test is illegal and unethical.
--
## Requirements

- Python 3.x
- ADB installed and configured on your system
- Fire Stick connected and authorized for ADB commands (via USB or network)
- Parental control PIN entry screen active on the Fire Stick
--
## Setup

1. Ensure ADB is installed and accessible from your command line.
2. Connect to your Fire Stick via ADB:
   ```bash
   adb connect <fire_stick_ip_address>
3.Verify connection:
bash:
**adb devices**

**Make sure the parental control PIN entry screen is displayed on the Fire Stick.**

##Usage

4.Run the script:

bash:
python brute_force_firestick_pin.py

The script will attempt every 5-digit code from 00000 to 99999, inputting each code via ADB key events.
--
##Notes
The script currently does not detect when the correct PIN is entered. You may need to manually observe or extend the script with detection logic (e.g., screen capture and analysis).
Be aware of potential rate limiting or lockout mechanisms on the Fire Stick that may slow or block brute force attempts.
Adjust delays in the script (time.sleep) as needed to avoid triggering lockouts.
--
##Extending the Script
To improve usability, consider adding:

Automatic detection of successful PIN entry (e.g., via screenshot analysis).
Logging of attempted codes.
Configurable delays and retry limits.
--
##License
This project is provided for educational and authorized testing purposes only. Use responsibly.
