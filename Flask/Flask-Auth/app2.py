from flask import Flask
from flask import render_template_string
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class Helloworld(Resource):
    def get(self):
#         return render_template_string('''<!doctype html>
# <html>
#     <head>
#         <link rel="stylesheet" href="css url"/>
#     </head>
#     <body>
#         <p>Hello, World!</p>
#     </body>
# </html>
# ''')
        return {'hello':'world'}
api.add_resource(Helloworld,'/')

cats =[]
class CatNames(Resource):
    def get(self,name):
        print(cats)
        for cat in cats:
            if cat.get('name')==name:
                return cat
        return {name:"Not found"},404

    def post(self,name):
        cat = {'name':name}
        cats.append(cat)
        print(cats)
        return cat
    
    def delete(self,name):
        for index,cat in enumerate(cats):
            if cat.get('name')==name:
                dc = cats.pop(index)
                return {'Note':'delete successfully','deleted cat':dc}
        return {name:'not found to delete'}


class AllNames(Resource):
    def get(self):
        return {'cats':cats}

api.add_resource(CatNames,'/cat/<string:name>')
api.add_resource(AllNames,'/cats')


if __name__ =='__main__':
    app.run(debug=True)