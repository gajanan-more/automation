import re

def extract_registration_numbers(file_path):
    """Extracts vehicle registration numbers from the input file."""
    with open(file_path, 'r') as file:
        content = file.read()

    # Regex pattern for UK registration numbers
    pattern = r'[A-Z]{2}[0-9]{2}\s?[A-Z]{3}'
    registrations = re.findall(pattern, content)

    # Normalize (remove spaces)
    return [reg.replace(" ", "") for reg in registrations]

