from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']
        return f"Employee Info: {name}, {email}, {department}"
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)

