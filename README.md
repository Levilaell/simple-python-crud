# 🐍 Simple Python CRUD (No Frameworks)

This is a basic **command-line CRUD application** built in **pure Python**, using a `.json` file to store data.  
It's a great example project for learning how to work with data persistence, Python dictionaries, and loops.

---

## 💡 Features

- ✅ Create a person (with name and age)  
- 📋 Read (list all people)  
- 🔄 Update a person's data  
- ❌ Delete a person  
- 🗃️ Data stored in `data.json`  
- 📌 All written in **pure Python** — no external libraries or frameworks

---

## 📁 Project Structure

```
simple-crud/
├── main.py         # main script with all logic
└── data.json       # local file used as database
```

---

## ▶️ How to Run

1. Make sure you have **Python 3.10+** installed  
2. Clone or download this project  
3. Run the script:

```bash
python main.py
```

---

## 🧠 How It Works

- **Data loading**: On startup, it checks if `data.json` exists and loads it into memory.
- **Data saving**: Each time you add, update, or delete, the file is overwritten with updated data.
- **Unique ID generation**: IDs are assigned based on the highest current ID, ensuring uniqueness even if entries are deleted.

---

## 📚 Example Use

```
Simple Python CRUD
1. Create person
2. View people
3. Update person
4. Delete person
5. Exit
```

---

## 📦 Dependencies

No external dependencies. Just Python’s built-in modules:
- `json`
- `os`

---

## 📝 Educational Purpose

This project was made for **learning purposes**, to practice:
- File handling
- Working with JSON
- Python dictionaries and loops
- Basic input/output in the terminal

Feel free to modify and expand it!

---

## 📜 License

MIT License — feel free to use and adapt this project for personal or educational use.
