# WE CAN ADD MORE ORGANISATIONS TO OUR CODE CALLED MODULES ........

#####[ math. ]
#####[ pygal. ]
#####[ statistic. ]
#####[ requests ] 
#####[ Tkinter ] --GUI
#####[ SQLAlchemy ] --DATA BASE
#####[ Numpy ] --quad. equation / linear algebra
#####[ Matplotlib ] --graphs
#####[ Pywin32 ]
#####[ NLTK ] --natural language processing
#####[ Scikit Learn ] --machine learning
#####[ openCV ] --image processing
#####[ Flask ] --website

#####################################[ //1// - NATURAL LANGUAGE PROCESSING (2) ]###################################################

#------------------#1 NLTK          :   Manipulate strings
#------------------#2 Flask Text    :   Replace keywords in sentences or extract keywords from sentences
#________________________________________________________________________________________________________________________
############################################[ //2// - Computer Vision (2) ]##################################################################

#------------------#1 OpenCV        : Computer vision and image processing 
#------------------#2 Simple CV     : Computer vision
#___________________________________________________________________________________________________________________---
###################################################[ //3// - GUI (3) ]###########################################################################

#------------------#1 Tkinter       :  GUI
#------------------#2 wxPython      :  GUI Toolkit
#------------------#3 PyQt          :  GUI Toolkit
#________________________________________________________________________________________________________________________
################################################[ //4// - GAME (2) ]#######################################################

#------------------#1 Pygame        :  Writing video game mainly
#------------------#2 Pyglet        :  3D-Animation andgame craetion engine
#_____________________________________________________________________________________________________________________
##################################################[ //5// - WEB (6) ]#####################################################################

#------------------#1 Requests       :  HTTP library / Web 
#------------------#2 Scarpy         :  Webscraping
#------------------#3 BeautifulSoup  :  Parsing / Webscarping
#------------------#4 Zappa          :  Serverless application on API gateway and Amazon Web services
#------------------#5 Django         :  Web framework
#------------------#6 Flask          :  Web freamework
#________________________________________________________________________________________________________________________________
##########################################[ //6// - DATA SCIENCE (5) ]############################################################################

#------------------#1 Pandas       :     Data-science
#------------------#2 Matplotlib   :     2-Dimentional graph and plots
#------------------#3 PLotly       :     Similar to Matplotlib
#------------------#4 Bokeh        :     Data visualization library
#------------------#5 SQLAchemy    :     Database Abstraction
#________________________________________________________________________________________________________________________
###########################################[ //7// - MATH (3) ]#######################################################################

#------------------#1 Numpy     :     Advanced math functionality
#------------------#2 SciPy     :     Algorithms and mathemathical tools
#------------------#3 SymPy     :     Algebra , differentiation , expension , complex numbers
#______________________________________________________________________________________________________________________
######################################[ //8// - MACHINE LEARNING (8) ]######################################################################33

#------------------#1 Keras             :   Deep neural network 
#------------------#2 Tensorflow        :   Develop , teach and design deep learning models
#------------------#3 Pytorch           :   ML
#------------------#4 Scikit-learn      :   ML 
#------------------#5 imbalanced-learn  :   ML
#------------------#6 Theano            :   Deep learning library
#------------------#7 LightGBM          :   ML
#------------------#8 Eli5              :   ML
#________________________________________________________________________________________________________________________
###########################################[ //9// - OTHER (9) ]###################################################################
 
#------------------#1 Twisted  :            Network application develop
#------------------#2 iPython  :            Completion , history , shell capabilities and a lot more 
#------------------#3 Pillow   :            Images / pyhton imaging library
#------------------#4 Poetry   :            Manage python packaging and dependencies 
#------------------#5 Gensim   :            Natural library processing library
#------------------#6 Pywin32  :            Intererct with windows 
#------------------#7 Kivy     :            Mobile apps
#------------------#8 Pendulum :            Date and time 
#------------------#9 loguru   :            Python logging













#=====================================[  MATH  ]==============================================================

import math

#.....................................[  pi -- PI ]
print ("value of pi")
print(math.pi)          #3.141592653589793

#...............................[  .sqrt -- SQUARE ROOT  ]
print(" square root ")
print(math.sqrt(16))

#....................................[   help -- HELP -- can use for any module  ]

help(math)

#..............................[  .ceil -- nearest incompleted value -- ROUND OFF  ]
import math
rounded = math.ceil(22.2)
print(rounded)   # 23

#..............................[  .floor = nearest completed value  -- ROUND OFF  ]
rounded = math.floor(22.7)
print(rounded)   # 22

#====================================[   PYGAL  ]=======================================================

#------------------------------------[  1  ]

import pygal


pie = pygal.Pie()
pie._title = "time spend on social media"
pie.add("twitter", 50)
pie.add("insta",150)
pie.add("facebook",40)

pie.render_in_browser()

#-----------------------------------[  2  ]

import pygal

chart = pygal.Pie()
chart.title = "favourite type of movies "
chart.add("sci-fi",12)
chart.add("Romance",50)
chart.add("action",70)

chart.render_in_browser()

#=============================================[   STATISTICS   ]==============================================================

import statistics

scores = [4,8,6,3,4,8,9,7,1,5,4,6]
mean = statistics.mean(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)

print(mean , median , mode)

# when we import a part of module such as //from math import pi//...we can use it without type //math.//
# we can modify the names of module by using //as//.....



