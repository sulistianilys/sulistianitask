from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/data', methods=['POST'])
def receive_data():
    if request.method == 'POST':
 
        if request.is_json:
            data = request.get_json() 
            air_quality = data.get('air_quality')  
         
            print(f"Received Air Quality: {air_quality} PPM")

            return jsonify({"Air Quality": air_quality}), 200
        else:
            return jsonify({'error': 'Unsupported Media Type, expecting application/json'}), 415

if _name_ == '_main_':
    app.run(host='192.168.102.112', port=5000)