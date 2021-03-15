import os
from config import app,api
from api.Model import Model

api.add_resource(Model,'/api/model')


if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5005, debug=True)