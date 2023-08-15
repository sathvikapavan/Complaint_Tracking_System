from shutil import RegistryError
import mysql.connector as mysql
from flask import Flask,render_template,request,session,redirect
b=0

db=mysql.connect(
    host='localhost',
    user='root',
    password='chaitu',
    database='jyothi'
)
cur = db.cursor()
app=Flask(__name__)
app.secret_key = '30c0'

@app.route('/')
def openPage():
    return render_template('open.html')
@app.route('/register2.html')
def signupPage():
    return render_template('register2.html')
@app.route('/login.html')
def loginPage():
    return render_template('login.html')
@app.route('/open.html')
def logoutPage():
    return render_template('open.html')
@app.route('/about.html')
def aboutPage():
    return render_template('about.html')
@app.route('/complaints.html')
def complainPage():
    return render_template('complaints.html')
@app.route('/adminlogin.html')
def AloginPage():
    return render_template('adminlogin.html')
@app.route('/Lcomplaint.html')
def LPage():
    return render_template('Lcomplaint.html')
@app.route('/Tcomplaint.html')
def TPage():
    return render_template('Tcomplaint.html')
@app.route('/teachingcomplaint.html')
def TeachPage():
    return render_template('teachingcomplaint.html')
@app.route('/Hcomplaint.html')
def HPage():
    return render_template('Hcomplaint.html')
@app.route('/Ccomplaint.html')
def CPage():
    return render_template('Ccomplaint.html')
@app.route('/Ecomplaint.html')
def EPage():
    return render_template('Ecomplaint.html')
@app.route('/dashboard.html')
def DashPage():
    return render_template('dashboard.html')
@app.route('/admindashboard.html')
def ADashPage():
    return render_template('admindashboard.html')
  
@app.route('/profile.html')
def profile():
    cur.execute('select * from student_credentials1')
    result=cur.fetchall()
    for x in result:
        if(b==x[1]):
            return render_template('profile.html',Name=x[0],RegID=x[1],dept=x[2],email=x[3],phno=x[5])
    
@app.route('/library.html')
def library():
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='LIBRARY'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            dummy.append(x[4])
            dummy.append(x[5])
            data.append(dummy)        
    return render_template('library.html',complaints=data)

@app.route('/hostel.html')
def hostel():
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='HOSTEL'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            dummy.append(x[4])
            dummy.append(x[5])
            data.append(dummy)
    return render_template('hostel.html',complaints=data)

@app.route('/canteen.html')
def canteen():
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='CANTEEN'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            dummy.append(x[4])
            dummy.append(x[5])
            data.append(dummy)
    print(data)
    return render_template('canteen.html',complaints=data)

@app.route('/transport.html')
def transport():
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='TRANSPORT'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            dummy.append(x[4])
            dummy.append(x[5])
            data.append(dummy)
    print(data)
    return render_template('transport.html',complaints=data)

@app.route('/events.html')
def event():
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='EVENTS'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            dummy.append(x[4])
            dummy.append(x[5])
            data.append(dummy)
    return render_template('events.html',complaints=data)

@app.route('/teachingmethodologies.html')
def teaching():
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='TEACHING METHODOLOGIES'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            dummy.append(x[4])
            dummy.append(x[5])
            data.append(dummy)
    return render_template('teachingmethodologies.html',complaints=data)

@app.route('/mycomplaints.html')
def mycomplaint():
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(b==x[0]):
            dummy=[]
            dummy.append(x[1])
            dummy.append(x[2])
            dummy.append(x[3])
            data.append(dummy)
    return render_template('mycomplaints.html',complaints=data)

@app.route('/collectData',methods=['POST'])
def collectData():
    Name=request.form['Name']
    RegID=request.form['RegID']
    dept=request.form['dept']
    email=request.form['email']
    pwd=request.form['pwd']
    phno=request.form['phno']
    sql='INSERT INTO student_credentials1 (Name,RegID,dept,email,pwd,phno) values (%s, %s,%s, %s, %s, %s)'
    values=(Name,RegID,dept,email,pwd,phno)
    cur.execute(sql,values)
    db.commit()
    return render_template('login.html')

