import face_recognition
import numpy as np
import pickle

import os


#open encoding text file to write the encoding on
fe= open("cache/encode.txt","w+")

# Load a  sample picture and learn how to recognize it.
student_encodings=[]
image_names = os.listdir('Students/')

for i in image_names:
	student_image = face_recognition.load_image_file('Students/'+str(i))
	student_face_encoding = face_recognition.face_encodings(student_image)[0]	
	student_encodings.append(student_face_encoding)
		

known_face_encodings = student_encodings
np.savetxt(fe,known_face_encodings)

fe.close()



student_names=[]
for i in image_names:
	student_names.append(i.split('.')[0])


#open names text file to write the names on
with open("cache/names.txt","wb") as fn:
	pickle.dump(student_names,fn)

fn.close()
