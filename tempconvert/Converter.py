class UnitConverter:
    def __init__(self):
        # Initialize any necessary variables or configurations
        pass

    def convert_temperature(self, value, input_unit, target_unit):
        if input_unit == target_unit:
            return value

        converted_value = None

        if input_unit == 'Kelvin':
            if target_unit == 'Celsius':
                converted_value = value - 273.15
            elif target_unit == 'Fahrenheit':
                converted_value = (value * 9/5) - 459.67
            elif target_unit == 'Rankine':
                converted_value = value * 9/5
            else:
                raise ValueError(f"Invalid target unit: {target_unit}")
        elif input_unit == 'Celsius':
            if target_unit == 'Kelvin':
                converted_value = value + 273.15
            elif target_unit == 'Fahrenheit':
                converted_value = (value * 9/5) + 32
            elif target_unit == 'Rankine':
                converted_value = (value + 273.15) * 9/5
            else:
                raise ValueError(f"Invalid target unit: {target_unit}")
        elif input_unit == 'Fahrenheit':
            if target_unit == 'Kelvin':
                converted_value = (value + 459.67) * 5/9
            elif target_unit == 'Celsius':
                converted_value = (value - 32) * 5/9
            elif target_unit == 'Rankine':
                converted_value = value + 459.67
            else:
                raise ValueError(f"Invalid target unit: {target_unit}")
        elif input_unit == 'Rankine':
            if target_unit == 'Kelvin':
                converted_value = value * 5/9
            elif target_unit == 'Celsius':
                converted_value = (value - 491.67) * 5/9
            elif target_unit == 'Fahrenheit':
                converted_value = value - 459.67
            else:
                raise ValueError(f"Invalid target unit: {target_unit}")
        else:
            raise ValueError(f"Invalid input unit: {input_unit}")

        if converted_value is None:
            raise ValueError("Conversion not implemented for the given input and target units")

        rounded_value = round(converted_value, 1)
        return rounded_value
