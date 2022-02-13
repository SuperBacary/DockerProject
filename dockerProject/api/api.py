from flask import Flask
import json
import random

app = Flask(__name__)
@app.route("/", methods=['GET'])
def getFruit():
    listFruit = ['apple', 'banana', 'orange']
    choiseFruit = listFruit[random.randint(0,2)]
    return json.dumps({"fruit" : choiseFruit})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    print("api Start !")
