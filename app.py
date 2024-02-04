from flask import Flask, render_template, request
import currency

app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        from_currency=request.form['from_currency']
        to_currency=request.form['to_currency']
        amount=request.form['amount']
        result=currency.convert_currency(from_currency,to_currency,amount)
        return render_template('results.html',result=result)
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)
