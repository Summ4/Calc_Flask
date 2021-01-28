from math import sqrt

from flask import Flask, render_template, request

app = Flask(__name__, template_folder="template")


@app.route('/')
def main():
    return render_template('entry.html')


@app.route('/entry', methods=['GET', 'POST'])
def send(sm=sum):
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'დამატება':
            sum = float(num1) + float(num2)
            return render_template('result.html', result=sum, num1=num1, num2=num2)

        elif operation == 'გამოკლება':
            sum = float(num1) - float(num2)
            return render_template('result.html', result=sum, num1=num1, num2=num2)

        elif operation == 'გამრავლება':
            sum = float(num1) * float(num2)
            return render_template('result.html', result=sum, num1=num1, num2=num2)

        elif operation == 'გაყოფა':
            sum = float(num1) / float(num2)
            return render_template('result.html', result=sum, num1=num1, num2=num2)
        elif operation == 'ახარისხება':
            sum = pow(float(num1), float(num2))
            return render_template('result.html', result=sum, num1=num1, num2=num2)
        elif operation == 'ფესვი':
            sum = sqrt(float(num1))
            return render_template('result.html', result=sum, num1=num1, num2=num2)
        else:
            return render_template('entry.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    num1 = request.form['num1']
    num2 = request.form['num2']
    sum = request.form['result']

    return render_template('result.html',
                           num1=num1,
                           num2=num2,
                           result=sum)

if __name__ == '__main__':
    app.run(debug=True)
