import sys
import os
from tabulate import tabulate


def get_driver_details():
    """Loads driver info from f1_drivers.txt"""
    drivers = {}
    try:
        with open('f1_drivers.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) < 4: continue
                code = parts[1].strip().upper()
                drivers[code] = {
                    'name': parts[2].strip(),
                    'team': parts[3].strip(),
                    'number': parts[0].strip()
                }
    except FileNotFoundError:
        pass
    return drivers


def main():
    driver_db = get_driver_details()

    # Command-line argument handling
    if len(sys.argv) != 2:
        print("Error: Please provide a lap times file")
        print("Usage: python program.py <lap_file>")
        sys.exit(1)

    lap_file = sys.argv[1]
    if not os.path.exists(lap_file):
        print(f"Error: File '{lap_file}' not found")
        sys.exit(1)

    # Read lap file
    try:
        with open(lap_file, 'r') as f:
            lines = [line.strip() for line in f]
    except IOError:
        print(f"Error: Could not read {lap_file}")
        sys.exit(1)

    # Display race name
    if not lines:
        print("Error: Empty lap file")
        sys.exit(1)
    print(f"\nRace Location: {lines[0]}")

    # Process lap times
    lap_data = {}
    all_times = []
    fastest_time = float('inf')
    fastest_driver = None

    for line in lines[1:]:
        if len(line) < 4: continue
        code = line[:3].upper()
        time_str = line[3:]

        try:
            time = float(time_str)
            if time < fastest_time:
                fastest_time = time
                fastest_driver = code
        except ValueError:
            continue

        if code not in lap_data:
            lap_data[code] = []
        lap_data[code].append(time)
        all_times.append(time)

    # Display the fastest driver with full details
    if fastest_driver:
        driver_info = driver_db.get(fastest_driver, {})
        print(f"\nFastest Driver: {fastest_driver} - {driver_info.get('name', 'Unknown')} "
              f"({driver_info.get('team', 'Unknown')}) - {fastest_time:.3f}")

    # Calculate statistics
    driver_stats = []
    for code, times in lap_data.items():
        driver_stats.append({
            'code': code,
            'name': driver_db.get(code, {}).get('name', 'Unknown'),
            'team': driver_db.get(code, {}).get('team', 'Unknown'),
            'number': driver_db.get(code, {}).get('number', 'N/A'),
            'fastest': min(times),
            'average': sum(times) / len(times),
            'laps': len(times)
        })

    # Overall average
    if all_times:
        print(f"Overall Average: {sum(all_times) / len(all_times):.3f}")

    # Sort and display
    sorted_drivers = sorted(driver_stats, key=lambda x: x['fastest'], reverse=True)

    print("\nDriver Statistics:")
    print(tabulate(
        [(d['code'], d['name'], d['team'], d['number'], f"{d['fastest']:.3f}", f"{d['average']:.3f}", d['laps'])
         for d in sorted_drivers],
        headers=["Code", "Driver", "Team", "Car #", "Fastest", "Average", "Laps"],
        tablefmt="simple_grid"
    ))


if __name__ == "__main__":
    main()