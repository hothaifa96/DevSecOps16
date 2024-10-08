from flask import Flask,jsonify,request
# import jsonify

foods = [
    {'id':1,'name':'pizza','price':60.0},
    {'id':2,'name':'sushi','price':38.0},
    {'id':3,'name':'flafel','price':28.0}
    ]

app = Flask(__name__)

@app.get('/foods')
def get_all_foods():
    return foods

@app.post('/foods')
def add_food():
    data = request.json
    data['id'] = foods[-1]['id']+1
    foods.append(data)
    return 'added !!!'

@app.delete('/foods/<int:id>')
def delete_food(id):
    for food in foods:
        if food['id'] == id:
            foods.remove(food)
            return 'deleted !!!' ,200
    return 'no foods to delete'

    
if __name__== '__main__':
    app.run(port=5000,host='0.0.0.0')