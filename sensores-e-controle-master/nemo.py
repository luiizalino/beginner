
import cv2
import numpy as np

video_path = './capacitacao/sec/videonemo.mp4'
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
	# Reading current frame. 'is_grabbed' is true if the frame is read
	# correctly.
	is_grabbed, frame = cap.read()

	if is_grabbed:
		# Creating and resizing the original video's window.
		cv2.namedWindow('Original version', cv2.WINDOW_NORMAL)
		cv2.resizeWindow('Original version', 800, 600)
		cv2.imshow('Original version', frame)
    
		# hsv is an array, and each element represents a pixel of the
		# current 'frame' object.
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		# Both 'light_orange' and 'dark_orange' are RGB arrays. They will
		# be used to determine the range of the mask to be implemented in
		# the video. Anything between these two values should be shown in
		# the filtered video window.
		light_orange = np.array([1, 190, 200])
		dark_orange = np.array([18, 255, 255])
    
		# The mask must exclude from the video everything that isn't the
		# fish. To do so, for each element (or pixel) in the 'hsv' array,
		# the inRange() function checks if the element lies between
		# 'light_orange' and 'dark_orange'.
		mask = cv2.inRange(hsv, light_orange, dark_orange)

		"""
	Consider two arrays of the same size. For each element of these two,
the bitwise_and function checks if both elements are the same (in fancier words, it executes a binary conjunction for the 'frame'array). This calculation keeps going until the last element of both arrays.
    
	Because both inputs to the bitwise_and function are the same array
(the 'frame' object), the output should be a "copy" of the 'frame' object itself (You can check this by removing the mask argument from the bitwise_and function and running the code. The result should be the original video).

	The mask argument inside the bitwise_and function is specifying
which elements of the output (the "copy" of the 'frame' object) should be changed, that is which elements should be kept and which should be "hidden" in the video.
		"""
		filtered_frame = cv2.bitwise_and(frame, frame, mask=mask)

		# Creating and resizing the filtered video's window.
		cv2.namedWindow('Filtered version', cv2.WINDOW_NORMAL)
		cv2.resizeWindow('Filtered version', 800, 600)
		cv2.imshow('Filtered version', filtered_frame)
    
		# Conditions to stop the video by breaking the loop.
		if cv2.waitKey(27) & 0xFF == ord('q'):
			break
      
	else:
		# If the frame is not read correcty ('is_grabbed' is False), then
		# break the loop.
		break


cap.release()
cv2.destroyAllWindows()
