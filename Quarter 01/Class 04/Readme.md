# GloProg (GloVersity) Class 04

Welcome to the repository for **GloProg (GloVersity) Class 04**, held on **-- / -- / ----**.

## 📚 Contents
- [Introduction to Variables and Data Types](#introduction-to-variables-and-data-types)
- [Data Formats](#data-formats)
- [Databases](#databases)
- [Primitive Data Types](#primitive-data-types)
- [Development Environment and Containers](#development-environment-and-containers)
- [Creating a "Hello World" Application Using Docker and DevContainers](#creating-a-hello-world-application-using-docker-and-devcontainers)

---

## 🔍 Introduction to Variables and Data Types
Variables are essential components in programming, serving as containers for storing data values. Here's a quick rundown of common data types in Python:

- **Integers**: Whole numbers without a fractional part, e.g., `10`, `-3`.
- **Floats**: Numbers with decimal points, e.g., `3.14`, `-0.01`.
- **Strings**: A sequence of characters used to represent text, e.g., `"name"`, `"email address"`.
- **Datetime**: Stores date and time values, e.g., `2024-08-25 10:00:00`.
- **Collections**:
  - **Lists**: Ordered and mutable collections of items, e.g., `[1, 2, 3]`.
  - **Tuples**: Ordered but immutable collections, e.g., `(1, 2, 3)`.
  - **Dictionaries**: Unordered collections of key-value pairs, e.g., `{"name": "Alice", "age": 30}`.

## 📄 Data Formats
Common data formats used in data exchange and storage:
- **XML (eXtensible Markup Language)**: A markup language that defines rules for encoding documents in a format readable by humans and machines.
- **JSON (JavaScript Object Notation)**: A lightweight data interchange format that's easy to read and write.
- **Protocol Buffers (protobuf)**: A language-neutral mechanism for serializing structured data.

## 🗃️ Databases
1. **Structured Databases**:
   - **Relational Databases (RDBMS)**: Store data in tables. Use SQL to manage data. Examples: MySQL, PostgreSQL.
   - **Use Case**: Detecting repeated values, enforcing data integrity, and managing structured data.

2. **NoSQL Databases**:
   - **Non-Relational Databases**: Store unstructured or semi-structured data. Example: MongoDB.
   - **Use Case**: Handling large volumes of unstructured data like JSON documents.

3. **Graph Databases**:
   - **Graph Databases**: Store and query data with complex relationships. Example: Neo4j.
   - **Use Case**: Social networks, recommendation engines, and knowledge graphs.

## 🔢 Primitive Data Types
- **Integers**: Whole numbers, positive or negative, without decimals.
- **Characters**: Single letters, digits, or symbols.

## 🛠️ Development Environment and Containers
### DEV Containers Extension Installation
- **Dev Container**: A development environment packaged as a Docker container for consistency across machines.
- **One-time Image Creation**: Create the Docker image once and use it for live checking and testing.

### Installing Pylance and Mypy
- **Pylance**: VS Code extension for Python.
- **Mypy**: Static type checker for Python.
  ```bash
  pip install mypy
  ```

---

## 🐳 Creating a "Hello World" Application Using Docker and DevContainers

### Step-by-Step Guide

#### Set Up Docker Environment:
Install Docker and the "Dev Containers" extension in VS Code.

#### Create a Jupyter Notebook Project:
Create a new directory for your project and initialize it.

#### Create a Dockerfile:
Example Dockerfile content:
```
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install jupyter
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

#### Create a DevContainer Configuration:
Create a `.devcontainer` folder and add `devcontainer.json`:
```
{
  "name": "Hello-World Dev Container",
  "dockerFile": "Dockerfile",
  "appPort": [8888],
  "extensions": ["ms-python.python"]
}
```

#### Build and Run the DevContainer:
Open the project in VS Code and use the "Reopen in Container" option.
Run the Jupyter Notebook:

Create `hello_world.ipynb` and add some Python code:
```
print("Hello, World!")
```

#### Accessing the Jupyter Notebook Externally:
Use VS Code's port forwarding to access the notebook from outside the container on port `8888`.

## 📸 Screenshots
### Dockerfile
![Dockerfile Screenshot](https://github.com/user-attachments/assets/3d5d1524-173d-4662-871d-ce807f0edd63)

### DevContainer.json
![Dev Container Screenshot](https://github.com/user-attachments/assets/553f96f0-0d69-4101-9383-9feb7d63b482)

---