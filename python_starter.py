"""
This file is a Python script, going through the most important bascis for using Python in the world of oceanographic research.
It is meant to help students and scientists unfamiliar with Python as a Progamming Language. Rather than a complete and official introduction, it is kept rather informal and leaves out lots of details. It is just intended to get the target group started.
author: Eike Köhn
date: 22.12.2018

The file is structured in different chapters, each covering different topics.
This is the table of contents:

0. Setting up your Python work environment
1. Mathematical basics
2. Lists and Dictionaries
3. Arrays and Numpy
4. Plotting things
5. Statements, Conditions and Loops 
6. Reading in and saving datafiles
7. Handling NetCDF Files
8. Other helpful packages
9. Jupyter Notebooks

To go through it, just execute the lines, line by line, and see what happens. Enjoy, have fun!

"""

############################################
###### CHAPTER 0 - Getting started #########
############################################

# You sit down in front of the computer and say to yourself: I want to learn Python. You've heard so much about it, now you finally want to explore and learn it yourself. But where to start?
# Before starting, it is important to understand that Python is an open source programming language that is developed by many people around the world. It is constantly being updated and improved. Usually, newer versions should be able to correctly interpret code that is written in older versions, but unfortunately this is not always the case. Today, Python 3 (Python 3.5 or 3.6) are the most up to date versions, but many phyton programms were written in Python 2 (e.g. Python 2.7). Most things between these versions are compatible with one another, but there is one important exception with the "print" command. But I will get to this later. For now, we will work with Python 3, but in case you run into problem when running other code, be aware that this version difference could be the source of problems. 
# It is then important to know that Python in itself is just a Programming language that is able to interpret the words and signs that you write. So you could just write a Python program just in your computer's text-editor (any editor is fine) abd save it with the file suffix ".py". Then, if you actually want to run the program, you need your Python interpreter that tries to make sense of what you write and actually execute the functions etc. that are featured in your program. There are many different Programs, that combine the editor and the interpreter into one interface. Examples for these are Spyder or Pyzo. The nice thing about them is, that you can write your code in the interfaces editor and directly execute the code in there.
# As many people work on different topics using Python as a programming language, there already exists a huge amount of functions etc. that do specific things. For example, if you want to plot your data, you could really start from scratch and tell you computer to create an interface that is able to show images, configure the interface in the correct way etc. This would be a quite tedious thing to do and would keep you from doing science. Instead one can just use so-called "modules" or "packages". They have all the necessary things inside and you can just use them as a working bundle. Regarding the plotting example, the most commonly used package is the "matplotlib" package. But more to this later in Chapter 4. 
# Because certain modules require within themselves other modules, things can get confusing quite quickly. And there are a lot of modules! But don't woryy, there is a nice solution for this, called a package or module manager. One example of this is "conda". If you need a new module (or update the module version), it will make sure that all dependencies are also installed and present in their right version. Via conda you can also install the python interpreter itself. If you decide to use "conda", then you have the chance between "Anaconda" and "Miniconda". When you install Anaconda, many packages will be installed right away, making Anaconda quite consuming regarding storage (around 2 or 3 GB, I think). Many of those modules, you will never need. In constrast, Miniconda is rather small. Only the most basic modules are included and one needs to individually install modules when necessary. I prefer Miniconda, as you have a good overview of what you have installed and what not. Also, I like to save space on the disks.
# Okay, so now we know what we need: 1) an interface to write and execute code (e.g. Spyder) and 2) a module manager (conda) to install/update modules and packages as well as the python interpreter (Python 3.5).

# This is the intallation procedure:


# In case you encounter problems or have questions, there is lots of help on the internet or even within python!




################################################
###### CHAPTER 1 - Mathematical basics #########
################################################


## 1.0 Variables - Integers, floats and strings

# With python you can define variables. Here is an example:
x = 2     # Does the calculation and saves it to the variable x

# To look at the variable you can say
x
# or
print(x)
# Both ways, the value of the variable x will be displayed in the shell.
# In Python 2, the syntax of the print command would require: "print x"

# To get the result in a nicer format, you can write
print('x =',x) 

# You can also write:
b = 'x ='
print(b,x)

# So it is possible to save numbers, but also text as a variable.
print(type(x))   #returns "<class 'int'>"
print(type(b))   #returns "<class 'str'>"
# In these cases we refer to x as an "Integer" (a whole number) and to b as a "String", a text object.

# If we now say
y = 2.
print(type(y))
# then we see that adding the point behind the 2, tells python, that y is a "float", rather than an integer, i.e. a decimal number.

