# Installing Python & IDE Setup

## 1. Introduction

The objective of this assignment is to set up a Python development environment by installing Python, configuring Visual Studio Code (VS Code), selecting the Python interpreter, and executing a simple Python program.

## 2. Python Installation

Python is a high-level, general-purpose programming language.

### Installation Steps

1. Visit the official Python website: https://www.python.org/downloads/
2. Download the latest stable Python 3 version.
3. Run the installer.
4. Enable the option to add Python to PATH, if available.
5. Complete the installation.

### Verify Python Installation

Open Command Prompt or VS Code terminal and execute:

```bash
python --version
```

**Expected Output:**

```text
Python 3.x.x
```

The version displayed should match the Python version installed on the system.

**Screenshot:**

![Python Version Verification](screenshots/01-python-version.png)

## 3. Visual Studio Code Installation

Visual Studio Code is a lightweight source-code editor used for writing, debugging, and executing programs.

### Installation Steps

1. Visit https://code.visualstudio.com/
2. Download Visual Studio Code for Windows.
3. Run the installer.
4. Complete the installation.
5. Open Visual Studio Code.

### Install Python Extension

1. Open VS Code.
2. Press `Ctrl + Shift + X`.
3. Search for Python.
4. Install the official Python extension published by Microsoft.

**IDE Configuration:**
- IDE: Visual Studio Code
- Extension: Python
- Publisher: Microsoft

**Screenshot:**

![VS Code Installation](screenshots/02-vscode-installation.png)

## 4. Configure Python Interpreter

The Python interpreter executes Python programs.

### Configuration Steps

1. Open Visual Studio Code.
2. Press `Ctrl + Shift + P`.
3. Search for `Python: Select Interpreter`.
4. Select the installed Python 3 interpreter.
5. Verify that the correct interpreter is selected.

**Screenshot:**

![Python Interpreter Configuration](screenshots/03-python-interpreter.png)

## 5. Create and Execute a Python Program

Create a new file named `hello.py`.

### Python Code

```python
print("Hello, Python!")
print("Python environment setup completed successfully!")
print("Welcome to Python Programming!")
```

### Execute Using Terminal

Open the VS Code terminal and execute:

```bash
python hello.py
```

### Expected Output

```text
Hello, Python!
Python environment setup completed successfully!
Welcome to Python Programming!
```

**Screenshot:**

![Python Program Execution](screenshots/04-python-execution.png)

## 6. Installation Verification

| Task | Expected Result |
|---|---|
| Python Installation | Successfully installed |
| Version Verification | Python version displayed |
| VS Code Installation | VS Code opened successfully |
| Python Extension | Installed successfully |
| Interpreter Configuration | Python 3 selected |
| Program Execution | Successful output displayed |

## 7. Conclusion

Successfully setting up a Python development environment is the first step towards learning Python programming.

In this assignment, Python was installed, its version was verified, Visual Studio Code was configured with the Python extension, and a sample Python program was executed using the terminal.

This environment provides the foundation for developing Python applications and learning advanced programming concepts.

## 8. References

1. Python Official Website: https://www.python.org/
2. Python Documentation: https://docs.python.org/3/
3. Visual Studio Code: https://code.visualstudio.com/
4. Python Extension for VS Code: https://marketplace.visualstudio.com/items?itemName=ms-python.python
