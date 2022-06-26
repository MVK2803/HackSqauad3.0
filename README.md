# HackSqauad3.0
## Adaptive Traffic Management System using Python and Open CV
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## INTRODUCTION 

Population in India is increasing day by day. More and more people are moving to urban areas.
So, with the increase in population and urbanization the problem of traffic is becoming more severe in big cities. 
The pressure of traffic also results in increasing numbers of road accidents.
In addition, there are people who have little road sense and often break the traffic rules. This too has resulted in road mishaps.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## WHY ?

The fact is that, the population of city and numbers of vehicles on the road are increasing day by day. 
With increasing urban population and hence the number of vehicles, need of controlling streets, highways and roads is major issue.
The main reason behind today’s traffic problem is the techniques that are used for traffic management. 
Today’s traffic management system is quite inefficient as it has no emphasis on live traffic scenario.
This project aims to prevent heavy traffic congestion by assigning traffic lights based on live traffic scenario.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## HOW ?
### 1.DETECTION MODULE

This module is responsible for detecting the number of vehicles in the image received as input from the camera.
More specifically, it will provide as output the number of vehicles of each vehicle class such as car, bike, bus, truck, and rickshaw.

### 2.SIGNAL SWITCHING MODULE:

This algorithm updates the red, green, and yellow times of all signals. 
These timers are set based on the count of vehicles of each class received from the vehicle detection module and several other factors such as the number of lanes, average speed of each class of vehicle, etc.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## THE DETECTION SYSTEM

YOLO(You Only Look Once)

YOLO algorithm is important because of the following reasons:

Speed: This algorithm improves the speed of detection because it can predict objects in real-time.
High accuracy: YOLO is a predictive technique that provides accurate results with minimal background errors.
Learning capabilities: The algorithm has excellent learning capabilities that enable it to learn the representations of objects and apply them in object detection.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## DEADLOCK PREVENTION


Always considering maximum could lead to deadlock i.e., a lane with least number of cars could be waiting for infinite time.
To prevent this situation we maintain a counter array with most output occurrences and when it exceeds 2 , for that iteration we give output to lane which hasn’t been a chance before

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## APPLICATIONS

1.Outdated signal timing currently accounts for more than 10 percent of all delays. 

2.On average, adaptive signal control technologies improve travel time by more than 10 percent. 

3.In areas with particularly outdated signal timing, improvements can be 50 percent or more.

4.Studies indicate that crashes could be reduced by up to 15 percent through improved signal timing.

5.Adaptive signal control technology can reduce the intersection congestion that causes many crashes.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## FUTURE SCOPE


1.Criminal tracking for rules violation and subsequent signal forwarding to nearest police station.

2.Collision detection & prediction.

3.Number plate detection.

4.Emergency vehicle detection like ambulance, fire brigade, police van, etc.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## INSTALLATION AND SETUP
### FILES
1.ref.py -- this python progarm made with the modules of opencv especially yolov3 is used to detect the vehicles

2.simulation.py --this python progaram is used to identify the configurations of the traffic signals based on the current traffic situation in 
a particular area

3.surveillance.m4v,rush.mp4,road.mp4 -- these are the video files that has been used as test cases for ref.py file
Note:In real life situation video is not being uploaded to the progarm,instead we are using the live feed from the roads.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------





