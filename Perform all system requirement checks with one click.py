# Author: Goutam Sahoo
import psutil  # Library for retrieving system information
import platform  # Provides system-related information
import shutil  # Used for checking disk and USB storage

def check_cpu():
    """Check if the CPU meets the 2 GHz dual-core requirement."""
    try:
        min_ghz = 2.0  # Minimum required CPU speed in GHz
        min_cores = 2  # Minimum required number of physical CPU cores
        
        # Get CPU max frequency and convert from MHz to GHz
        cpu_ghz = psutil.cpu_freq().max / 1000  
        # Get the number of physical cores (ignoring logical cores)
        cpu_cores = psutil.cpu_count(logical=False)  
        
        print(f"CPU: {cpu_cores} Cores, {cpu_ghz:.2f} GHz")
        if cpu_ghz >= min_ghz and cpu_cores >= min_cores:
            print("✅ CPU meets the requirement.")
        else:
            print("❌ CPU does not meet the requirement.")
    except Exception as e:
        print(f"⚠ Unable to check CPU: {e}")

def check_ram():
    """Check if the system has at least 4 GB of RAM."""
    min_ram_gb = 4  # Minimum required RAM in GB
    recommended_ram_gb = 8  # Recommended RAM for better performance

    # Get total RAM and convert from bytes to GB
    ram_gb = psutil.virtual_memory().total / (1024**3)  
    
    print(f"RAM: {ram_gb:.2f} GB")
    if ram_gb >= recommended_ram_gb:
        print("✅ RAM is optimal (8 GB or more).")
    elif ram_gb >= min_ram_gb:
        print("✅ RAM meets the minimum requirement (4 GB).")
    else:
        print("❌ RAM is insufficient (less than 4 GB).")

def check_disk():
    """Check if the system has at least 25 GB of free disk space."""
    min_disk_gb = 25  # Minimum required free disk space in GB

    # Get disk space details (total, used, free) in bytes and convert to GB
    total, used, free = shutil.disk_usage("/")
    free_gb = free / (1024**3)  

    print(f"Disk Space: {free_gb:.2f} GB Free")
    if free_gb >= min_disk_gb:
        print("✅ Disk space meets the requirement.")
    else:
        print("❌ Not enough disk space (Requires at least 25 GB).")

def check_usb():
    """Check if an external USB with at least 8 GB is available."""
    min_usb_gb = 8  # Minimum required USB size in GB
    usb_found = False  # Flag to track if a suitable USB is found

    # Get a list of all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        # Check if the partition is a removable USB drive
        if 'removable' in partition.opts.lower() or 'media' in partition.mountpoint.lower():
            # Get USB storage details and convert to GB
            usage = shutil.disk_usage(partition.mountpoint)
            usb_size_gb = usage.total / (1024**3)
            print(f"USB: {usb_size_gb:.2f} GB detected at {partition.mountpoint}")
            if usb_size_gb >= min_usb_gb:
                print("✅ USB drive meets the requirement.")
                usb_found = True
            else:
                print("❌ USB storage is too small (Needs at least 8 GB).")
    
    if not usb_found:
        print("⚠ No suitable USB drive detected.")

def check_system():
    """Run all system requirement checks."""
    print("\n🔍 Checking System Requirements for Ubuntu Installation...\n")
    check_cpu()
    check_ram()
    check_disk()
    check_usb()
    print("\n✅ System Check Complete!")

# Run the checks
check_system()

