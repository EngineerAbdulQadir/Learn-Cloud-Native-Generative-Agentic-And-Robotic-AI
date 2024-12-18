# GloProg (GloVersity) Class 07

Welcome to the repository for GloProg (GloVersity) Class 07, held on -- / -- / ----.

---

## 🚀 Why Use Google Colab?

**Google Colab** is a cloud-based platform that makes coding easier and faster. Here are some of the **amazing benefits** of using Colab:

1. **No Local Errors** 🔧: Since Google Colab runs in the cloud, you won’t face issues caused by your local hardware or system configuration. This eliminates the headache of troubleshooting local errors.
2. **Virtual Computing Environment** 💻: You don’t need a super-powerful computer to perform high-end computations! Google Colab provides a free virtual machine to run your code.
3. **16 GB VRAM** 🖥️: Colab provides access to powerful hardware, including GPUs with up to **16 GB of VRAM** for demanding tasks like machine learning or deep learning. Perfect for AI enthusiasts! 🤖
4. **1 GB/s Network Speed** ⚡: Fast internet speeds allow you to download large datasets or interact with APIs without delay.
5. **Python Pre-installed** 🐍: Python comes pre-installed, so there’s no need to install any packages or set up your environment manually. You’re ready to code as soon as you open Colab.
6. **Colab Pro and Colab Pro+** 💼: 
   - **Colab Pro** ($9.99/month): Gives access to better hardware, faster GPUs, and longer runtimes.
   - **Colab Pro+** ($49.99/month): Provides even **faster GPUs** and more memory for those working with large datasets and more complex machine learning models.

---

## 🛠️ Key Features of the Google Colab Interface

We took a tour of **Google Colab’s interface** to understand its layout and the features available. Here's a detailed look at what we discussed:

1. **Play Button** ▶️: This button is used to execute the code within a specific cell.
2. **+Code Button** ➕: Adds a new code cell to your notebook where you can write your Python code.
3. **Generate with AI** 🤖: A cutting-edge feature that helps generate code snippets using **AI assistance**. Super useful when you're stuck or need help creating complex code!
4. **Creating a New Notebook** 📝: You can create a new notebook in two ways:
   - Navigate to **File > New Notebook** within Colab.
   - Or, in Google Drive, click **New > More > Google Colaboratory** to create a new notebook directly.

---

## 🖥️ Google Colab’s Interface Components

Once you've created a notebook, the interface is organized into several essential sections:

1. **Menu Bar**: This section contains options for saving, editing, running, and managing your notebook.
2. **Toolbar**: Allows you to add or delete cells, run your entire notebook, or stop code execution if something goes wrong. ⛔
3. **Notebook Cells**: These are where you write and execute your Python code or add text. You can also use **Markdown** to format your text with headers, links, and more.

---

## ⚡ Accelerate Your Tasks with GPU/TPU

We also explored how to accelerate your deep learning tasks by enabling **GPUs** (Graphics Processing Units) or **TPUs** (Tensor Processing Units). This is crucial for machine learning models that require a lot of computational power.

### Steps to Enable GPU/TPU:

1. Go to **Runtime > Change runtime type**.
2. In the **Hardware accelerator** dropdown, select **GPU** or **TPU**.
3. Click **Save**.
4. Check if your environment has access to a GPU by running this Python code:
   ```python
   import tensorflow as tf
   print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
💻 Writing Your First Python Program - “Hello Wizard”
We wrote a simple Python program during class:
```
python
print("hello wizard")
This program prints “hello wizard” to the output.
```

🎉 We also encountered some common errors and learned how to troubleshoot them:

Syntax Error 🛑: This occurs when there is a mistake in the structure or formatting of your code. Always check for missing punctuation or improper indentation.
Name Error ⚠️: Happens when you try to use a variable or function that hasn’t been defined yet. Make sure all your variables and functions are properly named and initialized before you use them.


📦 Installing External Libraries with pip
---
Want to use external libraries? No problem! Google Colab supports package installations using pip. We learned how to install external libraries:
```
python
!pip install package_name
```
For example, to install the NumPy package, you would run:
```
python
!pip install numpy
```
💾 Accessing Files and Google Drive
---
Colab allows you to upload files directly or mount your Google Drive to access files:

To Mount Google Drive:
```
python
Copy code
from google.colab import drive
drive.mount('/content/drive')
```

After authentication, you’ll have access to your Google Drive files. This is a great feature for working with larger datasets stored in the cloud!

🔗 Using External Data Sources in Google Colab
---
Google Colab is excellent for accessing data from external sources, such as GitHub repositories or Google Sheets. Here’s how we can interact with them:
###
Cloning a GitHub Repository:
###

```python
!git clone https://github.com/username/repository.git
```

Reading Data from Google Sheets:

```python
import pandas as pd
url = 'your_google_sheet_url'
sheet = pd.read_csv(url)
```
---
👥 Sharing and Collaboration
---
Google Colab makes collaboration super easy! Here’s how you can share your notebook with others:
Click the Share button in the top-right corner of your notebook.
Set permissions for your collaborators—either view-only or edit access.
Share the generated link with your team members, and you’re ready to collaborate in real time! 👫


---
📧 Sending Emails from Google Colab
---
Yes, you can even send emails from Google Colab! We demonstrated how to use the smtplib library to send an email. Here's the code to send an email:
```
python
import smtplib

# Email details
sender = 'your_email@gmail.com'
receiver = 'receiver_email@gmail.com'
password = 'your_password'
message = """Subject: Test Email from Google Colab

This is a test email sent from Google Colab.
"""

# Setup server connection
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Login and send the email
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()

print('Email sent successfully!')
```
---