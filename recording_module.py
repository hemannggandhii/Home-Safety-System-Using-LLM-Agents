import cv2

out = None

def start_recording(frame, output_file='suspicious_activity.avi'):
    global out
    if out is None:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_file, fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    out.write(frame)

def stop_recording():
    global out
    if out is not None:
        out.release()
        out = None
