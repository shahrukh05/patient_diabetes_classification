from flask import Flask,render_template,request
import pickle

app = Flask(__name__) 


#load the model

model = pickle.load(open('model\logistic_regression_80_diabetic.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/diabetic',methods=['post'])
def diabetic2():
    preg = int(request.form.get('preg'))
    plas = int(request.form.get('plas'))
    pres = int(request.form.get('pres'))
    skin = int(request.form.get('skin'))
    test = int(request.form.get('test'))
    mass = int(request.form.get('mass'))
    pedi = int(request.form.get('pedi'))
    age = int(request.form.get('age'))
    result = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    print(result)
    if result[0]==1:
        diab = "Person is Diabetic."
    else:
        diab = "Person is Not Diabetic."
    print(diab)
    return render_template('predict.html',data = diab)

app.run(debug=True)
