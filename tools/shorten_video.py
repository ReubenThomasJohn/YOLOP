import cv2

def clip_video(start_time='2:40', end_time='3:10', vid_path='inference/videos/rgb_stream_204.avi', save_path='tools/shortened_file-60fps.avi'):

    cap = cv2.VideoCapture(vid_path)
    size = (int(cap.get(3)), int(cap.get(4)))

    fps = cap.get(cv2.CAP_PROP_FPS)
    print('fps:{}'.format(fps))
    start_mins, start_secs = start_time.split(':')
    end_mins, end_secs = end_time.split(':')
    end_frame = (int(end_mins) * 60 + (int(end_secs))) * int(fps)
    start_frame = (((int(start_mins) * 60) + int(start_secs))) * int(fps)
    # print('Clip starting at frame {start_frame}, and ending at {end_frame}'.format(start_frame, end_frame))

    result = cv2.VideoWriter(save_path, 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         fps, size)

    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video  file")
    frame_no = 0
    while(cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()
        frame_no += 1
        if ret == True:
            if frame_no % 500 == 0:
                # frame = cv2.resize(frame, (1920, 1080))
                print('Frame:{}'.format(frame_no))
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            if (frame_no >= start_frame and frame_no <= end_frame):
                result.write(frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        # Break the loop
        else: 
            break
   
    # When everything done, release 
    # the video capture object
    cap.release()
    result.release()
    # Closes all the frames
    cv2.destroyAllWindows()
    print('Result written to {}'.format(save_path))

clip_video(vid_path='inference/videos/rgb_stream_208.avi')
