import face_recognition
import cv2
from datetime import datetime
import numpy as np
import platform
import pickle

import os
#import glob

def get_jetson_gstreamer_source(capture_width=1280, capture_height=720, display_width=1280, display_height=720, framerate=60, flip_method=0):
    """
    Return an OpenCV-compatible video source description that uses gstreamer to capture video from the camera on a Jetson Nano
    """ 
    return (
            f'nvarguscamerasrc ! video/x-raw(memory:NVMM), ' +
            f'width=(int){capture_width}, height=(int){capture_height}, ' +
            f'format=(string)NV12, framerate=(fraction){framerate}/1 ! ' +
            f'nvvidconv flip-method={flip_method} ! ' +
            f'video/x-raw, width=(int){display_width}, height=(int){display_height}, format=(string)BGRx ! ' +
            'videoconvert ! video/x-raw, format=(string)BGR ! appsink'
            )

#open attendance text file to write the names on
f= open("Attendance/attendance"+datetime.now().strftime("%m-%d-%Y_%H:%M")+".txt","w+")

#array to make sure that a name isn't written twice on the file				
unique_attendance = []

#read the images names from the Students directory
image_names = os.listdir('Students/')


#student_names=[]
#for i in image_names:
	#student_names.append(i.split('.')[0])
	

#Read face encodings from encode.txt
known_face_encodings = np.genfromtxt('cache/encode.txt')


with open("cache/names.txt","rb") as fp:
	known_face_names = pickle.load(fp)

#known_face_names = np.genfromtxt('cache/names.txt')





def main_loop():
	# Initialize some variables
	face_locations = []
	face_encodings = []
	face_names = []
	process_this_frame = 1

	video_capture = cv2.VideoCapture(get_jetson_gstreamer_source(), cv2.CAP_GSTREAMER)

	while True:
		# Grab a single frame of video
		ret, frame = video_capture.read()

		# Resize frame of video to 1/5 size for faster face recognition processing
		small_frame = cv2.resize(frame, (0, 0), fx=0.20, fy=0.20)

		# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
		rgb_small_frame = small_frame[:, :, ::-1]

		# Find all the face locations and face encodings in the current frame of video
		face_locations = face_recognition.face_locations(rgb_small_frame)
		face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
		
		
		
		# Only process every other frame of video to save time
		if process_this_frame==1:
			# Find all the faces and face encodings in the current frame of video
			face_locations = face_recognition.face_locations(rgb_small_frame)
			face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

			face_names = []
			for face_encoding in face_encodings:
				# See if the face is a match for the known face(s)
				matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
				name = "Unknown"



				# Or instead, use the known face with the smallest distance to the new face
				face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
				best_match_index = np.argmin(face_distances)

				if matches[best_match_index]:
					name = known_face_names[best_match_index]
					if not best_match_index in unique_attendance:
						unique_attendance.append(best_match_index)						
						f.write(name + '\t' + str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) +'\n')
					

				face_names.append(name)

		process_this_frame = 1 if process_this_frame == 3 else process_this_frame+1


		# Display the results
		for (top, right, bottom, left), name in zip(face_locations, face_names):
		# Scale back up face locations since the frame we detected in was scaled to 1/4 size
			top *= 5
			right *= 5
			bottom *= 5
			left *= 5

			# Draw a box around the face
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

			# Draw a label with a name below the face
			cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
			font = cv2.FONT_HERSHEY_DUPLEX
			cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


		



		cv2.imshow('Video', frame)
		
		# Hit 'q' on the keyboard to quit!
		if cv2.waitKey(1) & 0xFF == ord('q'):
            		#save_known_faces()
            		break

	f.close()
	video_capture.release()
	cv2.destroyAllWindows()
    	



