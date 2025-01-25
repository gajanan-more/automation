import pytest
from pytest_bdd import given, when, then, parsers
from src.car_extractor import extract_registration_numbers
from src.car_valuation_api import fetch_car_details
from src.data_comparator import load_expected_output, compare_results

# Shared variables to hold state between steps
input_file_path = None
expected_file_path = None
actual_results = None
expected_results = None

@given(parsers.parse('the input file "{file_path}"'))
def input_file(file_path):
    global input_file_path
    input_file_path = file_path

@given(parsers.parse('the expected output file "{file_path}"'))
def expected_file(file_path):
    global expected_file_path
    expected_file_path = file_path

@when("I extract the car registration numbers")
def extract_registrations():
    global actual_results
    registration_numbers = extract_registration_numbers(input_file_path)
    actual_results = [fetch_car_details(reg) for reg in registration_numbers]

@when("I fetch the car details from the valuation website")
def fetch_car_details_step():
    # This step is combined with the previous one since it's a part of fetching details.
    pass

@then("the car details should match the expected output")
def compare_actual_with_expected():
    global expected_results
    expected_results = load_expected_output(expected_file_path)
    mismatches = compare_results(actual_results, expected_results)
    assert not mismatches, f"Mismatches found: {mismatches}"
