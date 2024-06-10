import wmi
import os
import time

def get_physical_disks():
    c = wmi.WMI()
    disks = []
    for disk in c.Win32_DiskDrive():
        disks.append(disk.DeviceID)
    return disks

def get_logical_disks():
    c = wmi.WMI()
    disks = []
    for disk in c.Win32_LogicalDisk():
        if disk.DriveType == 3:  # Fixed hard disk
            disks.append(disk.DeviceID)
    return disks

def list_files_and_folders(drive_letter):
    root_path = f"{drive_letter}\\"
    print(f"Contents of drive {drive_letter}:")
    for item in os.listdir(root_path):
        item_path = os.path.join(root_path, item)
        if os.path.isdir(item_path):
            print(f"  [Folder] {item}")
        else:
            print(f"  [File]   {item}")

def main():
    print("Press 'Ctrl+C' to quit the program at any time.")
    c = wmi.WMI()
    previous_disks = set(get_physical_disks())
    disk_drive_mapping = {}  # Dictionary to store the mapping between physical disks and drive letters
    
    # Capture the initial mapping between physical disks and drive letters
    for disk in c.Win32_DiskDrive():
        if disk.DeviceID in previous_disks:
            for partition in disk.associators("Win32_DiskDriveToDiskPartition"):
                for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                    disk_drive_mapping[disk.DeviceID] = logical_disk.DeviceID
                    list_files_and_folders(logical_disk.DeviceID)
    
    try:
        while True:
            current_disks = set(get_physical_disks())
            
            # Check for newly plugged devices
            new_disks = current_disks - previous_disks
            for disk in c.Win32_DiskDrive():
                if disk.DeviceID in new_disks:
                    print(f"Device {disk.DeviceID}: was PLUGGED IN")
                    time.sleep(1)  # Wait for 1 second to allow drive letter assignment
                    for partition in disk.associators("Win32_DiskDriveToDiskPartition"):
                        for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                            drive = logical_disk.DeviceID
                            disk_drive_mapping[disk.DeviceID] = drive
                            list_files_and_folders(drive)
            
            # Check for recently unplugged devices
            for disk in previous_disks - current_disks:
                if disk in disk_drive_mapping:
                    drive_letter = disk_drive_mapping[disk]
                    print(f"Device {disk} (Drive {drive_letter}): was UNPLUGGED")
                    del disk_drive_mapping[disk]  # Remove the mapping for the unplugged device
                else:
                    print(f"Device {disk}: was UNPLUGGED")
                # Add any cleanup actions here if needed
            
            previous_disks = current_disks
            time.sleep(1)  # Wait for 1 second before checking again
    except KeyboardInterrupt:
        print("\nYou pressed Ctrl+C, exiting...")

if __name__ == "__main__":
    main()