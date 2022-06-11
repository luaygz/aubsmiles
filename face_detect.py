import cv2

cap = cv2.VideoCapture("data/clip.webm")

while True:
	success, frame = cap.read()
	if not success:
		break

	cv2.imshow("Video", frame)
	k = cv2.waitKey(30) & 0xff
	if k==27:
		break

cap.release()