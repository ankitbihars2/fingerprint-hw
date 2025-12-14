import cv2

rtsp_url = "rtsp://username:admin@admin/Streaming/Channels/101"

cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to get frame")
        break

    cv2.imshow("IP Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

