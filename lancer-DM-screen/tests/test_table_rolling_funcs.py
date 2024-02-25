import pytest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from table_rolling_funcs import roll_on_table, generate_random_world, npc_encounter_generator

@pytest.fixture(scope="module")
def json_file():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tables.json')

@pytest.mark.parametrize("category", ["World Type", "Defining Natural Feature", "Defining Anthropocentric Feature", "Environments"])
def test_roll_on_table(json_file, category):
    result = roll_on_table(json_file, category)
    assert isinstance(result, str)

def test_generate_random_world(json_file):
    result = generate_random_world(json_file)
    assert isinstance(result, str)

def test_npc_encounter_generator():
    result = npc_encounter_generator(4)
    assert isinstance(result, dict)
    assert all(isinstance(value, int) for value in result.values())
