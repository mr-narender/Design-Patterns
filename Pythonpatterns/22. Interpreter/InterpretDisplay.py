"""Interpreter pattern
parses a simple grammar and sorts the results accordingly.
The parser uses stack reduction to reduce the tokens
to verbs and variables"""

import tkinter as tk
from operator import attrgetter
from tkinter import *
import os
import sys

# Command interface
class Command():
    def comd(self):pass

#derived button class with an abstract comd method
class DButton(Button, Command):
    def __init__(self, master,  **kwargs):
        super().__init__(master, command=self.comd, **kwargs)

# Interpreter button runs the parser
# and loads te list box
class Interp(DButton):
    def __init__(self, root, bldr):
        super().__init__(root, text="Interp")
        self.bldr=bldr
    def comd(self):
        print (sys.path[0])
        self.swmrs = Swimmers(os.path.join(sys.path[0],"100free.txt"))
        commands = self.bldr.getEntry().get()
        p = Parser(commands, self.swmrs.getSwimmers(), self.bldr)

        #stack reduction takes place here
        while len(p.getStack()) > 0:
            p.reduceStack()
        # get the sorted list of swimmers
        # and load it into the listbox
        plist = self.bldr.getPlist()
        lb = self.bldr.getListbox() #get the listbox
        lb.delete(0, END)
        for pl in plist:
            lb.insert(END, pl)

# One swimmer consists of name, club and time
class Swimmer():
    def __init__(self, dataline):
        sarray = dataline.split()  # read in a row and separate the columns
        i = 1       #skip the numbered column
        self.frname =sarray[1] # names
        self.lname =sarray[2]
        self.age =int(sarray[3])  # age
        self.club =sarray[4]  # club symbol
        self.seedtime =sarray[5]  # seed time as string
        self.time =0.0  # set defaults

        # remove colon from times of 1 minute or greater
        # so they can be sorted numerically
        if self.seedtime.find(":") > 0:
            mins = self.seedtime.split(":")
            atime = mins[0] + mins[1]  # time with colon removed
            self.time =float(atime)  # converted to float for sorting
        else:
            self.time =float(self.seedtime)

#Array of swimmers that gets sorted
class Swimmers():
    def __init__(self, filename):
        self.swimmers = []
        with open(filename, "r") as f:
            # the Swimmer class parses each line of the data file
            for swstring in f:
                sw = Swimmer(swstring)
                self.swimmers.append(sw)
    def getSwimmers(self):
        return self.swimmers

#carries out the sort by variable
class Sorter():
    def __init__(self, swmrs):
        self.swmrs = swmrs

    def sortby(self, vname):
        # bubble sort on one field
        f = attrgetter(vname) #create function to access field
        for i in range(len(self.swmrs)):
            for j in range(i, len(self.swmrs)):
                if f(self.swmrs[i]) > f(self.swmrs[j]):
                    temp=self.swmrs[i]
                    self.swmrs[i] =self.swmrs[j]
                    self.swmrs[j] = temp

# Variable is any token that is not a verb
class Variable():
    def __init__(self,varname):
        self.varType = "variable"
        self.varname = varname
        self.varlist = []
        self.varlist.append(varname)

    def append(self,var:Variable):
        # appends all the variables from previous token
        vlist = var.getList()
        for v in vlist:
            self.varlist.append(v)
    #def getName(self):
    #    return self.varlist[0]
    def getList(self):
        return self.varlist

# Verbs act on the accumulated variable tokens
class Verb(Variable, Command):
    def __init__(self, varname, swmrs, bldr):
        super().__init__(varname)
        self.varType = "verb"
        self.varname = varname
        self.swmrs = swmrs
        self.bldr = bldr


# here the Verb is executed
    def comd(self):
        # Sort by one field
        if self.varname.lower() == "sortby":
            sorter = Sorter(self.swmrs)
            self.varlist.pop(0)   #remove "sortby"
            for v in self.varlist: # multiple sorts here
                sorter.sortby(v)

        # generate a List of lines to disolay
        if self.varname.lower() == "print":
            self.varlist.pop(0)  # remove "print"
            pres = Printres( self.varlist, self.bldr)
            plist = pres.create(self.swmrs)

# creates the results strings to be loaded into the list box
class Printres:
    def __init__(self, varlist, bldr):
        self.printList = []
        self.functions = []
        self.bldr = bldr
        #create list of functions to fetch from Swimmer
        self.functions.extend(attrgetter(v) for v in varlist)
    def create(self, swmrs):
        for sw in swmrs:
            sline = "".join(f"{str(f(sw))}   " for f in self.functions)
            self.printList.append(sline)   # save in List
        self.bldr.setPlist(self.printList)

# Parser takes tokens and assigns them
# to Variable and Verb objects
class Parser():
    verbs= {"print", "sortby"}
    variables = {"lname", "frname", "club", "time", "age"}

    def __init__(self, commands, swmrs, bldr):
        tokens = commands.split()
        self.stack = []     #initialize stack
        self.swmrs = swmrs  # save swimmer array
        self.bldr = bldr    # and UI
        # go thru tokens and make them into
        # variables or verbs
        for tok in tokens:
            if tok.lower() in Parser.verbs:     # it's a Verb
                self.stack.append(Verb(tok, self.swmrs, bldr))
            if tok.lower() in Parser.variables: #or a Variable
                self.stack.append(Variable(tok))

    # stack reduction takes variables and collapses them
    # into a verb and its arguments
    def reduceStack(self):
        var = self.stack.pop()

        if var.varType == "variable":
           nextVar = self.stack.pop()   #get top of stack
           nextVar.append(var)      # append variables
           self.stack.append(nextVar)   #and put it back
           # act on variables if this is a verb
           if nextVar.varType == "verb":
                nextVar.comd()

    def getStack(self):
         return self.stack

# builds the UI and gives access to Entry and Listbox
class Builder():
    def __init__(self):
        self.plist = []
    def setPlist(self, pl):
        self.plist = pl
    def getPlist(self):
        return self.plist
    def build(self):
        commands = "Print lname frname club time Sortby time Thenby club"
        root = tk.Tk()
        root.geometry("300x250")
        root.title("Interpreter")

        self.entry =Entry(width=250)
        self.entry.pack()
        self.entry.insert(END, commands)

        self.results = Listbox(width=100)
        self.results.pack(padx=40)

        self.interp = Interp(root, self)
        self.interp.pack(pady=10)

        mainloop()
    #returns access to the Results list box
    def getListbox(self):
        return self.results
    #returns access to the entry field
    def getEntry(self):
        return self.entry

#----------------------------
def main():
    Builder().build()

###  Here we go  ####
if __name__ == "__main__":
    main()