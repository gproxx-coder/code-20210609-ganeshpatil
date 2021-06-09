import json
import random
import os

"""
This module will generate N number of Random Data
And also saves data to `bulk_data.json` file
Format of data will be {"Gender": {}, "HeightCm": {}, "WeightKg": {}}
GENDER_CHOICES: ['Male', 'Female']
Height Range: 120 to 200
Weight Range: 50 to 130
"""


def generate_random_json_data_and_save(total):
    json_arr = []
    GENDER_CHOICES = ['Male', 'Female']

    for _ in range(total):
        json_arr.append({"Gender": random.choice(GENDER_CHOICES), "HeightCm": random.randint(120, 200),
                         "WeightKg": random.randint(50, 130)})
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = '/data/bulk_data.json'
    with open(base_path + file_path, 'w') as file:
        file.write(json.dumps(json_arr))


if __name__ == '__main__':
    """
    For generating data you need to copy and paste following line.
    generate_random_json_data_and_save(N)
    Replace N with desired no of records you want.
    """
    pass
