from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']

        try :
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            if type(num1)==float or type(num1)==int or type(num2)==float or type(num2)==int:
                if(operation=='add'):
                    r=num1+num2
                    print('Adding')
                    result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
                if (operation == 'subtract'):
                    r = num1 - num2
                    result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
                if (operation == 'multiply'):
                    r = num1 * num2
                    result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
                if (operation == 'divide'):
                    r = num1 / num2
                    result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            else :
                result = custom_exception_msg(num1,num2)

        except Exception as e:
            result = ' Please provide a int instead of str or alnum'
            return render_template('results.html',result=result)

        return render_template('results.html',result=result)

def custom_exception_msg(fnum,snum):
        raise Exception('Please Enter Valid Number, instead of '+ type(fnum) + ' or ' + type(snum))
        #return int(fnum),int(snum)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)



if __name__ == '__main__':
    app.run()
