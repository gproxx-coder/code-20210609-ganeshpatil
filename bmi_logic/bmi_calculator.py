
class BMICalculator:
    BMI_CONSTANTS = {
        'UW': ['Under Weight', 'Malnutrition Risk'],
        'NW': ['Normal Weight', 'Low Risk'],
        'OW': ['Over Weight', 'Enhanced Risk'],
        'MO': ['Moderately Obese', 'Medium Risk'],
        'SO': ['Severely Obese', 'High Risk'],
        'VSO': ['Very Severely Obese', 'Very High Risk'],
    }

    # Initializing the values so that every person(object)
    # can have its own data associated.
    def __init__(self, gender, height_cm, weight_kg) -> None:
        self.gender = gender
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.height_mtr = self.height_cm / 100
        self.bmi = None
        self.bmi_cat = None
        self.health_risk = None

    def calculate_bmi(self) -> float:
        """
        Method that Simply Calculates BMI
        :return: BMI
        """
        self.bmi = round((self.weight_kg / self.height_mtr ** 2), 2)
        return self.bmi

    def bmi_category_and_health_risk(self) -> tuple:
        """
        Method that Categorize Person on Based on BMI
        We find BMI Category & Health Risk
        :return: BMI Category & Health Risk
        """
        if self.bmi < 18.4:
            self.bmi_cat = BMICalculator.BMI_CONSTANTS.get('UW')[0]
            self.health_risk = BMICalculator.BMI_CONSTANTS.get('UW')[1]
        elif 18.5 <= self.bmi <= 24.9:
            self.bmi_cat = BMICalculator.BMI_CONSTANTS.get('NW')[0]
            self.health_risk = BMICalculator.BMI_CONSTANTS.get('NW')[1]
        elif 25 <= self.bmi <= 29.9:
            self.bmi_cat = BMICalculator.BMI_CONSTANTS.get('OW')[0]
            self.health_risk = BMICalculator.BMI_CONSTANTS.get('OW')[1]
        elif 30 <= self.bmi <= 34.9:
            self.bmi_cat = BMICalculator.BMI_CONSTANTS.get('MO')[0]
            self.health_risk = BMICalculator.BMI_CONSTANTS.get('MO')[1]
        elif 35 <= self.bmi <= 39.9:
            self.bmi_cat = BMICalculator.BMI_CONSTANTS.get('SO')[0]
            self.health_risk = BMICalculator.BMI_CONSTANTS.get('SO')[1]
        elif 40 <= self.bmi:
            self.bmi_cat = BMICalculator.BMI_CONSTANTS.get('VSO')[0]
            self.health_risk = BMICalculator.BMI_CONSTANTS.get('VSO')[1]
        return self.bmi_cat, self.health_risk