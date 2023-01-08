#Import necessary modules
#import pymongo as py  
mongodb = ("mongodb://localhost:27017/")
#Create database
data=["StudentDatabase"]
A=data["Student_details"]
#Import the student.json dataset
import pandas as pd
df = pd.read_json("students.json",lines=True)

df_DICT=df.to_dict("records")
df_DICT
#Insert the students record into the collection
A.insert_many(df_DICT)
#Find the student name who scored maximum scores in all (exam, quiz and homework)?
List=[]
for i in A.find({}):
    exam=i["scores"][0]["score"]
    quiz=i["scores"][1]["score"]
    homework=i["scores"][2]["score"]
    Total=exam+quiz+homework   
    i['total']=Total
    L.append(i)
    
max = pd.DataFrame('L')
print("Student name who scored max in all types:",max['name'].iloc[max["total"].idxmax()])

#Find students who scored below average in the exam and pass mark is 40%?
L=[]
for i in A.find({'scores.0.score':{'$gt':40,'$lte':65}},{'_id':0,'name':1}):
     L.append(i)
pd.DataFrame(L)    

#Find students who scored below pass mark and assigned them as fail, and above pass mark as pass in all the categories
L1=[]
for i in A.find({'$and':[{'scores.0.score':{'$lte':40}},{'scores.1.score':{'$lte':40}},{'scores.2.score':{'$lte':40}}]}):
    i["Result"]="Fail"
    L.append(i)
fail=pd.DataFrame(L)

L2=[]
for i in A.find({'$and':[{'scores.0.score':{'$gt':40}},{'scores.1.score':{'$gt':40}},{'scores.2.score':{'$gt':40}}]}):
    i["Result"]="pass"
    L2.append(i)
p=pd.DataFrame(L2)

Result = [p,fail]
result=pd.concat(Result)
result

#Find the total and average of the exam, quiz and homework and store them in a separate collection
List=[]
for i in A.find({}):
    dic={}
    exam=i["scores"][0]["score"]
    quiz=i["scores"][1]["score"]
    homework=i["scores"][2]["score"]
    total=exam+quiz+homework
    a=total/3
    dic["id"]=i['_id']
    dic["Name"]=i["name"]
    dic["Total"]=total
    dic["Avgerage"]=a
    List.append(dic)

df=pd.DataFrame(List)
df1=df.to_dict("records")
df1

B=data["Average"]
B.insert_many(df1)

#Create a new collection which consists of students who scored below average and above 40% in all the categories
List1=[]
for i in A.find({'$and':[{'scores.0.score':{'$gt':40,'$lte':70}},{'scores.1.score':{'$gt':40,'$lte':70}},{'scores.2.score':{'$gt':40,'$lte':70}}]}):
    List1.append(i)
DF2=pd.DataFrame(List1)
belowAverage=DF2.to_dict("records")
C=data["Below_Average"]
C.insert_many(belowAverage)

#Create a new collection which consists of students who scored below the fail mark in all the categories
List2=[]
for i in A.find({'$and':[{'scores.0.score':{'$lte':40}},{'scores.1.score':{'$lte':40}},{'scores.2.score':{'$lte':40}}]}):   
    List2.append(i)
DF3=pd.DataFrame(List2)
fail=DF3.to_dict("records")
D=data["Falied"]
D.insert_many(fail)

#Create a new collection which consists of students who scored above pass mark in all the categories
List3=[]
for i in A.find({'$and':[{'scores.0.score':{'$gt':40}},{'scores.1.score':{'$gt':40}},{'scores.2.score':{'$gt':40}}]}):
   
    List3.append(i)
DF4=pd.DataFrame(List3)
P=DF4.to_dict("records")

E=data["passed"]
E.insert_many(P)








