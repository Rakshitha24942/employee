from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    employee = None

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']

        # Bundle the data into a dictionary
        employee = {
            'name': name,
            'email': email,
            'department': department
        }

    return render_template('form.html', employee=employee)

if __name__ == "__main__":
    app.run(debug=True)
