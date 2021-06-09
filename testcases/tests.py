import json
import os
import time
from unittest import TestCase
from bmi_logic.bmi_calculator import BMICalculator
from bmi_logic.connector_function import get_bmi_calculated

"""
This module contains test cases which can be run by pytest command
And also saves data to `bulk_data.json` file
Format of data will be {"Gender": {}, "HeightCm": {}, "WeightKg": {}}
GENDER_CHOICES: ['Male', 'Female']
Height Range: 120 to 200
Weight Range: 50 to 130
"""

TEST_BMI_CONSTANTS = {
    'UW': ['Under Weight', 'Malnutrition Risk'],
    'NW': ['Normal Weight', 'Low Risk'],
    'OW': ['Over Weight', 'Enhanced Risk'],
    'MO': ['Moderately Obese', 'Medium Risk'],
    'SO': ['Severely Obese', 'High Risk'],
    'VSO': ['Very Severely Obese', 'Very High Risk'],
}


def get_bmi_category_and_health_risk_for_testing(bmi):
    bmi_cat = None
    health_risk = None
    if bmi < 18.4:
        bmi_cat = TEST_BMI_CONSTANTS.get('UW')[0]
        health_risk = TEST_BMI_CONSTANTS.get('UW')[1]
    elif 18.5 <= bmi <= 24.9:
        bmi_cat = TEST_BMI_CONSTANTS.get('NW')[0]
        health_risk = TEST_BMI_CONSTANTS.get('NW')[1]
    elif 25 <= bmi <= 29.9:
        bmi_cat = TEST_BMI_CONSTANTS.get('OW')[0]
        health_risk = TEST_BMI_CONSTANTS.get('OW')[1]
    elif 30 <= bmi <= 34.9:
        bmi_cat = TEST_BMI_CONSTANTS.get('MO')[0]
        health_risk = TEST_BMI_CONSTANTS.get('MO')[1]
    elif 35 <= bmi <= 39.9:
        bmi_cat = TEST_BMI_CONSTANTS.get('SO')[0]
        health_risk = TEST_BMI_CONSTANTS.get('SO')[1]
    elif 40 <= bmi:
        bmi_cat = TEST_BMI_CONSTANTS.get('VSO')[0]
        health_risk = TEST_BMI_CONSTANTS.get('VSO')[1]
    return bmi_cat, health_risk


class TestBMICalculator(TestCase):
    def setUp(self) -> None:
        print("hahaha")
        self.gender = 'Male'
        self.height = 171
        self.weight = 96
        self.expected_bmi = round((self.weight / (self.height / 100) ** 2), 2)
        self.expected_bmi_category, self.expected_health_risk = get_bmi_category_and_health_risk_for_testing(
            bmi=self.expected_bmi)
        self.person = BMICalculator(self.gender, self.height, self.weight)

    def test_bmi_object_getting_created(self):
        self.assertTrue(self.person)
        self.assertEqual(self.person.gender, self.gender)
        self.assertEqual(self.person.weight_kg, self.weight)
        self.assertEqual(self.person.height_cm, self.height)

    def test_correct_bmi(self):
        self.assertEqual(self.person.calculate_bmi(), self.expected_bmi)
        self.assertEqual(self.person.bmi_category_and_health_risk()[0], self.expected_bmi_category)
        self.assertEqual(self.person.bmi_category_and_health_risk()[1], self.expected_health_risk)


class TestConnectorFunction(TestCase):
    def test_correct_ourput(self):
        json_data = [{
            "Gender": "Female",
            "HeightCm": 167,
            "WeightKg": 82
        }]
        expected_data = [{"OverWeightCount": 1}, {"People": [
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82, "BMI": 29.4, "BMICategory": "Over Weight",
             "HealthRisk": "Enhanced Risk"}]}]
        output_json = get_bmi_calculated(json_data)
        self.assertEqual(json.loads(output_json), expected_data)

    def test_correct_people_data(self):
        json_data = [{
            "Gender": "Female",
            "HeightCm": 167,
            "WeightKg": 82
        }]
        expected_data = {"People": [
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82, "BMI": 29.4, "BMICategory": "Over Weight",
             "HealthRisk": "Enhanced Risk"}]}
        output_json = get_bmi_calculated(json_data)
        self.assertEqual(json.loads(output_json)[1], expected_data)

    def test_correct_overweight_count(self):
        json_data = [{
            "Gender": "Female",
            "HeightCm": 167,
            "WeightKg": 82
        }]
        expected_data = {"OverWeightCount": 1}
        output_json = get_bmi_calculated(json_data)
        self.assertEqual(json.loads(output_json)[0], expected_data)


