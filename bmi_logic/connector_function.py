import json
from .bmi_calculator import BMICalculator


def get_bmi_calculated(json_data):
    """
    This Function Takes JSON as Input and Returns JSON data as output.
    Sample Input: ["Gender": "Male", "HeightCm": 171, "WeightKg": 96]
    Sample Output: [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96,
        "BMI": 32.83, "BMICategory": "Moderately Obese", "HealthRisk": "Malnutrition Risk"}]
    :return: JSON
    """
    ovname = BMICalculator.BMI_CONSTANTS.get('OW')[0]
    data = {}
    new_json = []
    over_weight_people_count = 0
    for dt in json_data:
        person = BMICalculator(dt.get('Gender'), dt.get('HeightCm'), dt.get('WeightKg'))
        bmi = person.calculate_bmi()
        bmi_cat, health_risk = person.bmi_category_and_health_risk()
        if bmi_cat == ovname:
            over_weight_people_count = over_weight_people_count + 1
        new_json.append({
            'Gender': dt.get('Gender'),
            'HeightCm': dt.get('HeightCm'),
            'WeightKg': dt.get('WeightKg'),
            'BMI': bmi,
            'BMICategory': bmi_cat,
            'HealthRisk': health_risk
        })
    ovcount = {'OverWeightCount': over_weight_people_count}
    data['People'] = new_json
    return json.dumps([ovcount, data])


if __name__ == '__main__':
    pass
    # import time
    #
    # time_before = time.time()
    # with open('heavy_data.json') as json_file:
    #     json_data = json.load(json_file)
    #
    # output_json = get_bmi_calculated(json_data)
    # time_after = time.time()
    # print(time_after - time_before)
    # print(output_json[:50])