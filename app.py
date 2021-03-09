from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)
CORS(app)


class HelloWorld(Resource):

    def get(self):
        status = request.args.get('status', type=int)
        if status == 1:
            # call some function here
            return {"message": "ok starting"}
        elif status == 0:
            return {"message": "ok stoping"}
        return {"message": "Sorry, dont know what to do "}


api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    run = app.run(debug=True)
