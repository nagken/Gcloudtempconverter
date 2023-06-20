from tempconvert.Converter import UnitConverter

class UserInterface:
    def __init__(self, converter):
        self.converter = converter

    def collect_input(self):
        value = float(input("Enter the numerical value: "))
        from_unit = input("Enter the input unit of measure: ")
        to_unit = input("Enter the target unit of measure: ")
        student_response = input("Enter the student's numeric response: ")

        return value, from_unit, to_unit, student_response

    def display_output(self, value, from_unit, to_unit, student_response, grading_result):
        print(f"\nInput Numerical Value: {value}")
        print(f"Input Unit of Measure: {from_unit}")
        print(f"Target Unit of Measure: {to_unit}")
        print(f"Student Response: {student_response}")
        print(f"Grading Result: {grading_result}\n")

    def grade_response(self, student_response, converted_value):
        rounded_student_response = round(float(student_response), 1)
        rounded_converted_value = round(converted_value, 1)

        if rounded_student_response == rounded_converted_value:
            return 'correct'
        else:
            return 'incorrect'

    def run(self):
        while True:
            try:
                value, from_unit, to_unit, student_response = self.collect_input()
                converted_value = self.converter.convert_temperature(value, from_unit, to_unit)
                grading_result = self.grade_response(student_response, converted_value)
            except ValueError:
                grading_result = 'invalid'

            self.display_output(value, from_unit, to_unit, student_response, grading_result)

            continue_input = input("Do you want to convert another temperature? (yes/no): ")
            if continue_input.lower() != 'yes':
                break


converter = UnitConverter()
ui = UserInterface(converter)
ui.run()
