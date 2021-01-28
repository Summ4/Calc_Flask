from math import sqrt

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('entry.html')


@app.route('/entry', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']


        if operation == 'დამატება':
            sum = int(num1) + int(num2)
            return render_template('result.html', result=sum, num1=num1, num2=num2)

        elif operation == 'გამოკლება':
            sum = int(num1) - int(num2)
            return render_template('result.html', result=sum, num1=num1, num2=num2)

        elif operation == 'გამრავლება':
            sum = int(num1) * int(num2)
            return render_template('result.html', result=sum, num1=num1, num2=num2)

        elif operation == 'გაყოფა':
            sum = int(num1) / int(num2)
            return render_template('result.html', result=sum, num1=num1, num2=num2)
        elif operation == 'ახარისხება':
            sum = pow(num1, num2)
            return render_template('result.html', result=sum, num1=num1, num2=num2)
        elif operation == 'ფესვი':
            sum = sqrt(num1)
            return render_template('result.html', result=sum, num1=num1, num2=num2)
        else:
            return render_template('entry.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    num1 = request.form['num1']
    num2 = request.form['num2']
    sum = request.form['result']

    return render_template('result.html',
                           the_first=num1,
                           the_second=num2,
                           result=sum)

if __name__ == '__main__':
    app.run(debug=True)
