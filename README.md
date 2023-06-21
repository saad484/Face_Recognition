# Face_Recognition
Facial recognition system using OpenCV and Python, with ESP32 integration for real-time control of external devices based on detected faces

This project showcases a face recognition system that combines an ESP32 microcontroller with Python programming and OpenCV library. The system detects and recognizes faces using a webcam connected to the computer, communicates with the ESP32 microcontroller over serial communication, and controls an LED and a servo motor based on the recognized faces.

## Python Code:
The Python code utilizes OpenCV and additional modules to perform face detection and recognition. It loads pre-encoded face images from a specified folder, detects faces in real-time video frames using the FaceDetector module, and matches the detected faces with the loaded encodings. The recognized faces are displayed on the screen with bounding boxes and labels. The program also sends signals to the ESP32 based on the presence of known faces.

## ESP32 Code:
The ESP32 code receives signals from the Python program over serial communication. It uses the cvzone library for serial data handling. When a known face is detected, the ESP32 turns on an LED connected to pin 4 and moves a servo motor attached to pin 9 to a 90-degree position. When an unknown face is detected, the LED is turned off, and the servo motor moves back to the 0-degree position.

### Dependencies:

OpenCV: A computer vision library used for face detection and recognition in the Python code.
cvzone: A Python library providing various utilities, including the FaceDetector and SerialData modules for face detection and serial communication, respectively.

### Potential Extensions:

Web Interface: Develop a web-based interface to control and monitor the face recognition system remotely.

Cloud Integration: Integrate the system with cloud platforms for data storage, analytics, and access control.

Voice Feedback: Implement voice feedback or alerts for face recognition results using text-to-speech technology.

Face Recognition on ESP32: Explore the possibility of performing face recognition directly on the ESP32 microcontroller using lightweight models and algorithms.
