# Polygon Drawing App

## Introduction
This project is a Python application that uses Tkinter to draw various geometric shapes based on user input. The application supports drawing simple polygons like squares and triangles, as well as irregular polygons. It is designed as a practical application to demonstrate object-oriented programming principles in Python, particularly focusing on the use of classes and inheritance.

## Features
- Draw different geometric shapes including squares, triangles, and irregular polygons.
- Interactive GUI using Tkinter.
- Object-oriented design.
- Console Based input style implementation

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Tkinter installed with Python (usually comes with the standard library)
- No additional packages are required to run the application as it uses Python's built-in libraries.

## Project Structure

```
PolygonV2-Tkinter-Integration/
│
├── main.py                         # Entry point of the application
├── app.py                          # Main application logic for Tkinter GUI     
├── PolyGon.py                      # Base class for polygons
├── Square_Class.py                 # Square class
├── Triangle_Class.py               # Triangle class
├── Irreg_Polygon.py                # Irregular polygon class
├── Reg_Polygon.py                  # Regular polygon class
├── Shape_Interface.py              # For Abstract Shape interface
├── Point_Class.py                  # Point class
│
├── Turtle/                         
│   ├── canvas.py                   # Canvas like a Drawing pad
│   ├── line.py                     # line class
│   └── pen.py                      # Pen That draws on canvas
│
└── README.md                       # Project documentation

```

## How It Works
The application uses a Tkinter canvas to draw shapes. Users can specify the vertices of the shapes they want to draw, and the application will render these on the screen. The shapes are defined using classes that inherit from a base `Polygon` class, demonstrating the use of inheritance and polymorphism.

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your features or fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.