<a href="../../../../index.html">Go back to index</a>

<a href="../../base.html">Go back to Python Portal</a>

<head>
  <link rel="stylesheet" href="../../../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>

# Virus, Drug Treatments and Computational Models

This problem will be an implementation of computational modeling for viral infection, such as how drug therapy and viral drug resistance affect viral load over time. 

# Results

These are plots of viral load over 300 time steps in various scenarios. The first image is for virus load without any drugs, while the latter two are for a scenario where all the viruses start off either being resistant or not resistant. 

![](virus_sim1.png)
![](virus_sim2.png)
![](virus_sim3.png)

```python
simulationWithoutDrug(1, 90, 0.8, 0.1, 1)   
simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)
simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 4)
```

# Code

```python
import random
import pylab
from ps3b_precompiled_37 import *
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
random.seed(0)

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        return self.maxBirthProb

    def getClearProb(self):
        return self.clearProb

    def doesClear(self):
        if random.random() <= self.getClearProb():
            return True
        else: 
            return False

    def reproduce(self, popDensity):
        
        if random.random() <= self.getMaxBirthProb() * (1 - popDensity):
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            raise NoChildException
            


class Patient(object):

    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        return self.viruses

    def getMaxPop(self):
        return self.maxPop

    def getTotalPop(self):
        return len(self.viruses)

    def update(self):
        # virus.doesClear() returns true if it IS cleared - therefore only keep if it isn't!
        survived = [virus for virus in self.viruses if not virus.doesClear()]
        self.viruses = []
        for virus in survived:
            try:
                self.viruses.append(virus)
                self.viruses.append(virus.reproduce(self.getTotalPop()/self.getMaxPop()))
            except NoChildException:
                pass
        return self.getTotalPop()

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    mydata = np.empty([300, numTrials + 1])
    mydata[:, :] = None
    viruslist = [SimpleVirus(maxBirthProb = maxBirthProb, clearProb = clearProb) for _ in range(numViruses)]
    for col in range(numTrials):
        patient = Patient(viruslist, maxPop)
        for row in range(300):
            mydata[row, col] = patient.update()

    mydata[:, numTrials] = np.mean(mydata[:, 0:numTrials], axis = 1)
    pylab.plot(mydata[:,numTrials].tolist(), label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        return self.resistances

    def getMutProb(self):
        return self.mutProb

    def isResistantTo(self, drug):
        if drug in self.getResistances().keys():
            return self.getResistances()[drug]
        else:
            return False

    def reproduce(self, popDensity, activeDrugs):
        # If virus reproduces: generate info for initiating new ResistantVirus
        enough_space = random.random() <= self.getMaxBirthProb() * (1 - popDensity)
        resisted_drug = False
        try:
            if all(self.getResistances()[drug] == True for drug in activeDrugs): 
                resisted_drug = True
            if (enough_space) and (resisted_drug):
                new_resistances = {}
                # Generate new resistance dictionary
                for drug, resistance in self.getResistances().items():
                    # If random num is less than mutation prob, the mutation occurs
                    if random.random() <= self.getMutProb():
                        new_resistances[drug] = not(resistance)
                    else:
                        new_resistances[drug] = resistance
                return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), new_resistances, self.getMutProb())
            else:
                raise NoChildException
        except KeyError:
            # If the Virus doesn't have the drug in its resistances, it isn't resistant by definition
            raise NoChildException


class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        Patient.__init__(self, viruses, maxPop)
        self.treatments = []

    def addPrescription(self, newDrug):
        if newDrug not in self.treatments:
            self.treatments.append(newDrug)

    def getPrescriptions(self):
        return self.treatments

    def getResistPop(self, drugResist):
        num_vir = 0
        for virus in self.getViruses():
            # Check that drug is in Resistances before trying to access - avoids KeyError 
            try:
                if (drugResist) and (all(virus.getResistances()[drug] == True for drug in drugResist)): 
                    num_vir += 1
            except KeyError:
                pass
        return num_vir

    def update(self):
        survived = [virus for virus in self.viruses if not virus.doesClear()]
        self.viruses = survived.copy()
        for virus in survived:
            try:
                popdensity = self.getTotalPop()/self.getMaxPop()
                self.viruses.append(virus.reproduce(popdensity, self.getPrescriptions()))
            except NoChildException:
                pass
        return self.getTotalPop()

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    mydata = np.empty([300, numTrials + 1])
    mydata[:, :] = None
    resist_vir = mydata.copy()
    viruslist = [ResistantVirus(maxBirthProb = maxBirthProb, clearProb = clearProb,
        resistances = resistances, mutProb = mutProb) for _ in range(numViruses)]
    for col in range(numTrials):
        patient = TreatedPatient(viruslist, maxPop)
        for row in range(300):
            if row == 150:
                patient.addPrescription("guttagonol")
            mydata[row, col] = patient.update()
            resist_vir[row, col] = patient.getResistPop(["guttagonol"])

    mydata[:, numTrials] = np.mean(mydata[:, 0:numTrials], axis = 1)
    resist_vir[:, numTrials] = np.mean(resist_vir[:, 0:numTrials], axis = 1)

    pylab.plot(mydata[:,numTrials].tolist(), label = "ResistantVirus Total Population")
    pylab.plot(resist_vir[:,numTrials].tolist(), label = "ResistantVirus Resistant Population")
    pylab.title("ResistantVirus, Total and Resistant simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()
```