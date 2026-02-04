def temperature_analysis():
    temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
    
    print("=== Temperature Analysis ===")
    print(f"Full temperature list: {temperatures}")
    print(f"Total readings: {len(temperatures)}")
    print()
    
    print("1. First and Last Readings:")
    print(f"   First reading (index 0): {temperatures[0]}°C")
    print(f"   Last reading (index -1): {temperatures[-1]}°C")
    print()
    
    print("2. Afternoon Peak Readings (Hours 3-6):")
    print(f"   Original indices: temperatures[3:6]")
    afternoon_peak = temperatures[3:6]
    print(f"   Afternoon Peak: {afternoon_peak}")
    print(f"   Values: {temperatures[3]}°C, {temperatures[4]}°C, {temperatures[5]}°C")
    print()
    
    print("3. Last 3 Hours Readings:")
    print(f"   Original indices: temperatures[-3:]")
    last_three_hours = temperatures[-3:]
    print(f"   Last 3 Hours: {last_three_hours}")
    print(f"   Values: {temperatures[-3]}°C, {temperatures[-2]}°C, {temperatures[-1]}°C")
    print()
    
    print("4. Additional Slicing Examples:")
    print(f"   First 5 hours: temperatures[:5] = {temperatures[:5]}")
    print(f"   Hours 2-8: temperatures[2:8] = {temperatures[2:8]}")
    print(f"   Every other hour: temperatures[::2] = {temperatures[::2]}")
    
    return {
        "full_data": temperatures,
        "first_last": [temperatures[0], temperatures[-1]],
        "afternoon_peak": afternoon_peak,
        "last_three_hours": last_three_hours
    }

if __name__ == "__main__":
    print("Starting Temperature Analysis...\n")
    results = temperature_analysis()
    print("\n=== Analysis Complete ===")
    print(f"Summary of extracted data:")
    print(f"  - First and last: {results['first_last']}")
    print(f"  - Afternoon peak: {results['afternoon_peak']}")
    print(f"  - Last 3 hours: {results['last_three_hours']}")