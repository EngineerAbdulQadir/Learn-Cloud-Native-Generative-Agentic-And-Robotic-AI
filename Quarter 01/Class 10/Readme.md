# GloProg (GloVersity) Class 10

Welcome to the repository for GloProg (GloVersity) Class 10, held on -- / -- / ----.

## Table of Contents:
### 1. **Setting up Google Colab** 💻:
Google Colab is an online environment where you can write and execute Python code. It’s super useful because you can use powerful cloud-based GPUs and TPUs for free, making it perfect for machine learning tasks! 🚀


### 2. **First Command** 🛠️:
```bash
!curl -o helper_functions.py https://raw.githubusercontent.com/panaversity/learn-cloud-native-modern-ai-python/main/07_natural_language_programming/02_ai_python_for_beginners/course1_basics/Lesson_9/helper_functions.py
```
This command does the following:

- **`!curl`**: The exclamation mark (`!`) means this is a shell command, not Python. `curl` is a tool to download files from the internet 🌐.
- **`-o helper_functions.py`**: The `-o` flag tells the command to save the file as `helper_functions.py`.
- **URL**: This URL points to a GitHub repository where the file is located 📂.

In summary, this downloads a Python file called `helper_functions.py` from GitHub to your local environment. 📥



### 3. **Second Command** 🧩:
```python
from helper_functions import *
```
This command is used to **import all functions** from the `helper_functions.py` file you just downloaded.

- **`from helper_functions`**: Refers to the file.
- **`import *`**: Imports *everything* (functions, classes, etc.) from that file so you can use them in your code without rewriting them. 🔄


### 4. **Creating a Gemini API Key through Google AI Studio** 🔑:
To use the Gemini API, you need an API key. Here’s how you can get it:
- **Step 1:** Go to [Google AI Studio](https://ai.google.com/studio/) 🌍.
- **Step 2:** Sign in with your Google account 🔐.
- **Step 3:** Create a new project 🚧.
- **Step 4:** Enable the API you need (like Gemini) 📊.
- **Step 5:** Go to "Credentials" and click "Create API Key" 🔑.
- **Step 6:** Copy the API key for use in your Python code 📝.


### 5. **Functions in Python** 🧑‍💻:
Functions are blocks of reusable code that perform a specific task. They usually have parentheses at the end (for parameters).

### **How to Create a Function in Python** 📝:
Use `def` to define a function, followed by the function name and parentheses for parameters.

```python
def greet():
    print("Hello World")
```

- `def`: Defines the function.
- `greet`: The name of the function.
- `print("Hello World")`: The function will print this message when called 🗣️.
- `greet()`: This line calls the function.

##### **Output**:
```
Hello World 🌍
```


#### 6. **Dependencies and Dev Dependencies** 📦:
- **Dependencies:** Essential tools or packages needed to run your project. In the example of a half-fried egg 🍳, oil, eggs, and salt are your *dependencies*—you need them to cook.
  
- **Dev Dependencies:** These are tools needed only during development 🛠️, like the frying pan 🥘. You don’t serve it with the egg but you need it to cook the egg!

In programming, dependencies are like libraries or packages your code needs, while dev dependencies are tools you use only when writing the code (like linters or debuggers).


### 7. **Functions Stored in Variables** 📂:
In Python, you can store functions inside variables! Here's how:

```python
greet_function = greet
greet_function()  # This will print "Hello World" 🌍
```

Here, `greet_function` refers to the original `greet()` function, so calling it works the same way.

### 8. **Return vs. Print in Functions** 🔄:
- **`print`:** Outputs something to the console but doesn’t return a value to be used later.
- **`return`:** Gives a value back to your code that can be stored or used elsewhere.

Example:
```python
def add(a, b):
    return a + b

sum = add(5, 3)
print(sum)  # Output will be 8 🎯
```


### 9. **Dynamic vs. Static Functions** 🧠:
- **Static Functions:** Always behave the same. For example, a function that always prints "Hello World" 🌎.
- **Dynamic Functions:** Change behavior based on input or conditions. They can adapt based on what you pass into them 🛠️.


### 10. **Parameters in Functions** 🎛️:
- **Default Parameters:** These parameters have default values that are used if no arguments are passed.
- **Custom Parameters:** Values that you provide when calling the function.

Example:
```python
def greet(name="Guest"):
    print("Hello, " + name)
```
If you don’t pass a name, the function will default to "Guest."

### 11. **Compiling vs. Interpreting** 🖥️:
- **Compiling:** Converts your entire code into machine language before running it, like C or C++ 🛠️.
- **Interpreting:** Executes code line by line, like Python 🐍. This allows you to run Python code interactively.


### 12. **Modules and Modular Approach** 🧩:
- **Modules:** Python files that contain useful code (functions, classes) that you can import into other programs.
- **Modular Approach:** Breaking your code into small, reusable pieces (modules). It's like dividing a big task into smaller, manageable parts.

Example:
```python
import math
print(math.sqrt(16))  # Using the sqrt function from the math module 📐
```

### 13. **Using Custom-Made Functions** 📜:
If you want to use someone else’s custom function, you either:
1. Download their code file 📥.
2. Copy their code directly into your program.

Then you can use their functions just like you would with any built-in Python function.

### 14. **LLM (Large Language Model) Limitation** ⚠️:
When working with LLMs, like GPT, they usually can’t access real-time data 🌐 (e.g., the latest news). That’s why they might not provide the most up-to-date information unless they're specifically integrated with real-time data sources.

### Tasks: 
1. What is AI agent
2. What is Langchain and are its uses
3. What is langraph

---