from flask import Flask, jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
import numpy as np
import pandas as pd
import pymysql
import psycopg2

connection = psycopg2.connect(user = "postgres",
                                  password = "123456",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "db9")

#initialize flask app
app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
#default route to 127.0.0.1:3000

<<<<<<< HEAD
@app.route('/get_data_count/', methods=['GET'])

def get_data_count():

   try:
      label_name = str(request.args.get('label_name'))
      count = int(request.args.get('count'))
      if label_name == 'positive':
          result=cursor.excute(" SELECT  CLASSIFECATION_NUM FROM  data_input1 where CLASSIFECATION_NUM = 1 LIMIT = '%S'" , count)
      elif label_name == 'negative':
          result=cursor.excute(" SELECT  CLASSIFECATION_NUM FROM  data_input1 where CLASSIFECATION_NUM = 0 LIMIT = '%s'", count)
      else:
          result=cursor.excute(" SELECT  CLASSIFECATION_NUM FROM  data_input1 LIMIT = '%s'", count)
      result= cursor.fetchall()
      return "data fetched correctly"
      return jsonify(len(result))
except:
      return "Error in using method get_data_count!"

@app.route('/get_data/', methods=['GET'])
def get_data():
   try:
      count1 = int(request.args.get('count1'))
      sort_order= int(request.args.get('sort_order'))
      if sort_order == 'ASC':
          result =cursor.excute("SELECT TEXT FROM  data_input LIMIT = '%d' ORDER BY timestamp ASC", count1)
      else :
          result =cursor.excute("SELECT TEXT FROM  data_input LIMIT = '%d' ORDER BY timestamp DESC", count1)
      result = cursor.fetchall()
      return "data fetched correctly"
      return jsonify(result)

   except:
      return "Error in using method get_data!"
connection.commit()
connection.close()
=======
@app.route('/get_data_count/, methods=['GET'])

def get_data_count(label_name, count):

   try:
      label_name = str(request.args.get('label_name'))
      count = int(request.args.get('count'))
      if label_name == 'positive':
          result=cursor.excute(" SELECT  CLASSIFECATION_NUM FROM  data_input1 where CLASSIFECATION_NUM = 1 LIMIT = '%S'" , count)
      elif label_name == 'negative':
          result=cursor.excute(" SELECT  CLASSIFECATION_NUM FROM  data_input1 where CLASSIFECATION_NUM = 0 LIMIT = '%s'", count)
      else:
          result=cursor.excute(" SELECT  CLASSIFECATION_NUM FROM  data_input1 LIMIT = '%s'", count)
      result= cursor.fetchall()
      return jsonify(len(result))
   except:
      return "Error in using method get_data_count!"

   @app.route('/get_data/, methods=['GET'])

   def get_data(count1, sort_order):
      try:
         count1 = int(request.args.get('count1'))
         sort_order = int(request.args.get('sort_order'))
         if sort_order == 'ASC':
            result = cursor.excute("SELECT TEXT FROM  data_input LIMIT = '%d' ORDER BY timestamp ASC", count1)
         else:
            result = cursor.excute("SELECT TEXT FROM  data_input LIMIT = '%d' ORDER BY timestamp DESC", count1)
         result = cursor.fetchall()
         return jsonify(result)

      except:
         return "Error in using method get_data!"

   connection.commit()
   connection.close()
>>>>>>> origin/master
if __name__ == "__main__":
  app.run(host= '0.0.0.0', port=3000)

