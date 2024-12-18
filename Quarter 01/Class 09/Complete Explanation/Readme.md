# GloProg (GloVersity) Class 09 (Complete Explanation)

Welcome to the repository for GloProg (GloVersity) Class 09, held on -- / -- / ----.

### Purpose of this lesson:
The purpose of this lesson is to teach students how to interact with AI using **variables**. By learning this, students can understand how to customize AI responses by feeding it different pieces of information, like names, ages, or other details.

For example, instead of manually writing out questions or descriptions, they can store those details in variables and let the AI generate personalized answers. This is important because it shows how coding can make tasks more dynamic and interactive, preparing them for more advanced applications in programming and AI.

### **Step 1: Download the Magic Helper Functions** 🧙‍♂️✨
You start by downloading a special helper file that lets you talk to the AI like a chatbot!

```python
!curl -o helper_functions.py https://raw.githubusercontent.com/panaversity/learn-cloud-native-modern-ai-python/main/07_natural_language_programming/02_ai_python_for_beginners/course1_basics/Lesson_9/helper_functions.py
```

🖱️ **Press run** to download the magic tools!

### **Step 2: Bring in the Magic Function** 🪄
Now, let's bring in the function so you can talk to the AI!

```python
from helper_functions import print_llm_response
```

### **Step 3: Ask the AI a Question** 🤔💬
Time to ask the AI simple questions. It’s like talking to a smart friend who knows everything!

**Example:**
```python
print_llm_response("What is the capital of France?")
```

🏙️ The AI will say: **"The capital of France is Paris."** 🗼

### **Step 4: Introducing Variables** 🧑‍💻📦
A variable is like a **box** that holds information, like a name or number. Instead of typing the same thing over and over, you put it in a variable.

**Example:**
```python
name = "Otto Matic"
dog_age = 21 / 7  # Otto is 3 years old in dog years!
```

### **Step 5: Ask the AI Using Variables** 🐕💡
Let’s tell the AI to describe Otto’s life if he were a dog. We can use the variables we created!

**Example:**
```python
print_llm_response(f"If {name} were a dog, he would be {dog_age} years old. Describe his energy level, interests, and behavior.")
```

🐾 The AI might say:
"Otto would be in his early adulthood, full of energy and curiosity!"

### **Step 6: Fixing Variable Names** 🛠️❌
Uh oh! Sometimes, we make mistakes when naming variables. Let’s fix a problem where we used spaces or special characters.

**Bad Code:**
```python
driver's vehicle = "dinosaur car"  # Wrong because of the apostrophe!
```

**Fixed Code:**
```python
drivers_vehicle = "dinosaur car"  # No special characters here!
```

### **Step 7: Create Fun Stories with AI** 🦄🚗🌈
You can make the AI write creative stories using variables like a **unicorn** racing a **dinosaur car**!

**Example:**
```python
driver = "unicorn"
vehicle = "dinosaur car"
favorite_planet = "Pluto"

print_llm_response(f"Write a 300-word story about a {driver} racing a {vehicle} on {favorite_planet}.")
```

🌍 The AI will write a magical story about a unicorn on Pluto!

### **Step 8: Practice Fixing Code** 🧩🔧
Try to fix broken code! Here’s an example of code that needs some fixing.

**Broken Code:**
```python
1favorite-book = "1001 Ways to Wear a Hat"  # Oops, variable names can't start with numbers!
```

**Fixed Code:**
```python
favorite_book = "1001 Ways to Wear a Hat"  # Much better!
```

### **Step 9: Ask AI for Recommendations** 🎮🎬🍕🎶
You can now create your own variables with your favorite things and ask the AI to give you recommendations!

**Example:**
```python
favorite_game = "Minecraft"
favorite_movie = "Harry Potter"
favorite_food = "Pizza"

print_llm_response(f"Based on my love for {favorite_game}, {favorite_movie}, and {favorite_food}, recommend me a new song to listen to.")
```

🎧 The AI will suggest a cool new song based on your favorites!


Now you’ve learned how to code and create fun prompts with an AI! 🎉

---