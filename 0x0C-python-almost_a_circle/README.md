
ALX Higher Level Programming - Almost a Circle
This repository contains Python files that implement a system for managing geometric shapes, including rectangles and squares. The project is part of ALX Higher Level Programming curriculum.

Table of Contents
Description
Project Structure
Files and Descriptions
Testing
How to Use


Description
The project focuses on building a robust system for managing geometric shapes using Python classes and object-oriented programming. The main classes include Base, Rectangle, and Square. The system provides functionalities such as creating shapes, calculating areas, displaying shapes, and converting shapes to JSON representations.

Project Structure
The project is organized into directories, and each directory contains specific files related to a particular aspect of the project.

models/: Contains the implementation of the Base, Rectangle, and Square classes.
tests/: Includes unit tests to ensure the functionality and correctness of the implemented classes.
Files and Descriptions
models/base.py: Contains the Base class with methods for managing IDs and converting instances to dictionaries.

models/rectangle.py: Implements the Rectangle class, which inherits from Base. It includes methods for calculating the area, displaying the rectangle, and updating attributes.

models/square.py: Implements the Square class, which inherits from Rectangle. It adds methods for managing the size attribute.

tests/: Directory containing unit tests for the implemented classes. Testing is done using the unittest module.

Testing
To ensure the correctness of the implemented classes, run the unit tests using the following command:

bash
Copy code
$ python3 -m unittest discover tests
Make sure that all tests pass without any errors.

How to Use
To use the implemented classes, you can create instances of Rectangle and Square and perform various operations such as calculating areas, displaying shapes, and updating attributes. Refer to the example scripts in the tests/ directory for usage examples.
