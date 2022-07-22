from datetime import datetime
from flask import *
from web_scraping import *
from db import *
import json


app = Flask(__name__)

# adding the data in the database
@app.route('/scrape_data_api', methods = ["POST","GET"])
def scrape_data_api():
    url = request.form["username"]
    try:
        data = scraping(url)
        new = UserInfo(user_name = data[0]['title'],user_role = data[0]['role'],user_company = data[0]['company'],user_university = data[0]['university'],
                   user_connections = data[0]['connections'],user_profile_link = data[0]['profile url'])
        session.add(new)
        session.commit()
        return jsonify(
            data = str(new),
            message = "Successfully scrape",
            status = 200
        )
    except Exception as e:
        return jsonify(
            message = e,
            status = 500
            )


#Showing all the data
@app.route('/show_data', methods = ["POST","GET"])
def show_data():
    if request.method == "GET":
        try:
            Data=[]
            result = session.query(UserInfo).all()
            for i in result:   
                data={
                    "data" : i.to_dict(),
                   
                }
                Data.append(data)
                
            return jsonify(
            UserData = Data,
            message = "succesfully show the data",
            status = 200
        )
        except Exception as e:
            return jsonify(
                message = e,
                status = 500
            )
            
#Showing the data by filtering
@app.route('/show_filter_data', methods = ["POST","GET"])
def show_filter_data():
    if request.method == "GET":
        try:
            # U_Data=[]
            username = request.form['username']
            result = session.query(UserInfo).filter_by(user_name = username).first()
            return jsonify(
            UserData = result.to_dict(),
            message = "succesfully filter the data",
            status = 200
        )
        except Exception as e:
            return jsonify(
                message = e,
                status = 500
            )
            
## updating the data
@app.route('/updating_data', methods = ["POST","GET"])
def updating_data():
    if request.method == "POST":
        try:
            username = request.form['username']
            result = session.query(UserInfo).filter_by(user_name = username).first()
            result.user_name = "Muhammad Kumail"
            session.commit()
            return jsonify(
                data = result.to_dict(),
                message = "succesfully update the data",
                status = 200
            )
        except Exception as e:
            return jsonify(
                 message = e,
                status = 500
            )


# Deleting the data
@app.route('/deleting_data',methods = ["POST","GET"])
def deleting_data():
    try:
        username = request.form["username"]
        result = session.query(UserInfo).filter_by(user_name = username).first()
        session.delete(result)
        session.commit()
        return jsonify(
                message = "Sucesfully delete the data",
                status = 200
            )
    except Exception as e:
        return jsonify(
            message = e,
            status = 500
        )
            

if(__name__ == '__main__'):
    app.run(debug = True, port = 5001)
