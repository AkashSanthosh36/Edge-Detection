import cv2
cap=cv2.VideoCapture('video.avi')
while(cap.isOpened()):
	ret,frame=cap.read()
	if(ret==True):
		#displaying the resulting frame
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame = cv2.GaussianBlur(frame, (45,45) , 0)
		canny = cv2.Canny(frame, 10, 30) # second and third parameter-thresholds(in here low threshold)
		#canny=cv2.Canny(frame,5,10)
		cv2.imshow("Canny with low thresholds", canny)
		cv2.waitKey(25)
		if(0XFF==ord('q')):
			break
	else:
		break	
cap.release()
cv2.destroyAllWindows()