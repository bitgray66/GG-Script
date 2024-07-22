import cv2

img = cv2.imread('wir60103.jpg')

# Get original height and width
print(f"Original Dimensions : {img.shape}")

# resize image by specifying custom width and height
f=10
h=427
w=641
nH = h*f
nW = w*f
resized = cv2.resize(img, (nW, nH))

print(f"Resized Dimensions : {resized.shape}")
cv2.imwrite('wir60103_resized_cv2x10.JPG', resized)