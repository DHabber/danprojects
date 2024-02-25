from flask import Flask, render_template, request
import json
from table_rolling_funcs import roll_on_table, generate_random_world, npc_encounter_generator

app = Flask(__name__)
with open('tables.json', encoding='utf-8') as f:
        data = json.load(f)
categories = list(data.keys())
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tablesroller')
def tablesroller():
    
    return render_template('tablesroller.html', categories=categories)

@app.route('/generate_text', methods=['POST'])
def generate_text():
    category = request.form['category']
    random_text = roll_on_table('tables.json', category)
    return render_template('tablesroller.html', categories=categories, random_text=random_text)

@app.route('/generate_random_world', methods=['POST'])
def generate_random_world_text():
    random_text = generate_random_world('tables.json')
    return render_template('tablesroller.html', categories=categories, random_text=random_text)

@app.route('/generate_random_encounter', methods=['POST'])
def generate_random_encounter_text():
    number = int(request.form['number'])
    random_text = npc_encounter_generator(number)
    return render_template('tablesroller.html', categories=categories, random_text=random_text)

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True)
    # http://localhost:5000/ 