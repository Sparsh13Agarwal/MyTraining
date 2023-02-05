#jwt -> authentications
from flask_jwt import JWT,jwt_required
from secure_check import authenticate,identity
from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
api = Api(app)
jwt = JWT(app,authenticate,identity)



class Helloworld(Resource):
    def get(self):
        return {'hello':'world'}
api.add_resource(Helloworld,'/')

cats =[]  
class CatNames(Resource):
    @jwt_required()
    def get(self,name):
        
        print(cats)
        for cat in cats:
            if cat.get('name')==name:
                return cat
        return {name:"Not found"},404

    @jwt_required()
    def post(self,name):
        cat = {'name':name}
        cats.append(cat)
        print(cats)
        return cat

    @jwt_required()
    def delete(self,name):
        for index,cat in enumerate(cats):
            if cat.get('name')==name:
                dc = cats.pop(index)
                return {'Note':'delete successfully','deleted cat':dc}
        return {name:'not found to delete'}


class AllNames(Resource):
    
    @jwt_required()
    def get(self):
        return {'cats':cats}

api.add_resource(CatNames,'/cat/<string:name>')
api.add_resource(AllNames,'/cats')


if __name__ =='__main__':
    app.run(debug=True)