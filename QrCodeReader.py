import cv2

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()


stockage = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    data, bbox, _ = detector.detectAndDecode(frame)

    if data:
        print("QR Code détecté :", data)
        cv2.putText(frame, data, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    

    cv2.imshow("QR Code Reader", frame)
    stockage.append(data)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # ESC pour quitter
        break

cap.release()
cv2.destroyAllWindows()

print(stockage)