# For now, these are the most important data types


## 1.1 Simple Math - Operators

alpha = x+2 # addition
beta = x-2 # subtraction
gamma = x*2 # multiplication
delta = x/2 # division
epsilon = x%2 # modulus (yields the rest, when deviding x by 2)
print(x,alpha,beta,gamma,delta,epsilon)

# It becomes clear, that despite the fact that only integers are involved, the division automatically yields floats. 
# BE AWARE: This is not the case in Python 2. There, a divison like 1/2 would yield the result 0, i.e. rounding to the lower integer.

# Using the // operator features this behaviour in Python 3.
zeta = 3//2
print(zeta)

# Hence, it is important to always think about what datatype you actually want, so to avoid any confusion, mistakes when transferring progams from Python 2 to 3 and vice versa.



#################################################
###### CHAPTER 2 - Lists and Dictionaries  ######
#################################################

## 2.0 - Lists

# Often it is nice to have multiple datapoints stored together in one variable. E.g. if you have multiple measurements, you might want to store them in one list. Here is an example:

list0 = [0,1,2,3,4,5]
print(list0)
print(type(list0))

# As you can see, a list is an official datatype (or "class"). 
# You can put everything in there, floats, strings, integers, or even lists themselves:
list1 = [10, 'hey', 2.7, list0]
print(list1)

# How do we handle these?
# You can access the data in the list by indexing with square brackets. Say, you want to have the first entry of list1:
print(list1[0])
# The index number must be an integer (so you cannot call list1[0.]) and in the world of Python counting starts with 0 (in contrast to other programming languages like Matlab, where you would start counting at 1, which in more intuitive).
#If you want to call the last entry of a list, then you can use -1, hence:
print(list1[-1])
# In this case, this will yield the entire list0, which is the last element of list1. One could now use doubled indexing to access the last element of list 0
print(list1[-1][-1])
# It is also possible to access multiple values at the same time
print(list1[0:2])
# or in a shorter version
print(list1[:2])
# This will return the first two values of the list as a list. Note, that as you also specified 2 one would expect the indices 0,1 and 2 to be extracted. However it only goes to index 2 minus 1. 

# Calling all values works as:
print(list1[:])

# You can also index from the end of the list:
print(list1[-2])
# giving you the second to last value.
print(list1[-2:-1]) #will lead to the same result, but as a list. Again the endindex of the extracted values is -1 minus 1, i.e. -2, so that you extract only the index -2.

# If you want to extract the last two values you should write
print(list1[-2:])

# Now you know how indexing of a list works.
# But how do you manipulate an existing list?
list1.append(10) # for example appends the integer 10 to the existing list 10
# There are many different operators on the list class. Here are just a few important ones:
#list1.clear
#list1.copy
#list1.count 
#list1.extend 
#list1.index
#list1.insert 
#list1.pop 
#list1.remove 
#list1.reverse 
#list1.sort

# While most of them are intuitive, the "copy" method is worth explaining.
list2 = list1
print(list2)
list3 = list1.copy()
print(list3)
list1[0] = 0
print(list2)
print(list3)
# When you execute the above 7 lines, then you realize, that list2 and list3 behave differently to changes in list1. After changing the first entry in list1, the same change happens in list2, while list3 remains in its old state. Why is that? list2 is created as a socalled "deep copy" of list1. Every change in list1 is also featured in list2. In contrast, list3 is a "shallow copy", created by the copy method. Changes in list1 will not affect list3. 
# This distinction is important and could lead to unforseen errors, if one is not aware of this peculiarity.

# Here are some more examples to create lists
list4 = [] # creates an empty list
list5 = [0]*5 # creates a list with 5 elements of integer 0
list6 = [0,1]*5 # similar to list5, but with alternating 0s and 1s


## 2.1 - Dictionaries
# While lists are an assembly of any sort of entries, the values inside can be indexed. The list is thereby sorted in a certain way.
# A so-called dictionary gives you the possibility to store data in an unsorted way.
# Here is how to create a dictionary:
dict0 = {} # this one is empty
dict1 = {'var0': 5} # this dictionary has one so-called "key", namely var0. The value associated with this key is the integer 5. To call the data in dict1 it is not possible to just call dict1[0], because the var0 key is not necessarily the 0th entry in the dictionary. If you add others, var0 might move to different positions. Hence, to prevent disambiguity, one has to call the data by giving the key, i.e.
print(dict1['var0']) 
# With
dict1.update({'var1':[0,1,2,3]}) # you update the dict1 with another key/value pair. In this case the value is a list. 
# With
dict1.pop('var0') # you remove a key/value pair, in this case var0

