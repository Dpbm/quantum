from flask import Flask, request
from papers_please import PapersPlease

app = Flask(__name__)

@app.route("/create-circuit", methods=['POST'])
def hello_world():
    inputs = request.get_json()
    bribe = inputs['bribe']
    false_info = inputs['false_info']
    wanted = inputs['wanted']
    passport = inputs['passport']
    other_documents = inputs['other_documents']

    pp = PapersPlease()
    pp.create_circuit(bribe, false_info, wanted, passport, other_documents)
    pp.save_circuit_image()

    return pp.get_states()

