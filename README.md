# Matrices operations for Robotics automation


## Running


To run the documentation for this project run the following commands, at the project folder:

```
#Install Spinxs
python -m pip install sphinx

#Install the "Read the Docs" theme
pip install sphinx-rtd-theme

make clean

make html
```

Or you can go directly on the build folder and execute the index.html.6I have uploaded the build files as well. they are so small.


## Contents

### Example 6

here you have some functions that:

* Defines a matrix with no rotation and no translation (Identity)
* Translation of a given distance on the X axis
* Second Translation of a given distance on the X axis
* Identity matrix multiplied by the first X translation multiplied by the second translation
* Rotation Matrix in X by a given angle
* Rotation Matrix in Z by a given angle

### What else?

You also have some matrix differentiation, pruduct rule, quocient rule and the jacobian representation of a matrix for robotic manipulation.

If yu want to see everything just go to the build folder and check the Sphinxs documentation.


