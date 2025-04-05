from flask import Flask,jsonify, make_response,request
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Movie

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.json.compact = False

CORS(app)

migrate= Migrate(app,db)
db.init_app(app)

@app.route('/movies',methods=['GET'])
def movies():
    if request.method=='GET':
        movies= [movie.to_dict() for movie in Movie.query.all()]
        return make_response(jsonify(movies), 200)

    return make_response(jsonify({"error":"Method not allowed"}), 405)

if __name__ == '__main__':
    app.run(port=5555,debug=True)