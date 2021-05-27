# SVM Project
University project. 

The purpose of this project is motion detection based on accelerometer data. As a classifiacation algorithm support vetor machine was used. It is a extension to first version of the proejct in which classification was made using neural network in Edge Impulse: https://www.edgeimpulse.com/.

## Collected data description

Bicycle trainer allows to ride a real bike indoors. It allows to set an ammount of power into excercise. 

Motion detection is carried out by analyzing bike frame vibration.
3 types of movement were selected:
* pedalling with output power of 60 Watts
* pedalling with output power of 110 Watts
* standing still 
As a device capturing data smartphone accelerometer was used. Data was captured in Edge Impulse and exportet into .json files.

<p align="center">
  <img src="https://user-images.githubusercontent.com/83305684/119743198-a308ec00-be89-11eb-8691-9c962fb85361.png" width="600"/>
</p>
<p align="center">
  <em>Smartphone mounted on a bicycle trainer</em>
</p>

Collected overall of 39 (13 for each type of movement) samples of 10 seconds movement.

<p align="center">
  <img src="https://user-images.githubusercontent.com/83305684/119744193-c6cd3180-be8b-11eb-8046-d695dc9260b5.png" width="300"/>
  <img src="https://user-images.githubusercontent.com/83305684/119744220-d3518a00-be8b-11eb-9b7e-974d242e1a40.png" width="300"/> 
  <img src="https://user-images.githubusercontent.com/83305684/119744058-7c4bb500-be8b-11eb-996a-1c59f60d5aab.png" width="300"/>
</p>
<p align="center">
  <em>Sample data</em>
</p>

## Feature extraction
For each sample RMS (Root Mean Square) was calculated.

<p align="center">
  <img src="https://user-images.githubusercontent.com/83305684/119747086-3cd49700-be92-11eb-8a97-7a172ea552d4.png" width="500"/>
</p>
<p align="center">
  <em>RMS of each sample</em>
</p>

## Initial analysis
Data analysis started with visual assessment.

At first to simplify the task, only 2 types of movement were analyzed: 60 Watts and 110 Watts.

Plots in fever dimensions were drawn to check which of the features allowed to visualy seperate data.

<p align="center">
  <img src="https://user-images.githubusercontent.com/83305684/119747650-722db480-be93-11eb-9f96-e90b6caff2ab.png" width="400"/>
  <img src="https://user-images.githubusercontent.com/83305684/119747677-7eb20d00-be93-11eb-8894-d0b25f54bdd9.png" width="400"/> 
</p>
<p align="center">
  <em>Data in fewer dimensions</em>
</p>

First attempt in building motion recognition system was to classify data for only 2 labels (110 Watts and 60 Watts), in 2 dimensions (X RMS and Y RMS). Linear classifier was used.

<p align="center">
  <img src="https://user-images.githubusercontent.com/83305684/119747860-e7998500-be93-11eb-9620-6ff96b1e5fd9.png" width="450"/>
  <img src="https://user-images.githubusercontent.com/83305684/119747887-f3854700-be93-11eb-8c8c-42a663b19bd7.png" width="450"/> 
</p>
<p align="center">
  <em>Simplified classifier</em>
</p>

Ideal accuracy was alarming. In order to ensure the correctness of the classifier more data needed to be fed into the model. 

Instead of recordnig new data, moving split window was used. Each of 10 second data samples was broken into 1 second long periods.

<p align="center">
  <img src="https://user-images.githubusercontent.com/83305684/119748228-b7061b00-be94-11eb-8c28-3b2b06d3001f.png" width="500"/>
</p>
<p align="center">
  <em>Increased ammount of data</em>
</p>
