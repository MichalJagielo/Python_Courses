#! python3

from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def start():
    name = ''
    height = ''
    weight = ''
    bmi = ''
    if request.method == "POST" and "username" in request.form:
        name = request.form.get("username")
        height = float(request.form.get("userheight"))
        weight = float(request.form.get("userweight"))
        bmi = bmi_calc(weight, height)
        
    return render_template("index.html",
                            name=name,
                            height=height,
                            weight=weight,
                            bmi = bmi)

def bmi_calc(weight, height):
    bmi = round(weight / ((height/100)**2),1)
    if bmi < 18.5:
        return f'{bmi} > Underweight'
    elif 18.5 <= bmi <= 24.9:
        return f'{bmi} Normal'
    elif 25 <= bmi <= 29.9:
        return f'{bmi} > Overweight'
    else:
        return f'{bmi} > Obese'
    


app.run()

