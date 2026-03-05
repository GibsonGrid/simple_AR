import cv2
import numpy as np
from pynput import keyboard
import time
from utils import project_points_manual

cv_file = cv2.FileStorage()
cv_file.open('./data/calibration/calib_cam.xml', cv2.FileStorage_READ)
camera_matrix = np.array(cv_file.getNode('K').mat(), dtype=np.float64)
dist_coeffs = np.array(cv_file.getNode('dist').mat(), dtype=np.float64)
cv_file.release()

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters_create()

# Define path to your video
### your code is here ###
### DO NOT DELETE THIS ###
video_file_path = './data/imgs_videos/capybara.mp4'
### your code is here ###
### DO NOT DELETE THIS ###

cap_video = cv2.VideoCapture(video_file_path)

cube_size = 1
half = cube_size / 2

# Define cube faces
cube_faces = {
    "top": np.float32([[-half, -half, cube_size], [half, -half, cube_size], [half, half, cube_size], [-half, half, cube_size]]),
    "bottom": np.float32([[-half, -half, 0], [half, -half, 0], [half, half, 0], [-half, half, 0]]),
    "front": np.float32([[-half, -half, 0], [half, -half, 0], [half, -half, cube_size], [-half, -half, cube_size]]),
    "back": np.float32([[-half, half, 0], [half, half, 0], [half, half, cube_size], [-half, half, cube_size]]),
    "left": np.float32([[-half, -half, 0], [-half, half, 0], [-half, half, cube_size], [-half, -half, cube_size]]),
    "right": np.float32([[half, -half, 0], [half, half, 0], [half, half, cube_size], [half, -half, cube_size]])
}

# Video resize scale
scale = 3

# Define modes and which faces of the cube to use
mode = ["cube", "video_plane", "cube_video"]
video_faces = ["back"]

prev_frame_time = 0
new_frame_time = 0

# Define plane perpendicular to marker
### your code is here ###
### DO NOT DELETE THIS ###
video_plane_width = 2
video_plane_height = 2

video_plane_points = np.array([
    ###

], dtype=np.float32)
### your code is here ###
### DO NOT DELETE THIS ###

save = False
terminate = False


def on_key_press(key):
    global save, terminate
    if key == keyboard.Key.shift:
        print("Image saved!")
        save = True
    if key == keyboard.Key.esc:
        print("###### TERMINATE APPLICATION ######")
        terminate = True


listener = keyboard.Listener(on_press=on_key_press)
listener.start()

cap = cv2.VideoCapture(0)

width = 1920
height = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("M", "J", "P", "G"))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = cv2.aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters)

    ret_video, video_frame = cap_video.read()
    if not ret_video:
        cap_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    
    video_frame = cv2.flip(video_frame, 0)

    if ids is not None:
        for i, corner in enumerate(corners):
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(
                corner, cube_size, camera_matrix, dist_coeffs)

            projected_faces = {}
            for face, face_points in cube_faces.items():
                # Project points manually and compare with cv2.projectPoints
                ### DO NOT DELETE THIS ###
                ### your code is here ###
                pass
                ### your code is here ###
                ### DO NOT DELETE THIS ###

            # Draw Cube Wireframe
            if 'cube' in mode:
                ### DO NOT DELETE THIS ###
                ### your code is here ###
                pass 
                ### your code is here ###
                ### DO NOT DELETE THIS ###

            # Overlay Video on Selected Faces
            if 'cube_video' in mode:
                for face in video_faces:
                    if face in projected_faces:
                        img_pts = projected_faces[face]

                        # Define Video Corners
                        src_pts = np.float32([[0, 0], [video_frame.shape[1], 0],
                                              [video_frame.shape[1], video_frame.shape[0]], [0, video_frame.shape[0]]])

                        if len(img_pts) == 4:
                            # Compute perspective transformation using cv2.getPerspectiveTransform and cv2.warpPerspective
                            ### DO NOT DELETE THIS ###
                            ### your code is here ###
                            pass 
                            ### your code is here ###
                            ### DO NOT DELETE THIS ###

                            # Create mask for overlay
                            ### DO NOT DELETE THIS ###
                            ### your code is here ###
                            pass 
                            ### your code is here ###
                            ### DO NOT DELETE THIS ###

            if 'video_plane' in mode:
                # Copy code from 5_AR_video_plane.py starting from:
                R, _ = cv2.Rodrigues(rvec)
                
                ### DO NOT DELETE THIS ###
                ### your code is here ###
                pass 
                ### your code is here ###
                ### DO NOT DELETE THIS ###


    # Calculate fps
    ### DO NOT DELETE THIS ###
    ### your code is here ###
    new_frame_time = NotImplemented
    fps = None
    prev_frame_time = None
    #...
    ### your code is here ###
    ### DO NOT DELETE THIS ###

    cv2.imshow("Video on cube plane", frame)
    cv2.waitKey(1)

    if terminate:
        break

cap.release()
cap_video.release()
cv2.destroyAllWindows()
