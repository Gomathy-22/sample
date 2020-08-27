from flask import Flask,render_template,request
app=Flask(__name__)
def funadd(n1,n2):
    return (n1+n2)
def funsub(n1,n2):
    return (n1-n2)
def funDiv(n1,n2):
    return (n1%n2)
def funMul(n1,n2):
    return (n1*n2)
@app.route('/')
def home():
	return render_template("homr.html")
@app.route('/homr', methods=['POST',"GET"])
def calculate():
    if request.method == "POST":
        num1=request.form['Num 1']
        num2=request.form['Num 2']
        num3=request.form['operation']
        if num3 == "Add":
            res=funadd(num1,num2)
        elif num3 == "Sub":
            res=funsub(num1,num2)
        elif num3 == 'Div':
            res=funDiv(num1,num2)
        else:
            res=funMul(num1,num2)
	return render_template('sol.html',m=res)
if __name__== "__main__":
	app.run(debug=True)