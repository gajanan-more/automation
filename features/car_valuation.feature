Feature: Car Valuation Automation
  To ensure the valuation process is accurate,
  I want to validate car details from the input file
  with the expected output.

  Scenario: Validate car details from the input file
    Given the input file "data/car_input.txt"
    And the expected output file "data/car_output.txt"
    When I extract the car registration numbers
    And I fetch the car details from the valuation website
    Then the car details should match the expected output
