
from flask import Flask, jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
import numpy as np
import pandas as pd
import pymysql
import psycopg2
import pickle



connection = psycopg2.connect(user = "postgres",
                                  password = "123456",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "db9")
cursor = connection.cursor()

#initialize flask app
app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)



@app.route('/get_data_count', methods=['GET'])

def get_data_count():
   print("get_data_count called")
   try:
      label_name = str(request.args.get('label_name'))
      count = int(request.args.get('count'))
     
      if label_name == 'positive':
          result= cursor.execute('SELECT classification_num  FROM data_input1 where id <= {}  AND  classification_num =1'.format(count))
      elif label_name == 'negative':
          result =  cursor.execute('SELECT classification_num  FROM data_input1 where id <= {}  AND  classification_num =0'.format(count))
      else:
          result= cursor.execute("SELECT  classification_num FROM  data_input1 LIMIT {}".format(count))
      result= cursor.fetchall()
      return jsonify(len(result))
   except:
      return "Error in using method get_data_count!"

@app.route('/get_data/', methods=['GET'])

def get_data():
   print("get_data called")
   try:
      count1=int(request.args.get('count1'))
      sort =str(request.args.get('sort'))
      
      if sort == 'ASC':
          result = cursor.execute("SELECT TEXT,classification_num  FROM  data_input2 ORDER BY DATE ASC  LIMIT {}" .format(count1))
      else:
          result =cursor.execute('SELECT TEXT ,classification_num FROM  data_input2 ORDER BY DATE DESC  LIMIT {}' .format(count1))
      result = cursor.fetchall()
      print("date fetched correctly")
      return jsonify(result)

   except:
      return "Error in using method get_data!"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3000)

connection.commit()
connection.close()

