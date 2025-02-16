# Timetable Generator

This project is a **Genetic Algorithm-based** timetable generator for schools. It ensures that subjects are assigned optimally based on weekly constraints while preventing subject repetition within a day.

## Features
- Generates **optimal school timetables** using **genetic algorithms**.
- Ensures each subject gets allocated **as per weekly constraints**.
- Assigns **teachers** to subjects.
- Displays a **progress bar** for real-time tracking.
- Supports **mutation and crossover** for optimized scheduling.

## Requirements
Ensure you have Python installed. Install dependencies using:
```bash
pip install tqdm
```

## Usage
Run the script using:
```bash
python timetable_generator.py
```

Modify the weekly subject constraints and teacher assignments in the `if __name__ == "__main__":` section to fit your needs.

## Input Constraints
- **Subjects**: Defined in `subjects` list.
- **Weekly Allocation**: Defined in `weekly_constraints` dictionary.
- **Teachers**: Defined in `teachers` dictionary.
- **Days & Periods**: Defined in `days` and `periods_per_day`.

## Example Output
```
Monday: Bengali (RKM), Math (TS), English (DKD), History (SPB)...
Tuesday: Geography (NKS), Life Science (APD), Math (TS), Computer (SKB)...
...
```

## Customization
- Modify **subjects, teachers, and constraints** in the script.
- Adjust **mutation and crossover probabilities** for different results.

## License
This project is open-source and free to use.
