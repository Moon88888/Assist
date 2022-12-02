### Integrate HTML With Flask
### HTTP verb GET And POST
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

# @app.route('/success/<int:score>')
# def success(score):
#     res=""
#     if score>=50:
#         res="PASS"
#     else:
#         res="FAIL"

#     return render_template('result.html',result=res)


# @app.route('/fail/<int:score>')
# def fail(score):
#     return "The Person has failed and the marks is "+ str(score)

# ### Result checker
# @app.route('/results/<int:marks>')
# def results(marks):
#     result=""
#     if marks<50:
#         result='fail'
#     else:
#         result='success'
#     return redirect(url_for(result,score=marks))

# ### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
ls1 = []
ls2 = for x in request.form.values()
ls3 = []
for i in ls2:
    if ls2[i] == ls1[i]:
        ls3.append[i]
        

    



if __name__=='__main__':
    app.run(debug=True)