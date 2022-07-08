import time
import cv2

vid_path = 'inference/rgb_streams/shortened_file-60fps.avi'
# vid_path = 'inference/rgb_streams/shortened_file-60fps.avi'

def rescale_frame(frame_input, shape = (540, 960)):
    width = shape[1]
    height = shape[0]
    dim = (width, height)
    return cv2.resize(frame_input, dim, interpolation=cv2.INTER_AREA)


cap = cv2.VideoCapture(vid_path)

if cap.isOpened():
    ret, frame = cap.read()
    if ret:
        rescaled_frame = rescale_frame(frame)
        (h, w) = rescaled_frame.shape[:2]
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter('inference/rgb_streams/video_output_540_640.mp4',
                             fourcc, 60.0,
                             (w, h), True)
    else:
        print('Done')
else:
    print("Camera is not opened")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        rescaled_frame = rescale_frame(frame, shape = (540, 640))

        # write the output frame to file
        writer.write(rescaled_frame)

        cv2.imshow("Output", rescaled_frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    else:
        break


cv2.destroyAllWindows()
cap.release()
writer.release()
