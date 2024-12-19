import cv2
from motion_detection import detect_motion
from llm_classification import classify_activity
from alert_system import send_alert_email
from recording_module import start_recording, stop_recording

def main():
    cap = cv2.VideoCapture(0)
    recording = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        motion_detected, processed_frame = detect_motion(frame)

        if motion_detected:
            description = "Movement detected near the window"
            classification = classify_activity(description)
            print(f"Classification: {classification}")

            if 'suspicious' in classification:
                send_alert_email("Alert: Suspicious Activity Detected", "Unusual movement detected near the monitored area.")
                if not recording:
                    start_recording(frame)
                    recording = True
            else:
                if recording:
                    stop_recording()
                    recording = False

        cv2.imshow('Home Safety System', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