# So what is the advantage? Sometimes it is just handy to have a nice overview over the data that you store away in a variable. By using the .keys() method, you can get all the keys stored in the dictionary.
print(dict1.keys())
# In this case it is quite senseless, but imagine having some oceanographic measurements, in which you want to specify where and when and by who the data was measured. Then you could define multiple keys, such as "longitude","latitude","time","researcher","data", etc. This helps you organize your data.



######################################################
###### CHAPTER 3 - Numpy - Arrays and Matrices  ######
######################################################

## 3.0 - Numpy
# As you might have realized, lists are already powerful objects. However, they are somehow hard to do math with. In their notation they look like vectors, but you might have already realized some issues. For example, the statement 
list7 = [1]*2
#leads to a list with two entries of the integer 1, rather than a list with one integer 2.
# Similarly, using "list7+2" will lead to an error. You might be intrigued to try list7+[2], but this will only append the value 2 to the list, similar to the append() method.

# So, doing math with lists is somewhat complicated, dictionaries are also not very convenient. If you are familiar with MATLAB, then this might strike you as something strange. MATLAB is built upon and highly optimized for vector and matrix operations. But Python wouldn't be python wouldn't be Python, if there wasn't a package to deal with this. It is called numpy. 
# To load it, just type
import numpy as np
# Whenever you now want to use a function from the numpy module, you have to add the prefix "np." to the functions. This way it is however clear, that the functions are rooted in the numpy package. There are other packages that contain maybe the same function name but you would want to avoid any disambiguities. For example, both the "math" and the "numpy" package contain the "sin" function. For now we will go over the "math" package and only focus on the "numpy" package, as it features everything we need, including the possibilities to do some vector and matrix calculations. In the python world, these are summarized under the name "array". An array can have any dimension, thus it could either represent a vector or a matrix or a tensor of higher dimensions.

## 3.1 - Numpy Arrays and matrices

# So, to set up an array, you could just write:
array0 = np.array([0,1]) # this is an array, similar to a vector
print(type(array0))  # is of class 'numpy.ndarray'
print(np.shape(array0)) # with dimension (2,)
# Now, if you do:
array1 = array0*2 # this will multiply each value in the array by 2
array2 = array0+2 # this will add 2 to each value in the array

# A higher dimensional array (e.g. 2D) is defined by writing:
array3 = np.array([[0,1],[2,3]])
print(np.shape(array3)) # with dimension (2x2)

# So, how do they behave if you want to do math with them?
# Multiplication, addition, subtraction, division, powerlaws and all other standard arithmetic functions work elementwise
print(array3*3)
print(array3+3)
print(np.sin(array3))

# If you have two arrays of the same dimension (m,n), then the multplication is elementwise between them. 
print(array3*array3)
print(array2*array2)
# Usually, the arrays have to be of same dimensions and size.
# A special case is the multiplication with a vector e.g. of dimension (m,) and the associated square matrix of dimension (m,m).
print(array3*array2)
# is equal to 
print(array2*array3)
# There the (m,m) array columns are multiplied with the respective value of the (m,) array.


# The Skalarproduct is called with the np.dot function
print(np.dot(array2,array2))
# in the case of higher dimensional arrays, this corresponds to a matrix-matrix multiplication.
print(np.dot(array3,array3))
# Remember, that the order of input matters.

# The Crossproduct is defined with
print(np.cross(array5,array5))


# The numpy.ndarray class features a matrix subclass, defined the np.matrix function. In this subclass, all arrays are set to be 2 dimensional. Hence, there is no such thing as a (m,) array, but rather a matrix with the two dimensions (m,1).
mat0 = np.mat([0,1,2])
print(mat0)
print(np.shape(mat0))  # of dimension (1,3) instead of (3,)
print(type(mat0))   # of class numpy.matrixlib.defmatrix.matrix

# If you transpose the mat0 matrix, then you get a matrix with dimension (3,1)
mat1 = mat0.T
print(mat1)
print(np.shape(mat1))

# This transposition function also works with ndarrays, but not in the (m,) dimension case. There, the dimension will remain (m,) after transposition.
print(np.shape(array2))
print(np.shape(array2.T))

# Another advantage of the matrix subclass is the simple notation. There, the matrix (array) multplication doesn't need the tedious np.dot(x,y) notation. Instead the "*" sign implies proper matrix multiplication in the case of matrix subclasses.
print(mat0*mat1)
print(mat1*mat0)


