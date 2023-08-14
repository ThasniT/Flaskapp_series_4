# import the Flask library
from flask import Flask, render_template, request
 
 
# Create the Flask instance and pass the Flask constructor the path of the correct module
app = Flask(__name__)
 
 
@app.route('/', methods=['GET', 'POST'])
def operation():
 # If method is POST, get the number entered by user
 # Calculate the square of number and pass it to answermaths
    if request.method == 'POST':
        if(request.form['num1'] == '') or (request.form['num2'] == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
            number1 = request.form['num1']
            number2 = request.form['num2']
            operator=request.form.get('operation')
            if operator=='add':
                res=int(number1)+int(number2)
            elif operator=='sub':
                res=int(number1)-int(number2)
            elif operator=='mul':
                 res=int(number1)*int(number2)
            return render_template('answer.html',
                            result=res, num1=number1,num2=number2)
    # If the method is GET,render the HTML page to the user
    if request.method == 'GET':
        return render_template("operation.html")
 
 
# Start with flask web app with debug as True only
# if this is the starting page
if(__name__ == "__main__"):
    app.run(debug=True)