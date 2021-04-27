import cv2 # import open cv 
img = cv2.imread('abc.jpg' , 1 )#''' read image and store in variabl img'''
cv2.imshow('image', img)#''' showing image'''
k = cv2.waitKey(5000)#''' wait for 5 sec '''
if k == 27:#''' if Esc key will press'''
    cv2.destroyAllWindows() #''''' close image '''
elif k==ord('s'):
#''' if s key will press new image save with abcd.jpg  '''
    cv2.imwrite('abcd.jpg' , img)
    cv2.destroyAllWindows()#destroy all windows
