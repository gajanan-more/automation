import csv

def load_expected_output(file_path):
    """Load expected output from a CSV file."""
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def compare_results(actual, expected):
    """Compare actual and expected car details."""
    mismatches = []
    for actual_car in actual:
        matching_car = next(
            (car for car in expected if car["VARIANT_REG"] == actual_car["registration"]), 
            None
        )
        if not matching_car or any(
            actual_car[key] != matching_car[key] for key in ["make", "model", "year"]
        ):
            mismatches.append((actual_car, matching_car))
    return mismatches
