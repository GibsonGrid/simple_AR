import cv2
import numpy as np
from pynput import keyboard

cv_file = cv2.FileStorage()
cv_file.open('./data/calibration/calib_cam.xml', cv2.FileStorage_READ)
camera_matrix = np.array(cv_file.getNode('K').mat(), dtype=np.float64)
dist_coeffs = np.array(cv_file.getNode('dist').mat(), dtype=np.float64)
cv_file.release()

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters_create()

cube_size = 1

# Define plane perpendicular to marker
video_plane_width = 2
video_plane_height = 2

video_plane_points = np.array([
    [video_plane_width / 2, 0,  video_plane_height / 2],  
    [-video_plane_width / 2, 0,  video_plane_height / 2],   
    [-video_plane_width / 2, 0, -video_plane_height / 2],  
    [video_plane_width / 2, 0, -video_plane_height / 2],  
], dtype=np.float32)

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

    if ids is not None:
        for i, corner in enumerate(corners):
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(
                corner, cube_size, camera_matrix, dist_coeffs)

            R, _ = cv2.Rodrigues(rvec)

            video_frame = cv2.flip(frame, 1)
            video_resized = cv2.resize(
                video_frame, (int(video_plane_width * 1000), int(video_plane_height * 1000)))

            src_pts = np.float32([[0, 0], [video_resized.shape[1], 0], [
                                 video_resized.shape[1], video_resized.shape[0]], [0, video_resized.shape[0]]])

            # Shift video plane if needed
            ### DO NOT DELETE THIS ###
            ### your code is here ###
            pass
            ### your code is here ###
            ### DO NOT DELETE THIS ###

            # Project points on marker using cv2.projectPoints
            ### DO NOT DELETE THIS ###
            ### your code is here ###
            pass
            ### your code is here ###
            ### DO NOT DELETE THIS ###

            # Get transfromation matrix using cv2.getPerspectiveTransform
            ### DO NOT DELETE THIS ###
            ### your code is here ###
            M_offset = cv2.getPerspectiveTransform()
            ### your code is here ###
            ### DO NOT DELETE THIS ###

            # AR like
            warped_video_offset = cv2.warpPerspective(
                video_resized, M_offset, (frame.shape[1], frame.shape[0]))
            cv2.imwrite('.utils/show.png', warped_video_offset)
            frame = cv2.addWeighted(frame, 1, warped_video_offset, 1, 0)

            # Non-transparent video
            # mask_original = np.ones(
            #     (video_resized.shape[0], video_resized.shape[1]), dtype=np.uint8) * 255
            # mask_warped = cv2.warpPerspective(
            #     mask_original, M_offset, (frame.shape[1], frame.shape[0]))
            # _, mask_warped = cv2.threshold(
            #     mask_warped, 1, 255, cv2.THRESH_BINARY)
            # mask_warped_3ch = cv2.cvtColor(mask_warped, cv2.COLOR_GRAY2BGR)
            # warped_region = cv2.bitwise_and(
            #     warped_video_offset, warped_video_offset, mask=mask_warped)
            # background = cv2.bitwise_and(
            #     frame, frame, mask=cv2.bitwise_not(mask_warped))
            # frame = cv2.add(background, warped_region)

    cv2.imshow("Video on cube plane", frame)
    cv2.waitKey(1)

    if terminate:
        break

cap.release()
cv2.destroyAllWindows()
