import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

def load_face_encoding(image_path):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if len(encodings) == 0:
        raise ValueError(f"No faces found in image: {image_path}")
    return encodings[0]

try:
    jobs_encoding = load_face_encoding("Steve_jobs.jpg")
    ratan_tata_encoding = load_face_encoding("Ratan_tata.jpg")
    Lata_mangeshkar_encoding = load_face_encoding("Lata_mangeshkar.jpg")
    Sharukh_khan_encoding = load_face_encoding("Sharukh_khan.webp")
except ValueError as e:
    print(e)
    exit(1)


known_face_encodings = [
    jobs_encoding,
    ratan_tata_encoding,
    Lata_mangeshkar_encoding,
    Sharukh_khan_encoding
]

known_face_names = [
    "jobs",
    "ratan tata",
    "Lata mangeshkar",
    "Sharukh khan"
]

students = known_face_names.copy()


face_locations = []
face_encodings = []
face_names = []

video_capture = cv2.VideoCapture(0)

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
csv_file = f'attendance_{current_date}.csv'

with open(csv_file, 'w+', newline='') as f:
    lnwriter = csv.writer(f)
    lnwriter.writerow(["Name", "Time"])


    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame.")
            break


        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

        for name in face_names:
            if name in students:
                students.remove(name)
                current_time = datetime.now().strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])
                print(f"Logged: {name} at {current_time}")

        cv2.imshow("Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video_capture.release()
cv2.destroyAllWindows()

