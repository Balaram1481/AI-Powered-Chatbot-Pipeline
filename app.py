from flask import Flask,request

app=Flask(__name__)

@app.route("/")
def home():
    return "Ai SecOps ChatBot Running"

@app.route("/chat")
def chat():
    user_input=request.args.get("msg")

    return f"AI Response: {user_input}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=False)
