#final page12
from flask import Flask, render_template, request
import random
app = Flask(__name__)
li=[]
random_number = random.randint(1, 100)
print(random_number,"<<<<<<,")

def bottomlist(txtval): #at footer part
    for i in range(50):
        li.append(txtval)
        print(li)
        return render_template("t1.html",marks = txtval,random_number=random_number,li=li,len=len(li))

def compare(txtval):
    if(txtval==random_number):
        print(">> equal to ==")
    elif(txtval>random_number):
        print(">> Large >>>")
    elif(txtval<random_number):
        print(">> Small <<")
    return bottomlist(txtval)
    
def difference(txtval):
    dif=txtval-random_number
    print(">> difference is: ",dif)
    return compare(txtval)
    
    
def isnumber(resultx): #check if its a number 
    txt=resultx
    txtval = txt.split("=")
    check=txtval[1].isdigit()
    if(check!=True):
        print(">> input is not a number")
        print("///RESTART///")
        del li[:]
        return render_template('index1.html')
        # exit(0)
    txtval=int(txtval[1])
    print(">> entered value: ",txtval)
    print(">> random No is : ",random_number)
    return difference(txtval)
        
    # return render_template("t1.html")

@app.route('/')
def student():
    return render_template('index1.html')

@app.route('/index1',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
    # result = request.form
        resultx = request.get_data()
        return isnumber(resultx)
        
