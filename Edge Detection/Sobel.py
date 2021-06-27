import cv2
cap=cv2.VideoCapture('video.avi')
while(cap.isOpened()):
	ret,frame=cap.read()
	if(ret==True):
		#displaying the resulting frame
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=3)
		sobely=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=3)
		laplacian = cv2.Laplacian(frame,cv2.CV_64F) 
		cv2.imshow('sobel',laplacian)
		if(cv2.waitKey(25) & 0XFF==ord('q')):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()				