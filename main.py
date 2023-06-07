from flask import Flask, render_template, request
from myform import MyForms
from aimanager import QueryResponse

import logging

app = Flask(__name__)



@app.route('/', methods= ["GET", "POST"])
def hompage():
    form = MyForms(meta={'csrf': False})
    question1 = form.ques1.label.text
    question2 = form.ques2.label.text

    if form.validate_on_submit():

        answer1 = form.ques1.data
        answer2 = form.ques2.data

        reply = QueryResponse(answer1=answer1,answer2=answer2,question1=question1,question2=question2)
        form.reply_field.data = reply

    return render_template("index.html", form=form)



if __name__=="__main__":
   app.run(debug=True)