class TestBMICategoriesAndHealthRisk(TestCase):
    def test_underweight(self):
        json_data = [{
            "Gender": "Female",
            "HeightCm": 171,
            "WeightKg": 51
        }]
        expected_over_weight_count = 0
        expected_bmi_category = 'Under Weight'
        expected_health_risk = 'Malnutrition Risk'
        output_json = json.loads(get_bmi_calculated(json_data))
        self.assertIn("OverWeightCount", output_json[0])
        self.assertEqual(output_json[0].get("OverWeightCount"), expected_over_weight_count)
        self.assertIn("People", output_json[1])
        self.assertEqual(output_json[1]["People"][0]["BMICategory"], expected_bmi_category)
        self.assertEqual(output_json[1]["People"][0]["HealthRisk"], expected_health_risk)

    def test_normalweight(self):
        json_data = [{
            "Gender": "Female",
            "HeightCm": 171,
            "WeightKg": 70
        }]
        expected_over_weight_count = 0
        expected_bmi_category = 'Normal Weight'
        expected_health_risk = 'Low Risk'
        output_json = json.loads(get_bmi_calculated(json_data))
        self.assertIn("OverWeightCount", output_json[0])
        self.assertEqual(output_json[0].get("OverWeightCount"), expected_over_weight_count)
        self.assertIn("People", output_json[1])
        self.assertEqual(output_json[1]["People"][0]["BMICategory"], expected_bmi_category)
        self.assertEqual(output_json[1]["People"][0]["HealthRisk"], expected_health_risk)

    def test_overweight(self):
        json_data = [{
            "Gender": "Female",
            "HeightCm": 171,
            "WeightKg": 80
        }]
        expected_over_weight_count = 1
        expected_bmi_category = 'Over Weight'
        expected_health_risk = 'Enhanced Risk'
        output_json = json.loads(get_bmi_calculated(json_data))
        self.assertIn("OverWeightCount", output_json[0])
        self.assertEqual(output_json[0].get("OverWeightCount"), expected_over_weight_count)
        self.assertIn("People", output_json[1])
        self.assertEqual(output_json[1]["People"][0]["BMICategory"], expected_bmi_category)
        self.assertEqual(output_json[1]["People"][0]["HealthRisk"], expected_health_risk)

    def test_moderately_obese(self):
        json_data = [{
            "Gender": "Female",
            "HeightCm": 171,
            "WeightKg": 96
        }]
        expected_over_weight_count = 0
        expected_bmi_category = 'Moderately Obese'
        expected_health_risk = 'Medium Risk'
        output_json = json.loads(get_bmi_calculated(json_data))
        self.assertIn("OverWeightCount", output_json[0])
        self.assertEqual(output_json[0].get("OverWeightCount"), expected_over_weight_count)
        self.assertIn("People", output_json[1])
        self.assertEqual(output_json[1]["People"][0]["BMICategory"], expected_bmi_category)
        self.assertEqual(output_json[1]["People"][0]["HealthRisk"], expected_health_risk)

    def test_severely_obese(self):
        json_data = [{
            "Gender": "Female",
            "HeightCm": 171,
            "WeightKg": 105
        }]
        expected_over_weight_count = 0
        expected_bmi_category = 'Severely Obese'
        expected_health_risk = 'High Risk'
        output_json = json.loads(get_bmi_calculated(json_data))
        self.assertIn("OverWeightCount", output_json[0])
        self.assertEqual(output_json[0].get("OverWeightCount"), expected_over_weight_count)
        self.assertIn("People", output_json[1])
        self.assertEqual(output_json[1]["People"][0]["BMICategory"], expected_bmi_category)
        self.assertEqual(output_json[1]["People"][0]["HealthRisk"], expected_health_risk)

    def test_very_severely_obese(self):
        json_data = [{
            "Gender": "Female",
            "HeightCm": 171,
            "WeightKg": 120
        }]
        expected_over_weight_count = 0
        expected_bmi_category = 'Very Severely Obese'
        expected_health_risk = 'Very High Risk'
        output_json = json.loads(get_bmi_calculated(json_data))
        self.assertIn("OverWeightCount", output_json[0])
        self.assertEqual(output_json[0].get("OverWeightCount"), expected_over_weight_count)
        self.assertIn("People", output_json[1])
        self.assertEqual(output_json[1]["People"][0]["BMICategory"], expected_bmi_category)
        self.assertEqual(output_json[1]["People"][0]["HealthRisk"], expected_health_risk)


class TestHeavyPayload(TestCase):
    def test_1_lac_records(self):
        base_path = os.path.dirname(os.path.dirname(__file__))
        filename = 'data/bulk_data.json'
        try:
            with open(filename) as json_file:
                json_data = json.load(json_file)
        except FileNotFoundError:
            print("Please Run 'random_data_generator/random_json_data_generator.py' file first")
        else:
            time_before = time.time()
            output_json = get_bmi_calculated(json_data)
            time_after = time.time()
            final_time = time_after - time_before
            self.assertLessEqual(final_time, 5)
