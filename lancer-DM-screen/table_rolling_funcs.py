import json
import random

def roll_on_table(json_file, category): #changed from generate_random_text
    with open(json_file, encoding='utf-8') as f:
        data = json.load(f)

    if category in data:
        options_from_category = data[category]
        selected_entry = random.choice(options_from_category)
        return selected_entry.get("description", "No description available.")
    else:
        return "Category not found"
    
def generate_random_world(json_file):
    world_text = ""
    tables = ["World Type", "Defining Natural Feature", "Defining Anthropocentric Feature", "Environments"]
    for table in tables:
        world_text += table + ': ' + roll_on_table('tables.json', table) + '\n\n'
    return world_text

def npc_encounter_generator(player_count, json_file='npc_classes_roles.json'):
    with open(json_file, encoding='utf-8') as f:
        data = json.load(f)
    
    enemies = {'Standard': 0, 'Grunt': 0, 'Elite': 0, 'Ultra': 0}
    selectedclasses = generate_enemies_variety()
    selectedclasses_step = 0
    enemy_options = list(enemies.keys())
    while(player_count > 0):
        difficulty_template = random.choice(enemy_options)  
        if difficulty_template == 'Ultra':
            if player_count >= 4:
                template_and_class = 'Ultra' + ' ' +selectedclasses[selectedclasses_step%4]
                enemies[template_and_class] = enemies.setdefault(template_and_class, 0) + 1
                selectedclasses_step += 1
                player_count -= 4
            else:
                enemy_options.remove('Ultra')
        elif difficulty_template == 'Elite':
            if player_count >= 2:
                template_and_class = 'Elite' + ' ' +selectedclasses[selectedclasses_step%4]
                enemies[template_and_class] = enemies.setdefault(template_and_class, 0) + 1
                selectedclasses_step += 1
                player_count -= random.choice([1, 2])
            else:
                enemy_options.remove('Elite')
        elif difficulty_template == 'Grunt':
            template_and_class = 'Grunt' + ' ' +selectedclasses[selectedclasses_step%4]
            enemies[template_and_class] = enemies.setdefault(template_and_class, 0) + random.choice([3, 4])
            selectedclasses_step += 1
            player_count -= 1
        elif difficulty_template == 'Standard':
            template_and_class = 'Standard' + ' ' +selectedclasses[selectedclasses_step%4]
            enemies[template_and_class] = enemies.setdefault(template_and_class, 0) + random.choice([1, 2])
            selectedclasses_step += 1
            player_count -= 1
    
    
    enemies = {key: value for key, value in enemies.items() if value != 0}
    enemies = shuffle_dict(enemies)

    enemy_options = list(enemies.keys())


    return enemies
    
def generate_enemies_variety():
    with open('npc_classes_roles.json', encoding='utf-8') as f:
        data = json.load(f)

    categories = random.choice(['Striker', 'Artillery'])
    dps_class = random.choice(data[categories]).get("Class", "No class available.")
    all_classes = [item['Class'] for category in data.values() for item in category]
    
    selectedclasses = [dps_class]
    for i in range(4):
        selectedclasses.append( random.choice(all_classes))
    return selectedclasses #['Operator', 'Mirage', 'Rainmaker', 'Demolisher', 'Berserker']



def shuffle_dict(d):
    # Convert the dictionary into a list of key-value tuples
    items = list(d.items())
    # Shuffle the list
    random.shuffle(items)
    # Convert the shuffled list back into a dictionary
    shuffled_dict = dict(items)
    return shuffled_dict

json_file = 'tables.json'  # Path to your JSON file
# category = 'mission hook'  # Category you want to select from
# random_hook = generate_random_text(json_file, category)
# world = generate_random_world(json_file)
print(npc_encounter_generator(4))