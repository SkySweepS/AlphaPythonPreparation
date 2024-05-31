#Import the whole module and call it function by function with Module.function() method
import myModule
myModule.function()

#From the module import only the specific function
#can use it like a function created in the same file
from myModule import function
function()

#Wildcard imports(BAD PRACTICE)
#imports everything from the Module file,
#even lower level interpretation

from myModule import *
function()

#IMPORT ALIAS
import myModule as m
m.function()

