# GloProg (GloVersity) Class 06

Welcome to the repository for GloProg (GloVersity) Class 06, held on -- / -- / ----.

## 📖 Table of Contents
1. [🚀 GitHub Setup](#github-setup)
2. [💻 VS Code Shortcuts](#vs-code-shortcuts)
3. [🔍 Data Types](#data-types)
4. [🔠 Cases in Strings](#cases-in-strings)
5. [📊 Variables and Data Types](#variables-and-data-types)
6. [🆔 ID and Directory Functions](#id-and-directory-functions)
7. [🔗 String Concatenation](#string-concatenation)

## 🚀 GitHub Setup

1. **📝 Sign Up on GitHub**: Visit GitHub and create an account if you don't have one.

2. **💾 Install GitHub Desktop**: Download and install GitHub Desktop to manage your repositories with a GUI.

3. **🔑 Log in to GitHub**: Open GitHub Desktop and log in using your GitHub credentials.

4. **🗂️ Creating a New Repository**:
    - Step 1: Create a new repository on your local PC using GitHub Desktop.
    - Step 2: Ensure your repository name is unique to avoid conflicts.
    - Step 3: Open the repository in VS Code using the terminal command: `code .`
    - Step 4: Create a file named `main.py` in the repository.

5. **💾 Committing Changes**: Use GitHub Desktop to commit changes. Committing saves your changes locally.

6. **🌐 Pushing to a Remote Repository**: Convert your local repository to a remote one to secure it and share it online. Use `git push origin` to push all new commits to the remote repository on GitHub.

7. **🔄 Checkout Command**: The `git checkout` command removes files from your VS Code workspace. However, you can restore them by using the `git checkout` command with the specific link or commit hash obtained from GitHub.

8. **🌐 Accessing a Container**: If someone needs to access your container, they must have access to the specific port.

## 💻 VS Code Shortcuts
- **CTRL + Enter**: Run the current code.
- **SHIFT + Enter**: Run code in a new line.
- **ALT + Enter**: Run code in the terminal.

## 🔍 Data Types

1. **Dynamic Data Types**:
   Variables can store any type of data without explicitly specifying the type.
   ```python
   x = 10        # x is an integer
   x = "Hello"   # x is now a string
   x = 3.14      # x is now a float

2. **Static Data Types**
   ```
   age: int = 20      # age can only be an integer
   name: str = "Ali"  # name can only be a string
   ```
## Upper Case Example
```
text = "hello world"
print(text.upper())  # Output: "HELLO WORLD"
```
## Lower Case Example
```
text = "HELLO WORLD"
print(text.lower())  # Output: "hello world"
```
## Title Case Example
```
text = "hello world"
print(text.title())  # Output: "Hello World"
```
## Variables and Data Types
```
name: str = "Abdul Qadir"
print(type(name))  # Output: <class 'str'>
```
## ID and Directory Functions
```
print(id(name))
print(dir(name))
```
## String Concatenation
```
A = "Wizard"
B = "Explains"
C = A + B
print(C)  # Output: "GloProg"
```
---