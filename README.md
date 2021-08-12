# FilePropertyViewer
[![License](https://img.shields.io/badge/license-GPLv3-blue?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0.html) ![Pull Requests](https://img.shields.io/github/issues-pr-closed/katorlys/FilePropertyViewer?style=for-the-badge) ![Issues](https://img.shields.io/github/issues-closed/katorlys/FilePropertyViewer?style=for-the-badge)

## Introduction
A program that shows all files' property in a specified directory (Subdirectory included).<br>

<img align="center" src="screenshot.png"><br>

## Usage
Change `%LOCAL_PATH%` into a directory in your computer.<br>
```python
if __name__ == "__main__":
    path = r"%LOCAL_PATH%"
    showFileProperty(path)
```