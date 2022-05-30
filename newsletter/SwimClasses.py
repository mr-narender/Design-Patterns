class Seeding:
    def getSwimmers(self): pass


class Event():
    def __init__(self, filename, lanes):
        self.numLanes = lanes
        self.swimmers=[]        #array of swimmers
        with open(filename, "r") as f:
            # the Swimmer class parses each line of the data file
            for swstring in f:
                sw = Swimmer(swstring)
                self.swimmers.append(sw)
    #place holders to be filled in in actual classes
    def getSeeding(self): pass
    def isPrelim(self): pass
    def isFinal(self): pass
    def isTimedFinal(self): pass
#-----------------------
class PrelimEvent (Event):
 #creates a preliminary event which is circle seeded
    def __init__(self, filename, lanes):
        super().__init__(filename, lanes)

    def  getSeeding(self):
        return CircleSeeding(self.swimmers, self.numLanes)
#--------------------
class TimedFinalEvent (Event):
#creates an event that will be straight seeded
   def __init__(self, filename,  lanes):
        super().__init__(filename, lanes)

   def getSeeding(self):
        return StraightSeeding(self.swimmers, self.numLanes)

"""Straight seeding puts the top swimmers in the last heat
and the next fastest ones in the second heat and so forth"""
class StraightSeeding(Seeding):
    def __init__(self, sw, nlanes):
        self.swimmers = sw
        self.numLanes = nlanes
        self.count = len(sw)
        self.lanes = self.calcLaneOrder()
        self.seed()
# --------------------------------
    def seed(self):
    #loads the swmrs array and sorts it
        asw = self.sortUpwards()  # number in last heat
        self.lastHeat = self.count % self.numLanes
        self.lastHeat = max(self.lastHeat, 3)
        lastLanes =self.count - self.lastHeat
        self.numHeats = self.count / self.numLanes

        if (lastLanes > 0):
            self.numHeats += 1 # compute total number of heats
        heats = self.numHeats

        # place heat and lane in each swimmer's object
        j = 0
        for i in range(lastLanes):
            sw = asw[i] # get each swimmer
            sw.lane= int(self.lanes[j]) # copy in lane
            j += 1
            sw.heat = int(heats) # and heat
            if (j >= self.numLanes):
                heats -= 1 # next heat
                j=0
    # Add in last partial heat
        if (j < self.numLanes):
             heats -= 1
             j = 0
      #for (int i = lastLanes-1; i < count; i++):
        for i in range(lastLanes-1, self.count):
             sw = asw[i]
             sw.lane= int(self.lanes[j])
             j += 1
             sw.heat= int(heats)
    # copy from array back into list
        swimmers = [asw[i] for i in range(self.count)]

    # Sorts the swimmers by seed time
    def sortUpwards(self):
        swmrs = list(self.swimmers)

        for i in range(self.count):
            for j in range(i, self.count):
                if (swmrs[i].time > swmrs[j].time):
                    swtemp = swmrs[i]
                    swmrs[i] = swmrs[j]
                    swmrs[j] = swtemp
        return swmrs

    # This works for any number of lanes, odd or even
    # seeing always starts in the middle and works outward
    def calcLaneOrder(self):
        lanes =[]
        mid = self.numLanes / 2
        if self.odd(self.numLanes):
            mid = mid + 1 # start in middle lane

        incr = 1
        ln = mid

        for _ in range(self.numLanes):
            lanes.append(ln)
            ln = mid + incr
            incr = - incr
            if (incr > 0):
                incr = incr + 1
        return lanes
    #returns a List of sorted, seeded swimmers
    def getSwimmers(self):
        return self.swimmers

    #simple function to return true if the number is off
    def odd(self, num):
        return (num % 2) != 0

"""Circle seeding distributes the fastest swimmers into the top 3 heats"""
class CircleSeeding(StraightSeeding):
    def __init__(self, sw, nlanes):
        super().__init__(sw, nlanes)

    def seed(self):
        super().seed() # do straight seed as default
        if (self.numHeats >= 2):
            circle = 3 if (self.numHeats >= 3) else 2
        i = 0

        for j in range(self.numLanes):
            for k in range(circle):
                self.swimmers[i].lanes = int(self.lanes[j])
                self.swimmers[i].heat = int(self.numHeats - k)
                i += 1
#------------
class Swimmer():
     def __init__(self, dataline):
         sarray = dataline.split()  #read in a row and separate the columns
         self.frname=sarray[1]      #names
         self.lname=sarray[2]
         self.age=int(sarray[3])    #age
         self.club=sarray[4]        #club symbol
         self.seedtime=sarray[5]    #seed time as string
         self.time=0.0              #set defaults
         self.lane=0                #seeded heats and lanes go here
         self.heat=0
         #remove colon from times of 1 minute or greater
         #so they can be sorted numerically
         if self.seedtime.find(":") > 0:
             mins = self.seedtime.split(":")
             atime = mins[0] + mins[1]  # time with colon removed
             self.time=float(atime)     #converted to float for sorting
         else:
             self.time=float(self.seedtime)

    #mConcatenate first and last names
     def getName(self):
         return f"{self.frname} {self.lname}"

