from flask import  Flask,request,jsonify
import random
import requests
app=Flask(__name__)

@app.route("/",methods=['GET']) 
def respond():
    req=request.args
    print(req) #ImmutableMultiDict([('name', 'Animesh')])

    return "You have reached the root endpoint"

  
#curl -d '{"emp":{"name":"Advait","age":"20"},"work":{"job":"stud"}}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000 

#curl -d '{"name":"Advait","age":"20"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000 

#http://6b9a2fcc.ngrok.io  --localhost to the webhost generate the dynamic url using tunneling
#ngrok http 5000

  

url="http://numbersapi.com/"
@app.route("/getfact",methods=['POST'])
def getfact():
    req=request.get_json() #json--dictionary
    intent=req.get("queryResult").get("intent").get("displayName")
    number=req.get("queryResult").get("parameters").get("number")
    qtype=req.get("queryResult").get("parameters").get("type")
    if intent=="Trivia_Numbers":
        if qtype=="random":
            qtype=random.choice(["math","trivia","year"])
        qurl=url+ str(int(number)) + "/" +qtype + "?json"
        res=requests.get(qurl).json()["text"]
        print(res)
    return jsonify({"fulfillmentText":res})  #printing in DialogFlow      
     
    print(req) #server side print --POST "name:Advait"
    return jsonify({"fulfillmentText":"Flask Server Hit"}) #client side printing 
   

app.run()