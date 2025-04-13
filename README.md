### Word Count (`wc`) Tool

This repository contains three implementations of the `wc` (word count) tool:

1. **Python CLI Version**: A command-line version written in Python.
2. **Python GUI Version**: A graphical user interface (GUI) version written in Python using `tkinter`.
3. **C CLI Version**: A command-line version written in C.

## Table of Contents

- [Python CLI Version](#python-cli-version)
- [Python GUI Version](#python-gui-version)
- [C CLI Version](#c-cli-version)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

---

## Python CLI Version

### Description
A command-line tool that counts lines, words, and characters in one or more files. It mimics the behavior of the Unix `wc` command.

### Features
- Counts lines, words, and characters.
- Handles multiple files.
- Reads from standard input if no files are provided.
- Provides clear error messages.

### Installation
No installation required. Just ensure you have Python 3 installed.

### Usage
```bash
python wc_cli.py [file1] [file2] ...
```

### Example
```bash
python wc_cli.py sample.txt
```

---

## Python GUI Version

### Description
A graphical user interface (GUI) version of the `wc` tool that allows users to select files and view counts in a user-friendly window.

### Features
- Select multiple files using a file dialog.
- Displays lines, words, and characters for each file.
- Shows total counts if multiple files are selected.
- Clear results button to start over.

### Installation
No installation required. Just ensure you have Python 3 and `tkinter` installed.

### Usage
```bash
python wc_gui.py
```

### Screenshot
![GUI Screenshot](gui_screenshot.png)

---

## C CLI Version

### Description
A command-line version of the `wc` tool written in C. It provides a fast and efficient way to count lines, words, and characters in files.

### Features
- Counts lines, words, and characters.
- Handles multiple files.
- Reads from standard input if no files are provided.
- Lightweight and fast.

### Installation
Compile the C program using `gcc`:
```bash
gcc wc_cli.c -o wc
```

### Usage
```bash
./wc [file1] [file2] ...
```

### Example
```bash
./wc sample.txt
```

---

## Usage Examples

### Python CLI
```bash
python wc_cli.py file1.txt file2.txt
```

### Python GUI
```bash
python wc_gui.py
```

### C CLI
```bash
gcc wc_cli.c -o wc
./wc file1.txt file2.txt
```

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

--- 

This `README.md` provides a clear and structured overview of all three versions of the `wc` tool, making it easy for users to understand and use each implementation.
