# gitKeeper
A small python script for convenience and learning purposes.
Creates *.gitkeep* files or deletes them (for reversibility).
Can be useful when starting a new project and you create your project directory structure with lots of empty folders but you don't want to create the *.gitkeep* files manually for them.

## Usage
The script has two modes, add and delete. <br>
Navigate to your project root directory and use the mode which suits you.

- **add**

Adds a *.gitkeep* file to every empty subdirectory under the current directory.
```
py gitkeeper.py add
```
- **delete**

Removes *.gitkeep* files from every subdirectory under the current directory.
```
py gitkeeper.py del
```
