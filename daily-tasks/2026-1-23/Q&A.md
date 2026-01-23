# Python Concepts: Recursion, Context Managers, Files, CSV, and JSON

---

## 1. What is a recursive function, and how does it differ from an iterative solution?

- **Definition:**  
  A recursive function is a function that calls itself.

```python
def foo():
    # do something
    foo()  # recursive call
    # continue
```

- **Differences from iterative solutions:**

| Iterative Solution                            | Recursive Solution                                                                 |
|-----------------------------------------------|----------------------------------------------------------------------------------|
| Generally faster                              | Slower due to function call overhead                                              |
| Uses a single stack frame                      | Each recursive call adds a new stack frame                                        |
| Uses loop termination conditions              | Requires base cases to avoid stack overflow                                       |
| Used for performance- and memory-efficient problems | Preferred for problems with recursive structure (trees, backtracking) and code readability |

---

## 2. Why is it important to have a base case in a recursive function?

- Recursive functions call themselves, creating new stack frames each time.  
- Without a **base case**, recursion may never stop → **stack overflow**.

---

## 3. What is a context manager in Python?

- A **context manager** is an object that defines a runtime context for the `with` keyword.  
- It automatically **sets up** and **cleans up** resources.

---

## 4. What is the purpose of the `with` statement in Python?

- The `with` statement creates a context for a block of code.

```python
with context_manager as variable:
    # block of code
```

- **Execution steps:**
  1. `context_manager.__enter__()` → setup, optional return value assigned to `variable`
  2. Block executes
  3. `context_manager.__exit__()` → cleanup, runs even if an exception occurs

---

## 5. How does the `with` statement help in managing resources like files or network connections?

- Creates a context that **automatically releases resources** when the block exits.
- Example resources: files, network connections.

---

## 6. Role of `__enter__` and `__exit__` methods in a context manager

- **`__enter__` method:**  
  Sets up the environment and optionally returns a value.

- **`__exit__` method:**  
  Cleans up all resources when exiting the context.

---

## 7. Different file modes in Python

| Mode | Description                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| `r`  | Read only. File must exist. Pointer at start.                                                 |
| `w`  | Write. Overwrites if file exists, creates new if not.                                         |
| `a`  | Append. Moves pointer to end if file exists, creates new if not.                              |
| `rb` | Read binary. Like `r` but for binary files.                                                  |
| `wb` | Write binary. Like `w` but for binary files.                                                 |

---

## 8. Difference between `read()`, `readline()`, and `readlines()`

- **`read()`** → reads entire file as a single string.

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

- **`readline()`** → reads one line at a time (includes `\n`).

```python
with open("data.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1, line2)
```

- **`readlines()`** → reads all lines into a list of strings.

```python
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)
```

---

## 9. What is a CSV file, and why is it widely used?

- **CSV (Comma Separated Values):** Plain text file for tabular data.  
- **Structure:** Each line = a row, values separated by commas.

**Advantages:**
1. Simple and lightweight  
2. Human-readable  
3. Supported everywhere  
4. Compact

---

## 10. How Python’s `csv` module helps in reading and writing CSV files

- **Reading CSV:**

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

- **Writing CSV:**

```python
import csv

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

---

## 11. What is JSON, and how is it different from Python dictionaries?

- **JSON (JavaScript Object Notation):** Text-based format for structured data exchange.

| Feature    | Python Dict                                                      | JSON                                                          |
|----------- |-----------------------------------------------------------------|---------------------------------------------------------------|
| **Type**   | In-memory                                                      | Text/string representation                                    |
| **Keys**   | Strings, numbers, tuples, etc.                                  | Must be strings                                              |
| **Values** | Any Python object (int, list, dict, bool, None, custom objects) | Only basic types: string, number, boolean, null, array, object|
| **Syntax** | Single `' '` or double quotes `" "`                               | Must use double quotes `" "`                                  |
| **Usage**  | Inside Python programs                                           | Data exchange between programs or languages                  |

---

## 12. Why is JSON preferred for data exchange in web APIs?

- Language-agnostic  
- Lightweight and compact  
- Human-readable  
- Easy to parse

