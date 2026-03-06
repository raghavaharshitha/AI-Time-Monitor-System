AI Camera Time Monitoring System
Overview

This project detects people using a webcam and measures how long each person stays in the camera view.
It uses YOLOv8 for person detection and DeepSORT for tracking to assign a unique ID and show the time spent by each person in real time.

Features

Real-time person detection

Multi-person tracking

Unique ID for each person

Timer showing time spent in camera

Technologies

Python

YOLOv8 (Ultralytics)

OpenCV

DeepSORT

NumPy

PyTorch

Installation

git clone https://github.com/yourusername/AI-Time-Monitor-System.git

cd AI-Time-Monitor-System

python -m venv venv

venv\Scripts\activate

pip install ultralytics opencv-python deep-sort-realtime numpy torch torchvision

Run Project

python tracking.py

Press ESC to close the camera.

Output Example
ID 1   Time 00:12
ID 2   Time 00:07
ID 3   Time 00:04

BTech Final Year Project – AI Computer Vision System

https://github.com/user-attachments/assets/f0514689-ca54-4012-9b3a-26d997c16b73

<img width="1536" height="1024" alt="result-1" src="https://github.com/user-attachments/assets/0182525c-6d1f-41bc-9bd1-6ae079f6d554" />
<img width="1536" height="1024" alt="result-2" src="https://github.com/user-attachments/assets/8d4e4c8f-1a1d-463f-95a0-ff727e40ac7a" />



