# gpt-LineBot
<h2>
The project involves implementing an intelligent LINE chatbot that integrates the OpenAI API with LINE developer tools. Additionally, the functions are deployed on Google Cloud Functions, eliminating the need for self-hosted servers.</h2>

# Functionality

## Wafer Peeling Speed Detection
* **Object Detection**：Utilizes YOLOv8 to detect a variety of objects including 'BareWafer', 'PW', 'Plate', 'Ring', 'Wafer', 'Hand', 'Tape','Forceps'.
  
* **Algorithm for Speed** Calculation: Implements a custom algorithm to calculate the speed of tape peeling.
  
* **GUI Interface**: Allows the addition of multiple IP cameras from different sources for image input, enabling simultaneous detection.
  
* **Multi-Process** Architecture: This feature ensures efficient handling of various tasks in parallel.

## Finger Cot Changing Detection
* **Technology Base**: Employs YOLOv8 and MediaPipe Hands for foundational technology.
  
* **Behavior Recognition**: Identifies the actions of operators to determine if there has been a change in finger cots.
  
* **Versatile Image Input**: Capable of receiving image inputs from various IP camera sources, similar to the Wafer Detection functionality.

# Usage

Execute the following command to install all the required packages:

```
pip install -r requirements.txt
```

Execute the following wrapper.py to start the gui program

```
cd IAC_Project

python wrapper.py
```

**In actual use, some parameters need to be modified**
