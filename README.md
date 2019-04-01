# Week-01
## Python Programming Basics and Essential Python Module

In week 01 we discussed about essential Python Programming and essential contributed modules, Numpy, Matplotlib and OpenCV that we are going to use throughout our course.

### Python Essentials

#### Python Identifiers

A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).

Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language. Thus, Manpower and manpower are two different identifiers in Python.


#### Python Lists

The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.

Creating a list is as simple as putting different comma-separated values between square brackets.

```python
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]
```

read more at [tutorialspoint](https://www.tutorialspoint.com/python/python_lists.htm)

#### Python Tuples

A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

Creating a tuple is as simple as putting different comma-separated values. Optionally you can put these comma-separated values between parentheses also.

```python
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
```

read more at [tutorialspoint](https://www.tutorialspoint.com/python/python_tuples.htm)

#### Python Dictionary

Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.

Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

```python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']
```

read more at [tutorialspoint](https://www.tutorialspoint.com/python/python_dictionary.htm)


#### Python Functions

A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own functions. These functions are called user-defined functions.

You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

-Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).

-Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.

-The first statement of a function can be an optional statement - the documentation string of the function or docstring.

-The code block within every function starts with a colon (:) and is indented.

-The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

```python
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]
```

read more at [tutorialspoint](https://www.tutorialspoint.com/python/python_functions.htm)

### Numpy, Matplotlib and OpenCV

#### Numpy

NumPy is a Python package. It stands for 'Numerical Python'. It is a library consisting of multidimensional array objects and a collection of routines for processing of array.

Numeric, the ancestor of NumPy, was developed by Jim Hugunin. Another package Numarray was also developed, having some additional functionalities. In 2005, Travis Oliphant created NumPy package by incorporating the features of Numarray into Numeric package. There are many contributors to this open source project.

```python
import numpy as np 
a = np.array([1,2,3]) 
b = np.array([[1, 2], [3, 4]])
```
read more at [tutorialspoint](https://www.tutorialspoint.com/numpy/numpy_ndarray_object.htm)

#### Matplotlib

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.

read more at [matplotlib documentation](https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py)

#### OpenCV

OpenCV was started at Intel in 1999 by Gary Bradsky, and the first release came out in 2000. Vadim Pisarevsky joined Gary Bradsky to manage Intel's Russian software OpenCV team. In 2005, OpenCV was used on Stanley, the vehicle that won the 2005 DARPA Grand Challenge. Later, its active development continued under the support of Willow Garage with Gary Bradsky and Vadim Pisarevsky leading the project. OpenCV now supports a multitude of algorithms related to Computer Vision and Machine Learning and is expanding day by day.

#### Images in Computers

A digital image is composed of M rows and N columns of pixels each storing a value. Pixel values are most often grey levels in the range 0-255(black-white) or R,G,B values. images can easily be represented as matrices. In case of RGB images, a single pixel in a 2D matrice will have 3 x 8bit numbers for R,G,B components. In Gray scaled image, a pixel will contain only a single 8bit number (0-255) which gives the gray scale value

![Image in 2D array](https://blogs.mathworks.com/images/steve/2011/dipum_fig_2_1_a.png)
[source](https://blogs.mathworks.com/images/steve/2011/dipum_fig_2_1_a.png)


##### Accessing and Modifying pixel values

```python
import cv2

img = cv2.imread('messi5.jpg')
img[100,100] = [255,255,255]
cv2.imshow('IMG',img)
```

##### Changing Colorspaces

here are more than 150 color-space conversion methods available in OpenCV. But we will look into only two which are most widely used ones, BGR \leftrightarrow Gray and BGR \leftrightarrow HSV.

For color conversion, we use the function ```python cv2.cvtColor(input_image, flag)``` where flag determines the type of conversion.

For BGR to Gray conversion we use the flags ```python cv2.COLOR_BGR2GRAY```  Similarly for BGR to HSV, we use the flag cv2.COLOR_BGR2HSV

read more at [OpenCV documentation](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
