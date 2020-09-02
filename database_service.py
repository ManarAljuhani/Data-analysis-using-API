from flask import Flask, jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.dialects.postgresql import JSON

#initialize flask app 
app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
#default route to 127.0.0.1:3000
@app.route('/')
def home():
    return"HELLO WORLD" 

@app.route('/get_data_count/<label_name>,<count1>', methods=['GET'])

def get_data_count(label_name, count):
   
   try:
      label_name = str(request.args.get('label_name'))
      
      count = int(request.args.get('count'))
      
      result ="your chosen label name is".format(label_name)

      return jsonify(result)
   except:
      return "Error in using method get_sum!"
@app.route('/get_data/<int> , <int>', methods=['GET'])

def get_data(int,int):
   
   try:
      count = int(request.args.get('count'))
      
      sort_order= int(request.args.get('sort_order'))
       

      return jsonify(result)
   except:
      return "Error in using method get_sum!"


#stat the API by port 3000
if __name__ == "__main__":
  app.run(host= '0.0.0.0', port=3000)
