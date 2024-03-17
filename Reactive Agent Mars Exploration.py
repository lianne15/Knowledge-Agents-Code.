import random
#locations surveyed set 2 for unsurveyed
surveyed=[2,2,2,2]
class roverperformance:
    def __init__(self):
        self.score = 0
    def getScore(self):
        return self.score/8*100

class marsenvironment:
    def __init__(self):
        self.location = ["A","B","C","D"]
        self.locationcondition={"A":0,"B":0,"C":0,"D":0}
        #set conditions of locations
        for i in range(4):
            choice= random.choice([0,1])
            self.locationcondition[self.location[i]] = choice
        print(self.locationcondition)

class roveragent:
    def __init__(self,environment,performance):
        self.startLocation = random.choice([0,1,2,3])
        for i in range (4):
            if environment.locationcondition[environment.location[i]] == 1:
                if surveyed[i]==1:
                    print(environment.location[i]," Location has been sample before.")
                else:
                    print(environment.location[i]," has no rocks.")
                    surveyed[i]=1
            else:
                if surveyed[i]==2 or surveyed[i]==1:
                    print(environment.location[i]," Rocks Sample.")
                    surveyed[i]=0
                    performance.score+=1

                else:
                    print(environment.location[i]," has no rocks.")


total_performance=0
final_location=[]
for i in range(2):
    print("_________Exploration  Venture ",i,"_________")
    performance1 = roverperformance()
    environment1 = marsenvironment()
    roveragent1 = roveragent(environment1,performance1)
    total_performance+=performance1.getScore()
    final_location = environment1.locationcondition
print("Locations sampled",final_location)
print("Performance ", total_performance,"%")

Explanation
import random  # Import the random module for generating random numbers

# Initialize a list indicating unsurveyed locations
surveyed = [2, 2, 2, 2]

# Define a class for rover performance
class roverperformance:
    def __init__(self):
        self.score = 0  # Initialize the score attribute

    def getScore(self):
        return self.score / 8 * 100  # Calculate and return the score percentage

# Define a class for the Mars environment
class marsenvironment:
    def __init__(self):
        self.location = ["A", "B", "C", "D"]  # Locations on Mars
        self.locationcondition = {"A": 0, "B": 0, "C": 0, "D": 0}  # Condition of each location

        # Set conditions of locations randomly (0 or 1)
        for i in range(4):
            choice = random.choice([0, 1])
            self.locationcondition[self.location[i]] = choice
        print(self.locationcondition)  # Print the generated conditions

# Define a class for the rover agent
class roveragent:
    def __init__(self, environment, performance):
        self.startLocation = random.choice([0, 1, 2, 3])  # Randomly select a starting location

        # Iterate through each location in the environment
        for i in range(4):
            if environment.locationcondition[environment.location[i]] == 1:
                if surveyed[i] == 1:
                    print(environment.location[i], "Location has been sampled before.")
                else:
                    print(environment.location[i], "has no rocks.")
                    surveyed[i] = 1
            else:
                if surveyed[i] == 2 or surveyed[i] == 1:
                    print(environment.location[i], "Rocks Sample.")
                    surveyed[i] = 0
                    performance.score += 1
                else:
                    print(environment.location[i], "has no rocks.")

total_performance = 0  # Initialize total performance
final_location = []  # Initialize list to store final location data

# Loop for two exploration ventures
for i in range(2):
    print("_________Exploration Venture ", i, "_________")
    performance1 = roverperformance()  # Create rover performance instance
    environment1 = marsenvironment()  # Create Mars environment instance
    roveragent1 = roveragent(environment1, performance1)  # Create rover agent instance
    total_performance += performance1.getScore()  # Update total performance
    final_location = environment1.locationcondition  # Update final location data

print("Locations sampled", final_location)  # Print sampled locations
print("Performance ", total_performance, "%")  # Print overall performance

