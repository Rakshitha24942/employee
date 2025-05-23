from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']

        # Basic validation
        if not name or not email or not department:
            return "All fields are required!", 400

        return render_template('result.html', name=name, email=email, department=department)
    
    return render_template('form.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
