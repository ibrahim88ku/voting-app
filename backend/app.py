from flask import Flask
app=Flask(__name__)
votes={"cats":0,"dogs":0}

@app.route("/vote/<animal>")
def vote(animal):
    if animal in votes:
        votes[animal]+=1
    return str(votes)

if __name__=="__main__":
    app.run(host="0.0.0.0")