@app.route('/Details',methods=['POST'])
def data():
    RegID=request.form['RegID']
    pwd=request.form['pwd']
    cur.execute('select * from student_credentials1')
    result=cur.fetchall()
    flag=0 
    for x in result:
        if(RegID==x[1] and pwd==x[4]):
            flag=1
            session['RegID']=RegID
            session['pwd']=pwd
            global b
            b=x[1]
            return render_template('dashboard.html')            
    if flag==0:
        msg='INVALID USERNAME OR PASSWORD'
        return render_template('login.html',msg=msg)

@app.route('/Alogin',methods=['POST'])
def Adata():
    Username=request.form['Username']
    pwd=request.form['pwd']
    flag=0
    if(Username=='admin' and pwd=='Kits'):
        flag=1
        session['Username']=Username
        session['pwd']=pwd
        return render_template('admindashboard.html')
    if flag==0:
        msg='INVALID USERNAME OR PASSWORD'
        return render_template('adminlogin.html',msg=msg)

@app.route('/L',methods=['POST'])
def Lcomplain(): 
    complaints=request.form['complaints']
    a='LIBRARY'
    sql='INSERT INTO complaints2 (complaints,category,RegID) values (%s,%s,%s)'
    values=(complaints,a,b)
    cur.execute(sql,values)
    db.commit()
    return render_template('Lcomplaint.html')

@app.route('/T',methods=['POST'])
def Tcomplain():
    complaints=request.form['complaints']
    a='TRANSPORT'
    sql='INSERT INTO complaints2 (complaints,category,RegID) values (%s,%s,%s)'
    values=(complaints,a,b)
    cur.execute(sql,values)
    db.commit()
    return render_template('Tcomplaint.html')

@app.route('/Teach',methods=['POST'])
def Teachcomplain():
    complaints=request.form['complaints']
    a='TEACHING METHODOLOGIES'
    sql='INSERT INTO complaints2 (complaints,category,RegID) values (%s,%s,%s)'
    values=(complaints,a,b)
    cur.execute(sql,values)
    db.commit()
    return render_template('teachingcomplaint.html')

@app.route('/H',methods=['POST'])
def Hcomplain():
    complaints=request.form['complaints']
    a='HOSTEL'
    sql='INSERT INTO complaints2 (complaints,category,RegID) values (%s,%s,%s)'
    values=(complaints,a,b)
    cur.execute(sql,values)
    db.commit()
    return render_template('Hcomplaint.html')

@app.route('/C',methods=['POST'])
def Ccomplain():
    complaints=request.form['complaints']
    a='CANTEEN'
    sql='INSERT INTO complaints2 (complaints,category,RegID) values (%s,%s,%s)'
    values=(complaints,a,b)
    cur.execute(sql,values)
    db.commit()
    return render_template('Ccomplaint.html')
    
@app.route('/E',methods=['POST'])
def Ecomplain():
    complaints=request.form['complaints']
    a='EVENTS'
    sql='INSERT INTO complaints2 (complaints,category,RegID) values (%s,%s,%s)'
    values=(complaints,a,b)
    cur.execute(sql,values)
    db.commit()
    return render_template('Ecomplaint.html')

@app.route('/view/<id>',methods=['post'])
def viewid(id):
    sql="UPDATE complaints2 set view='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='TRANSPORT'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            data.append(dummy)
    return render_template('transport.html',complaints=data)

@app.route('/view1/<id>',methods=['post'])
def viewid1(id):
    sql="UPDATE complaints2 set view='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='LIBRARY'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            data.append(dummy)
    return render_template('library.html',complaints=data)

@app.route('/view2/<id>',methods=['post'])
def viewid2(id):
    sql="UPDATE complaints2 set view='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='HOSTEL'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            data.append(dummy)
    return render_template('hostel.html',complaints=data)

@app.route('/view3/<id>',methods=['post'])
def viewid3(id):
    sql="UPDATE complaints2 set view='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='EVENTS'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            data.append(dummy)
    return render_template('events.html',complaints=data)

