# GloProg (GloVersity) Class 11

Welcome to the repository for GloProg (GloVersity) Class 11, held on -- / -- / ----.

### **1. Paradigm:** 🧠💻
Programming paradigms refer to the style or approach in which programs are written. A programming paradigm shapes how you think about and solve programming problems.

**Linear Programming:**
- In the context of programming, linear programming refers to a structured, sequential flow of execution. It follows a straight line of steps or operations, as opposed to event-driven or parallel execution. Each line of code runs one after the other without interruption unless a specific control structure (like loops or conditionals) alters this flow.

**Structured Programming:**
- Structured programming is a subset of procedural programming that emphasizes dividing code into manageable blocks. It promotes clear, readable code by breaking down a large problem into smaller functions or procedures, making the code easy to follow, debug, and maintain. 📝✅


### **2. ChatGPT Model Interaction:** 🤖💬
We explored interactive sessions with an advanced model of ChatGPT. This highlighted the capabilities of AI in natural language understanding, dialogue, and assistance in programming. This practical session helped improve communication and problem-solving via AI tools. 🛠️✨

### **3. Control Structures:** 🔄🛑
Control structures are fundamental building blocks in programming that control the flow of execution of code. These include:
- **Loops (e.g., `for`, `while`)**
- **Conditionals (e.g., `if`, `else`, `elif`)**
- **Functions**
- **Exception Handling (`try/except`)**

**Example of a simple `if` structure:**
```python
if True:
    print("Pakistan 🇵🇰")
    print("Zindabad 🎉")
```
This snippet prints "Pakistan" and "Zindabad" because the condition `True` is always true.

### **4. Comprehensive Structures:** 🔍
**Comprehensive if-else Style:**  
This is a shorthand for writing conditional expressions in Python.

**Example (corrected syntax):**
```python
result = true_block if logic else else_block
```
Here, if the `logic` evaluates to `True`, the `true_block` is executed, otherwise, the `else_block` runs. ⚙️💡

### **5. Grading System Examples:** 🏅

#### **Grading System 1:** 🧑‍🏫
```python
percentage: int = 75

if percentage >= 80:
    print("A+")
elif percentage >= 70:
    print("A")
elif percentage >= 60:
    print("B")
elif percentage >= 50:
    print("C")
elif percentage >= 40:
    print("D")
elif percentage >= 33:
    print("Happy")
else:
    print("Fail")
```
**Explanation:**  
This program takes a percentage value and returns the corresponding grade based on the conditions provided. It uses an `if-elif-else` structure to check the percentage and print the appropriate grade. 

#### **Grading System 2:** 📝
```python
percentage: int = 90

if percentage >= 0 and percentage < 40:
    print("Fail")
elif percentage >= 40 and percentage < 50:
    print("D")
elif percentage >= 50 and percentage < 60:
    print("C")
elif percentage >= 60 and percentage < 70:
    print("B")
elif percentage >= 70 and percentage < 80:
    print("A")
elif percentage >= 80 and percentage < 100:
    print("A+")
else:
    print("Invalid")
```
This program refines the grading scale by including an explicit range check for each grade, ensuring the percentage falls within valid ranges before printing the grade.

### **6. Loops in Python:** 🔄

Python offers two main types of loops:
1. **`while` loop:** This loop continues as long as a certain condition is true.
2. **`for` loop:** This iterates over a sequence (such as a string, list, or tuple).

**While Loop Example:**
```python
counter: int = 0
while counter <= 10:
    print(counter)
    counter += 1
```
**Explanation:**  
This loop prints numbers from 0 to 10. The loop runs until the condition `counter <= 10` becomes false. ⏳

**For Loop Example:**
```python
for letter in "Wajahat":
    print(letter)
```
**Explanation:**  
This loop iterates through each character in the string "Wajahat" and prints it one by one. 📜

### **7. Usage of `zip` and `unzip` Functions:** 🔗🔓

- **`zip` function:** Combines two or more iterables (like lists, tuples) into tuples.
- **`unzip` function:** Splits zipped objects back into separate iterables.


### **8. Error Handling in Python:** ⚠️🛠️
Error handling ensures that a program can respond to unexpected situations (e.g., wrong user input) gracefully. The `try/except` structure helps to catch exceptions and handle them without crashing the program.

### **9. Login/Signup System in Python (Example Code):** 🖥️🔑

Here's a professional version of the login/signup page created during the class:

```python
users = {}

def signup():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Please try again.")
    else:
        password = input("Enter a new password: ")
        users[username] = password
        print("Signup successful! 🎉")

def login():
    username = input("Enter your username: ")
    if username in users:
        password = input("Enter your password: ")
        if users[username] == password:
            print("Login successful! 🎉")
        else:
            print("Incorrect password. ❌")
    else:
        print("Username not found. ❌")

def main():
    while True:
        choice = input("Do you want to login or signup? (login/signup/exit): ").lower()
        if choice == 'login':
            login()
        elif choice == 'signup':
            signup()
        elif choice == 'exit':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please choose login, signup, or exit.")

main()
```
**Explanation:**  
- This script allows users to sign up with a username and password, and then log in. If a user tries to sign up with an existing username, it will prompt them to try again. The login function checks for valid credentials before allowing access.

---