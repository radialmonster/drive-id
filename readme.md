# Drive Monitor

This script is designed to monitor physical and logical disk drives on a Windows machine. It detects when a drive is plugged in or unplugged, lists the files and folders on newly plugged drives, and provides a real-time view of drive changes.

## Why It's Necessary

Monitoring physical and logical disk drives can be crucial for various reasons, including:

- **Data Security:** Ensuring that unauthorized drives are detected immediately.
- **Data Management:** Keeping track of all connected storage devices and their contents.
- **System Maintenance:** Monitoring the health and status of drives for early detection of potential failures.

## Features

- **Real-Time Monitoring:** Continuously checks for changes in the connected drives.
- **Drive Mapping:** Maintains a mapping between physical disks and their assigned drive letters.
- **Content Listing:** Automatically lists the contents of newly plugged-in drives.
- **User-Friendly Output:** Provides clear and concise output about the status of the drives.

## Unique Aspects

- **Integration with WMI:** Utilizes Windows Management Instrumentation (WMI) to gather detailed information about disk drives.
- **Dynamic Updates:** Detects and handles changes in real-time without requiring manual refresh.
- **Comprehensive Coverage:** Monitors both physical disks and their logical partitions, providing a complete view of the storage environment.

## How to Use

1. **Clone the Repository:**
    ```bash
    git clone <repository-url>
    ```

2. **Install Dependencies:**
    Ensure you have the `wmi` package installed. You can install it using pip:
    ```bash
    pip install wmi
    ```

3. **Run the Script:**
    Execute the script from your terminal or command prompt:
    ```bash
    python drive_monitor.py
    ```

4. **Monitor Output:**
    The script will start monitoring immediately, displaying information about any drive changes in real-time. Press `Ctrl+C` to stop the script.

## Example Output

Press 'Ctrl+C' to quit the program at any time.
Contents of drive C:
[Folder] Program Files
[Folder] Users
[Folder] Windows
[File] pagefile.sys
Device \.\PHYSICALDRIVE1: was PLUGGED IN
Contents of drive D:
[Folder] Documents
[Folder] Music
Device \.\PHYSICALDRIVE1 (Drive D): was UNPLUGGED


## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request with your improvements or bug fixes.
