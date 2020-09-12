from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123thisisit@localhost/BMI_values'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://awfgiaytanalom:be92994f79552595f94138cd09117fd97b4cbedd71b35dacee4d375bbfda7368@ec2-3-214-46-194.compute-1.amazonaws.com:5432/d8fe62eoh9if6c?sslmode=require'  
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ ='data'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120) , unique = True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    BMI = db.Column(db.Float)
    

    def __init__(self,email , height , weight , BMI):
        self.email = email
        self.height = height
        self.weight = weight
        self.BMI = BMI
        

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])

def success():
    #get_(VARIABLE NAME) is the local variable of the success function that we get from the user via the website
    if request.method == 'POST':
        get_email = request.form['email_name']
        get_height = request.form['height_in_cm']
        height_calc = get_height
        get_weight = request.form['weight_in_kg'] 
        BMI_value = int(get_weight) / (int(height_calc)/100 * int(height_calc)/100)
        #print(type(height))
        
        
        if (db.session.query(Data).filter(Data.email == get_email).count() == 0):
            data = Data(get_email,get_height,get_weight,BMI_value)
            db.session.add(data)
            db.session.commit()
            average_BMI = db.session.query(func.avg(Data.BMI)).scalar()
            average_BMI = round(average_BMI)
            count = db.session.query(Data.BMI).count()
            #print(average_BMI)
            #get_height = int(get_height)/100
            #get_height = int(get_height)
            send_email(get_email , get_height , get_weight ,BMI_value , average_BMI , count)
            return render_template("success.html")

        else:
            return render_template("index.html" , 
            text = "Super Sorry but we've already got that email in our database! Try with a new e-mail address to get your BMI Index!")    

if __name__ == '__main__':
    app.debug = True
    app.run()
    #db.create_all()    

