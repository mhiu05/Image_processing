import cv2

cat_img = cv2.imread('cat_img.jpeg')
cat_cascade = cv2.CascadeClassifier('cat_face.xml')

cats = cat_cascade.detectMultiScale(cat_img)

for (x, y, w, h) in cats:
    img = cv2.rectangle(cat_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img, 'Cat', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))

cv2.imshow('Cat', cat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
