from flask import Flask, render_template, request
from tempconvert.Converter import UnitConverter

app = Flask(__name__)
converter = UnitConverter()


def grade_response(student_response, converted_value):
    if isinstance(student_response, (int, float)) and round(student_response, 1) == round(converted_value, 1):
        return 'correct'
    else:
        return 'incorrect'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    value = request.form['value']
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']
    student_response = request.form['student_response']

    try:
        value = float(value)
        converted_value = converter.convert_temperature(value, from_unit, to_unit)
        grading_result = grade_response(float(student_response), converted_value)
    except ValueError:
        converted_value = None
        grading_result = 'invalid'

    return render_template('results.html', value=value, from_unit=from_unit, to_unit=to_unit,
                           student_response=student_response, converted_value=converted_value,
                           grading_result=grading_result)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
