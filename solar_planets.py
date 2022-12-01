import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sol", (100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))

cv2.putText(img,"Mercurio", (120,250),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"Venus", (190,260),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,185,225))
cv2.putText(img,"Terra", (290,260),cv2.FONT_HERSHEY_COMPLEX,0.4,(5,125,0))
cv2.putText(img,"lua", (328,190),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Marte", (380,250),cv2.FONT_HERSHEY_COMPLEX,0.4,(85,45,125))
cv2.putText(img,"Jupiter", (560,380),cv2.FONT_HERSHEY_COMPLEX,1,(0,165,185))
cv2.putText(img,"Saturno", (730,300),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,205,205))
cv2.putText(img,"Urano", (970,290),cv2.FONT_HERSHEY_COMPLEX,0.6,(165,185,0))
cv2.putText(img,"Netuno", (1120,285),cv2.FONT_HERSHEY_COMPLEX,0.5,(211,0,0))

cv2.imshow("showed image", img)
cv2.waitKey(0)