class UnitConverter:
    def __init__(self):
        # Initialize any necessary variables or configurations
        pass

    def convert_temperature(self, value, input_unit, target_unit):
        converted_value = None

        if input_unit == 'Kelvin':
            if target_unit == 'Celsius':
                # Conversion formula: Celsius = Kelvin - 273.15
                converted_value = value - 273.15
            elif target_unit == 'Fahrenheit':
                # Conversion formula: Fahrenheit = (Kelvin * 9/5) - 459.67
                converted_value = (value * 9/5) - 459.67
            elif target_unit == 'Rankine':
                # Conversion formula: Rankine = Kelvin * 9/5
                converted_value = value * 9/5
            else:
                raise ValueError(f"Invalid target unit: {target_unit}")
        elif input_unit == 'Celsius':
            if target_unit == 'Kelvin':
                # Conversion formula: Kelvin = Celsius + 273.15
                converted_value = value + 273.15
            elif target_unit == 'Fahrenheit':
                # Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
                converted_value = (value * 9/5) + 32
            elif target_unit == 'Rankine':
                # Conversion formula: Rankine = (Celsius + 273.15) * 9/5
                converted_value = (value + 273.15) * 9/5
            else:
                raise ValueError(f"Invalid target unit: {target_unit}")
        elif input_unit == 'Fahrenheit':
            if target_unit == 'Kelvin':
                # Conversion formula: Kelvin = (Fahrenheit + 459.67) * 5/9
                converted_value = (value + 459.67) * 5/9
            elif target_unit == 'Celsius':
                # Conversion formula: Celsius = (Fahrenheit - 32) * 5/9
                converted_value = (value - 32) * 5/9
            elif target_unit == 'Rankine':
                # Conversion formula: Rankine = Fahrenheit + 459.67
                converted_value = value + 459.67
            else:
                raise ValueError(f"Invalid target unit: {target_unit}")
        elif input_unit == 'Rankine':
            if target_unit == 'Kelvin':
                # Conversion formula: Kelvin = Rankine * 5/9
                converted_value = value * 5/9
            elif target_unit == 'Celsius':
                # Conversion formula: Celsius = (Rankine - 491.67) * 5/9
                converted_value = (value - 491.67) * 5/9
            elif target_unit == 'Fahrenheit':
                # Conversion formula: Fahrenheit = Rankine - 459.67
                converted_value = value - 459.67
            else:
                raise ValueError(f"Invalid target unit: {target_unit}")
        else:
            raise ValueError(f"Invalid input unit: {input_unit}")

        if converted_value is None:
            raise ValueError("Conversion not implemented for the given input and target units")

        # Round the converted value to the tenths place
        rounded_value = round(converted_value, 1)
        return rounded_value
