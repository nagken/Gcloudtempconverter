from flask import Flask, render_template, request
from tempconvert.Converter import UnitConverter

app = Flask(__name__)
converter = UnitConverter()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    value = request.form['value']
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']

    try:
        value = float(value)
        converted_value = converter.convert_temperature(value, from_unit, to_unit)
    except ValueError:
        converted_value = None

    return render_template('results.html', value=value, from_unit=from_unit, to_unit=to_unit,
                           converted_value=converted_value)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
