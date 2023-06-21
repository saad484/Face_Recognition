# import cv2
# from simple_facerec import SimpleFacerec

# # Encode faces from a folder
# sfr = SimpleFacerec()
# sfr.load_encoding_images("D:/python-opencv/face _recognition/images/")

# # Load Camera
# cap = cv2.VideoCapture(1)


# while True:
#     ret, frame = cap.read()

#     # Detect Faces
#     face_locations, face_names = sfr.detect_known_faces(frame)
#     for face_loc, name in zip(face_locations, face_names):
#         y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

#         cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

#     cv2.imshow("Frame", frame)

#     key = cv2.waitKey(1)
#     if key == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
from simple_facerec import SimpleFacerec
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

detector = FaceDetector()
arduino = SerialObject("COM5")

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("D:/python-opencv/face _recognition/images/")

# Load Camera
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    img, bboxs = detector.findFaces(frame)
    if any(name != "Unknown" for name in face_names):  # Check if any known face is detected
        arduino.sendData([1])
    else:
        arduino.sendData([0])

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


