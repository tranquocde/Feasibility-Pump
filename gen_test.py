import json
import random

def generate_constraints(num_constraints):
    constraints = []
    for _ in range(num_constraints):
        eq = [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20) ,  random.randint(1, 20) ,  random.randint(1, 20)]
        if random.choice([True, False]):
            constraints.append({"eq": eq, "ge": random.randint(1, 10)})
        else:
            constraints.append({"eq": eq, "le": random.randint(20, 30)})
    return constraints

def generate_json_files(num_files, constraints_per_file):
    for i in range(num_files):
        data = {
            "min": [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20) ,  random.randint(1, 20) ,  random.randint(1, 20)],
            "constrs": generate_constraints(constraints_per_file)
        }
        filename = f'constraints_{i+1}.json'
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f'Generated {filename}')
import sys
constraints_per_file = int(sys.argv[1])
generate_json_files(10, constraints_per_file)