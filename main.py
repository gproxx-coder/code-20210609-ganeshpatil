from bmi_logic.connector_function import get_bmi_calculated
import json


# Open data.json file and read JSON data from it
# Converting JSON to Python for further operations
with open('./data/data.json') as json_file:
    json_data = json.load(json_file)

# Calling connector method which connects BMICalculator to User Input
output_json = get_bmi_calculated(json_data)

print(output_json)