@app.route('/view4/<id>',methods=['post'])
def viewid4(id):
    sql="UPDATE complaints2 set view='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='CANTEEN'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            data.append(dummy)
    return render_template('canteen.html',complaints=data)

@app.route('/view5/<id>',methods=['post'])
def viewid5(id):
    sql="UPDATE complaints2 set view='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='TEACHING METHODOLOGIES'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[3])
            data.append(dummy)
    return render_template('teachingmethodologies.html',complaints=data)

@app.route('/process/<id>',methods=['post'])
def processid(id):
    sql="UPDATE complaints2 set process='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='TRANSPORT'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[4])
            data.append(dummy)
    return render_template('transport.html',complaints=data)

@app.route('/process1/<id>',methods=['post'])
def processid1(id):
    sql="UPDATE complaints2 set process='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='LIBRARY'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[4])
            data.append(dummy)

    return render_template('library.html',complaints=data)
  
@app.route('/process2/<id>',methods=['post'])
def processid2(id):
    sql="UPDATE complaints2 set process='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='HOSTEL'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[4])
            data.append(dummy)
    return render_template('hostel.html',complaints=data)

@app.route('/process3/<id>',methods=['post'])
def processid3(id):
    sql="UPDATE complaints2 set process='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='EVENTS'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[4])
            data.append(dummy)
    return render_template('events.html',complaints=data)

@app.route('/process4/<id>',methods=['post'])
def processid4(id):
    sql="UPDATE complaints2 set process='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='CANTEEN'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[4])
            data.append(dummy)
    return render_template('canteen.html',complaints=data)

@app.route('/process5/<id>',methods=['post'])
def processid5(id):
    sql="UPDATE complaints2 set process='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='TEACHING METHODOLOGIES'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[4])
            data.append(dummy)
    return render_template('teachingmethodologies.html',complaints=data)

@app.route('/sort/<id>',methods=['post'])
def sortid(id):
    sql="UPDATE complaints2 set sort='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='TRANSPORT'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[5])
            data.append(dummy)
    return render_template('transport.html',complaints=data)

@app.route('/sort1/<id>',methods=['post'])
def sortid1(id):
    sql="UPDATE complaints2 set sort='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='LIBRARY'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[5])
            data.append(dummy)
    return render_template('library.html',complaints=data)

@app.route('/sort2/<id>',methods=['post'])
def sortid2(id):
    sql="UPDATE complaints2 set sort='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='HOSTEL'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[5])
            data.append(dummy)
    return render_template('hostel.html',complaints=data)

@app.route('/sort3/<id>',methods=['post'])
def sortid3(id):
    sql="UPDATE complaints2 set sort='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='EVENTS'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[5])
            data.append(dummy)
    return render_template('events.html',complaints=data)

@app.route('/sort4/<id>',methods=['post'])
def sortid4(id):
    sql="UPDATE complaints2 set sort='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='CANTEEN'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[5])
            data.append(dummy)
    return render_template('canteen.html',complaints=data)

@app.route('/sort5/<id>',methods=['post'])
def sortid5(id):
    print(id)
    sql="UPDATE complaints2 set sort='1' where cID='"+str(id)+"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    global b
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for x in result:
        if(x[1]=='TEACHING METHODOLOGIES'):
            dummy=[]
            dummy.append(x[0])
            dummy.append(x[2])
            dummy.append(x[5])
            data.append(dummy)
    return render_template('teachingmethodologies.html',complaints=data)

@app.route('/track/<id>',methods=['post','GET'])
def trackid(id):
    cur.execute("select * from complaints2")
    result=cur.fetchall()
    data=[]
    for i in result:
        print(i)
        status=-1
        if(i[3]==int(id)):
            if(i[6]=='1'):
                status=3
                break
            elif(i[5]=='1'):
                status=2
                break
            elif(i[4]=='1'):
                status=1
                break
            else:
                status=0
        print(status)
    return render_template('tracking1.html',status=status)

if __name__=="__main__":
    app.run(debug=True)
