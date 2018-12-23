from flask import Flask, render_template, request
app = Flask(__name__)

#This dictates where page will load
@app.route('/banana', methods=['GET', 'POST'])
#function name doesn't matter
def wolololo():
    #Load the value if this is send a request
    if request.method == 'POST':
        age = request.form['age']

        return render_template('age.html', age=age)
    #If nor equest is sent, load the home page
    return render_template('index.html')

if __name__ == "__main__":
        app.run()
