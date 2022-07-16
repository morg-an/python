from flask import Flask
from helper import pets
app = Flask(__name__)


@app.route('/')
def index():
    return '''
  <h1>Adopt a Pet!</h1>
  <p> Browse through the links below to find your new furry friend: </p>
  <ul>
    <li> <a href='/animals/dogs'> Dogs </a></li>
    <li> <a href='/animals/cats'> Cats </a></li>
    <li> <a href='/animals/rabbits'> Rabbits </a></li>
  </ul>
  '''


@app.route('/animals/<pet_type>')
def animals(pet_type):
    i = 0
    html = f'''
  <h1> List of {pet_type} </h1>
  <ul> 
  '''
    for pet in pets[pet_type]:
        animal_dict = pets[pet_type][i]
        animal_name = animal_dict.get('name')
        new_url = fr'/animals/{pet_type}/{i}'
        html = html + f'<li><a href = {new_url}>{animal_name} </a></li>'
        i += 1
    html = html + '</ul>'
    return html


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    pet_name = pet.get('name')
    pet_image = pet.get('url')
    pet_desc = pet.get('description')
    pet_breed = pet.get('breed')
    pet_age = pet.get('age')
    return f'''
  <h1>{pet_name}</h1>
  <img src={pet_image}>
  <p>{pet_desc}</p>
  <ul>
  <li>{pet_breed}</li>
  <li>{pet_age}</li>
  </ul>
  '''
