### Airbnb Clone -  The Console Project

![models](./img/Project.png)

## Brief Description

The console , is a command interpreter his  functionality is similar to shell , but with limited & unique Commands.

We Want to be able to manage the objects via :

=> Create a new objects (new User or New Place)

=> Get an object from the Storage(in the first Version we only use json file for storage)

=> Perfome operation on objects

=> Update attributes of an object

=> Destroy/Delete an object


## How to Use it 'console.py'

`console.py` is a command-line interpreter designed to interact with a hierarchical object-oriented data storage system. The commands provided in the interpreter allow you to perform operations on instances of various classes.

### Getting Started

1. Ensure you have Python3 installed on your system
2. Clone the Repository containing 'console.py'
3. Navigate to the project directory in your terminal 

### Running the Console

To start the console, execute the following command in your terminal:
```bash 
Python3 console.py
```
This will launch the interactive command-line interpreter.

### Available Commands
#### quit
Exit the Program:
```bash
(hbnb) quit
```
#### EOF
Exit the program after reacing the end-of-file:
```bash
(hbnb) EOF or Ctrl+D
```
#### create
Create a new instance of a class. Provide the class name as an argument:
```bash
(hbnb) create BaseModel
```
#### show
show the string representation of an instance based on the class name and ID:
```bash
(hbnb) show BaseModel 1234-5647-9874-4562 
```
#### destroy
Delete an instance based on the class name and ID:
```bash
(hbnb) destroy BaseModel 1234-5647-9874-4562
```
#### all
print all string representations of instances, based on the class name or print all instances:
```bash
(hbnb) all
(hbnb) all BaseModel
```
#### update
Update an instance based on the class name , ID, attribute name:
```bash
(hbnb) update BaseModel 1234-5647-9874-4562 name "New Name"
```
#### count
Print the count of all instance of a specific class:
```bash
(hbnb) count BaseModel
```
### Custom Commads:
for now the Console support only one custome Command BaseModel.all()
Print all string representations of instance of BaseModel:
```bash
(hbnb) BaseModel.all()
```

#### Notes

<li>
<ul>invalid inputs will be handled with appropriate error messages</ul>
<ul>Make sure to enclose the attribute value in the update command  with double quotes</ul>
</li>

## setup the models
![models](./img/all_models.jpg)

## Authors

Younes Bousfiha <younesanas2021@gmail.com>

Mohamed Assaoui <assaoui54@gmail.com>
