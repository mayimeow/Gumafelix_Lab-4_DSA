from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    error = None

    if request.method == 'POST':
        input_string = request.form.get('inputString', '')

        if not input_string:
            error = "Please enter a valid input string."
        elif any(char.isalpha() for char in input_string):
            
            result = input_string.upper()
        else:
            error = "Input should contain at least one alphabetical character."

    return render_template('touppercase.html', result=result, error=error)


@app.route('/circle_area', methods=['GET', 'POST'])
def circle_area():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            if radius >= 0:
                area = 3.14159 * radius**2 
                result = f"The area of the circle with a radius of {radius} is {area:.2f} square units."
            else:
                result = "Radius should be a non-negative number."
        except ValueError:
            result = "Invalid input. Please enter a valid number for the radius."

    return render_template('circle_area.html', result=result)

@app.route('/triangle_area', methods=['GET', 'POST'])
def triangle_area():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            if base >= 0 and height >= 0:
                area = 0.5 * base * height 
                result = f"The area of the triangle with a base of {base} and height of {height} is {area:.2f} square units."
            else:
                result = "Base and height should be non-negative numbers."
        except ValueError:
            result = "Invalid input. Please enter valid numbers for the base and height."

    return render_template('triangle_area.html', result=result)


@app.route('/works')
def works():
    return render_template('works.html')  

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