##########################################
###### CHAPTER 4 - Plotting things  ######
##########################################

## 4.0 - Matplotlib basics
# Okay, so now you know how to store data in variables, such as lists or arrays. Now you want to maybe have a look at it by visualizing it.
# The most popular package to plot things in python is "matplotlib". The package contains many things, but the most important part is the pyplot module. You need to load it to get going. This works like
import matplotlib.pyplot as plt
# In the following, you will have to call all functions of the matplotlib.pyplot module, by starting with "plt."

# Imagine you have two lists with integers that you want to plot:
listx = [0,1,2,3,4,5,6]
listy = [2,1,2,1,2,1,3]

# Then you can plot them with the following three lines:
plt.subplots() # initiates the plotting window
plt.plot(listx,listy) # plots the data as a lineplot into the window
plt.show()  # command to actually show the plot in a window


## 4.1 - Making plots nice
# In science, nice graphs of the results are an important asset. So you want to make your plots look all nice. Here are some basics, to get the figure to contain all necessary labels, titles etc.

# take again the same figure as before
plt.rcParams['font.size'] = 13 # 
fig, ax = plt.subplots() # initiates the plotting window, this time defining the name of the figure (fig) and the axis (ax)
ax.plot(listx,listy,'.--',markersize=20,markerfacecolor='C1',markeredgecolor='k',color='C0') # plot the data, again as a lineplot, but with markers (set by the dot in the '.--' string. The line itself is given as a dashed line (the '--' in the '.--' string). The color of the line is set to be 'C0' (blue), which is a matplotlib (version3) predefined color (others are C1,C2,C3,...,C8). The color of the marker is split into an edgecolor (in this case black, given by the string 'k') and a facecolor ('C1' - orange).
ax.set_xlabel('X_label') # adds the label to the xaxis
ax.set_ylabel('Y_label') # adds the label to the yaxis
ax.set_title('Title') # adds the title
ax.grid() # adds the grid
ax.set_xlim([0,6]) # set the limits of the xaxis
ax.set_ylim([1,3]) # sets the limits of the yaxis
h0 = plt.axhline(2.25,color='k',label='Horiz. line') # adds a horizontal line at the y-value 2.5 with the color black ('k'). The line itself has a handle called h0. With this handle the line itself can be called and modified directly later on. Additionally, the line carries a label or name "Horiz. line". This serves as a title of the line, in case a legend is included in the figure, explaining what this line is.
plt.axvline(1.5,color='#ABCDEF',label='Vertical line') # same as above, but this time a vertical line. The color of the line is this time given in a HEX code, thus a string consisting of a '#' and afterwards 6 digits which can be anything from 0-9 and A-F.
ax.scatter(3,2,200,'c',zorder=3,marker='*',edgecolor='r',label='Scatter') # here, a data point is scattered into the plot at the x-location 3 and the y-location. The markers size is 200, its facecolor is cyan blue ('c') , the marker itself is a star ('*') and its edgecolor is red ('r')
plt.legend(loc=0) # here we include a legend which features both the horizontal and vertical line, as those are the ones featuring a label. The legend is positioned at loc=0, which means that matplotlib tries to find itself the ideal spot to put the legend, covering as little plot content as possible. One could also set the location to loc=1, loc=2, ... to set it to specific corners of the plot.
plt.tight_layout() # this one stretches the axis ax as far as possible to make ideal use of the space provided by the figure (fig).
plt.show() # finally shows the plot

# If you don't have one dimensional data, but two dimensional data, then visualization mostly requires a different representation. 
plot2D = np.random.rand(20,20) # creates a random field of floats between 0 and 1 with dimension (20,20)
fig1,ax1 = plt.subplots()
h1 = plt.contourf(plot2D,20)  # contourf interpolates between the data points to give a full spatial picture with 20 different color levels, each color representing a certain value interval
plt.colorbar(h1) # this initiates a colorbar corresponding to the h1 handle datafield
plt.show()

# In the above case the x and y axis are just the indices of the data points stored in the matrix. You could also write plt.contourf(xaxis,yaxis,plot2D,20) with the corresponding x and y axes, to feature them in the plot rather than the indices.

# This is just a handful of options that have been presented above and it would be unnecessary and super exhausting to list all posible options because there are just so many. The page of the matplotlib package has a very useful website, on which you can easily look up everything that is part of matplotlib. So here is the link, it'll also appear as a first result on Google if you type in matplotlib: "matplotlib.org" 


##


#here is a useful function to create a list:
list2 = range(5) # gives you a list with integers from 0 to 4
print(type(list2))