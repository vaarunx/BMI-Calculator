from email.mime.text import MIMEText
import smtplib

def send_email(email , height , weight , BMI , average_BMI ,count):
    #Enter your e-mail address
    from_email = ""
    #Enter your password(e-mail) 
    from_password = ""
    to_email = email

    subject = "BMI Value"
    message = " <h3>Hey there , The BMI Value for your height <strong> <i>%s cm</i> </strong> and your weight <strong> <i>%s kg</i> </strong> is <br> <br> <i>%.4s</i></h3> <br> <br> <br> <h4>  What is the body mass index (BMI)?  </h4> <br>     The body mass index (BMI) is a measure that uses your height and weight to work out if your weight is healthy.<br> <br> <br> <i> <b> If your BMI is: </i> </b> <ul> <li> below <b>18.5</b> – you're in the <i>underweight<i> range </li> <li> between <b>18.5</b> and <b>24.9</b> – you're in the <i>healthy</i> weight range </li> <li>between <b>25</b> and <b>29.9</b> – you're in the <i>overweight</i> range </li> <li>between <b> 30</b> and <b>39.9</b> – you're in the <i>obese</i> range  </li> </ul> <br> <br> <br> <h4> <i>The average BMI is %s from %s users who have used this website to calculate their BMI! </i></h4>" %(height , weight , BMI , average_BMI ,count)
    #message2 = " <i> If your BMI is: </i> <ul> <li> below 18.5 – you're in the underweight range </li> <li> between 18.5 and 24.9 – you're in the healthy weight range </li> <li>between 25 and 29.9 – you're in the overweight range </li> <li>between 30 and 39.9 – you're in the obese range  </li> </ul>"

    msg = MIMEText(message ,'html')

    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email
    

    gmail = smtplib.SMTP("smtp.gmail.com" , 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email , from_password)
    gmail.send_message(msg)