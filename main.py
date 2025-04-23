import json
import os

DATA_FILE = 'data.json'

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
        
def create(person):
    data = load_data()
    if data:
        max_id = max(person['id'] for person in data)
    else:
        max_id = 0 

    person['id'] = max_id + 1
    data.append(person)
    save_data(data)
    print("Person created successfully!")

def read():
    data = load_data()
    if not data:
        print('No entries found!')
    for person in data:
        print(f"ID: {person['id']}, Name: {person['name']}, Age: {person['age']}")

def update(person_id, updates):
    data = load_data()
    for person in data:
        if person['id'] == person_id:
            person.update(updates)
            save_data(data)
            print('Person updated.')
            return
    print('Person not found.')    
    
def delete(person_id):
    data = load_data()
    new_data = [person for person in data if person['id'] != person_id]
    if len(data) != len(new_data):
        save_data(new_data)
        print('Person deleted.')
    else:
        print('Person not found.')

def menu():
    while True:
        print("\nSimple Python CRUD")
        print("1. Create person")
        print("2. View people")
        print("3. Update person")
        print("4. Delete person")
        print("5. Exit")

        choice = int(input('Choose an option: ').strip())

        if choice == 1:
            name = input('Enter name: ')
            age = input('Enter age: ')
            create({'name': name, 'age': age})

        elif choice == 2:
            read()

        elif choice == 3:
            person_id = int(input('Enter ID to update: '))
            name = input('New name: ')
            age = input('New age: ')
            updates = {}
            if name: updates['name'] = name
            if age: updates['age'] = age
            update(person_id, updates)

        elif choice == 4:
            person_id = int(input('Enter ID to delete: '))
            delete(person_id)

        elif choice == 5:
            print('Exiting... Goodbye!')
            break

        else:
            print('Invalid option... Try again.')

if __name__ == "__main__":
    menu()
