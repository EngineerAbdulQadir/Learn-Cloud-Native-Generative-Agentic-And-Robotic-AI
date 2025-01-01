# GloProg (GloVersity) Class 09

Welcome to the repository for GloProg (GloVersity) Class 09, held on -- / -- / ----.

### **💼 Business Problem and Solution**  
A business solves **modern problems** and makes money by offering valuable solutions. Here's an example:

- **Problem**: 🏦 People stand in long queues at banks to pay bills.
- **Solution**: 💳 **Digital Payment System** allows people to pay online and avoid queues!


### **📚 Table of Contents**  
1. 🔑 Variables  
2. 🧮 Data Types  
3. 💻 Python Dynamic Nature  
4. 🧰 Type Hints in Google Colab  
5. 📝 Working with Variables  
6. 💬 Comments and Documentation  
7. 🔎 Exploring Object Methods and Attributes  
8. 🔄 Variable Overwriting  
9. 🔡 Concatenation in Python


### **1️⃣ Variables**  
Variables store different types of data in Python. Here's a breakdown of **data types**:

- **int**: Numbers without decimals (e.g., `11`, `1000`) 🧮  
- **str**: Text (e.g., `"Wajahat"`, must be inside **quotes**) 📜  
- **float**: Decimal numbers (e.g., `1.5`, `6.9`) 🌊  
- **list**: A collection of items (e.g., `[1, "apple", 3.5]`) 📋  
- **bool**: True/False values for conditions (e.g., `True`, `False`) ✅❌  
- **dict**: Key-value pairs (e.g., `{"name": "Wajahat", "age": 15}`) 📖  
- **set**: A collection of unique values (e.g., `{1, 2, 3}`) 🌟


### **2️⃣ Python Dynamic Nature**  
Python is **dynamic**! You don't have to define data types explicitly, but for clarity, you can use **type hints**.

📘 **Example**:
```python
def add(x: int, y: int) -> int:
    return x + y
```

To learn how to use **type hints** in Google Colab, check out this guide: [Type Hints in Colab](https://stackoverflow.com/questions/63142182/to-what-extent-does-google-colab-support-python-typing) 📚✨


### **3️⃣ Working with Variables**  
Variables are like **placeholders** for storing data. You can check a variable's data type using the **type() function**.

👨‍🏫 **Example**:
```python
x = 5
print(type(x))  # Output: <class 'int'>
```

**📋 Commenting**: Use `#` to add comments in your code (explanations ignored by Python).  
```- Example: `# This is a comment```


### **4️⃣ Methods and Attributes**  
Every **object** in Python has **methods** (functions that perform actions) and **attributes** (properties or characteristics).  
- 🎯 If there are round brackets (`()`), it's a **method**.  
- 🌟 Without brackets, it's an **attribute**.

💻 **Using `dir()` to Explore**:
```python
print([i for i in dir(age) if '__' not in i])
```
This reveals the methods and attributes for the `age` object. 👀


### **5️⃣ Variable Overwriting**  
Variables can be **overwritten**, meaning their values can be changed at any time.

🔄 **Example**:
```python
x = 10
x = 20  # Overwriting x
print(x)  # Output: 20
```

### **6️⃣ Concatenation**  
Joining strings together in Python is called **concatenation**. You can do it using the `+` operator or an **f-string**.

🧑‍🏫 **Example**:
```python
teacher_name = "Sir Wajahat"
print("Hello " + teacher_name)  # Using +
print(f"Hello {teacher_name}")  # Using f-string
```
✨ **Output**:  
`Hello Sir Wajahat`  
`Hello Sir Wajahat`


### 🎨 **Where to Add Animations**  
Here are some ideas for adding animations to make your content pop:

1. **Business Problem and Solution**:  
   - Add an animation of a bank queue followed by a smooth transition to a person using a phone to pay bills online.
   
2. **Variables Section**:  
   - Show icons of data types (e.g., numbers, strings) being stored inside boxes (variables) with labels like "int", "str", etc.

3. **Python is Dynamic**:  
   - Show dynamic, colorful transitions between different data types (numbers changing into strings, etc.).
   
4. **Methods and Attributes**:  
   - Animate a method performing an action (e.g., a character waving) vs. an attribute staying still (e.g., a character’s age).

5. **Concatenation**:  
   - Animate strings combining together like pieces of a puzzle forming a message.
  
## Overriding In Python
```
# Initialize variables for runs and wickets
runs = 0  # Batsman's score starts at 0
wickets = 0  # Bowler's wickets start at 0

# Assignment operators to update scores during the match
# Batsman scores runs
runs += 4  # Batsman hits a 4
print(f"Batsman scored {runs} runs!")  # Output: Batsman scored 4 runs!

runs += 6  # Batsman hits a 6
print(f"Batsman scored {runs} runs!")  # Output: Batsman scored 10 runs!

# Bowler takes wickets
wickets += 1  # Bowler takes 1 wicket
print(f"Bowler took {wickets} wicket!")  # Output: Bowler took 1 wicket!

wickets += 2  # Bowler takes 2 more wickets
print(f"Bowler took {wickets} wickets!")  # Output: Bowler took 3 wickets!
```
---