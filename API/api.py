from flask import Flask, request, jsonify,abort
import uuid
from threading import Thread
app = Flask(__name__)

def kickoff_crew(job_id:str,stock:str):
    print(f'Crew is working on {stock} with job_id {job_id}')
    # Setup Crew
    # Run Crew

    
    # Do some work
    print(f'Crew has finished working on {stock}')

@app.route('/api/crew', methods=['POST'])
def run_crew():
    data = request.json
    if not data or 'stock' not in data:
        abort(400,description='stock is required')
    
    job_id = str(uuid.uuid4())

    stock = data['stock']

    # Run crew on thread
    thread = Thread(target=kickoff_crew , args=(job_id,stock))
    thread.start()

    return jsonify({'job_id':job_id}),200

@app.route('/api/crew/<job_id>', methods=['GET'])
def get_status(job_id):
    return jsonify({'message': f'Crew is running job {job_id}'}),200

if __name__ == '__main__':
    app.run(debug=True,port=3001)