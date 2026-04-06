# Bluetooth Device Scanner

A terminal-based Python script that continuously scans for nearby Bluetooth devices and logs discovered MAC addresses and names.

> **For educational and authorized use only.**

---

## Features

- Continuous Bluetooth scan using `hcitool`
- Deduplicates results across scans
- Persists discovered devices to `devices.txt`
- Displays indexed list of named devices in real time
- Custom ASCII logo via `logo.py`

---

## Requirements

- Linux with Bluetooth support
- `bluez` package (`hcitool`)
- Python 3

```bash
sudo apt install bluez
```

No external Python packages required.

---

## File Structure

```
.
├── scanner.py
├── logo.py          # Contains print_cyberday() ASCII art function
└── devices.txt      # Auto-created on first run
```

---

## Usage

```bash
sudo python scanner.py
```

> Root privileges are required for Bluetooth scanning.

Press any key to start. Use `Ctrl+C` to exit cleanly.

---

## How It Works

1. Runs `hcitool scan` in a loop to discover nearby Bluetooth devices
2. New entries (not already in `devices.txt`) are appended
3. Only devices with a known name (not `n/a`) are printed to the terminal
4. Each device is shown with an index, MAC address, and name

---

## Notes

- `hcitool scan` only detects **discoverable** Bluetooth Classic devices (not BLE)
- For BLE scanning, consider replacing with `hcitool lescan` or using `bluepy`
- The `logo.py` file must define a `print_cyberday()` function
