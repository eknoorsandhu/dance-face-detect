from mtcnn import MTCNN
import cv2
import os

detector = MTCNN()

def has_face(img):
    """
    Returns whether the image has a face or not

    Args:
        img (cv2.image): image to be processed

    Returns:
        bool
    """
    if len(detector.detect_faces(img)) > 0:
        return True
    else:
        return False

def get_face_frames(path, skip_count=3):
    """
    Reads the video from path and returns a list of frames
    where a face is detected. Writes them to faces/ folder

    Args:
        path (str): path to the video
        skip_count (int): number of frames to skip between detections

    Returns:
        list
    """
    frames = []
    cap = cv2.VideoCapture(path)
    ret, frame = cap.read()

    count = 0
    while ret:
        if count % skip_count == 0 and has_face(frame):
            frames.append(frame)
        ret, frame = cap.read()
        count += 1
    
    cap.release()

    # check if folder exists
    if not os.path.exists('./faces'):
        os.makedirs('./faces')

    # save frames
    for i, frame in enumerate(frames):
        cv2.imwrite('./faces/' + str(i) + '.jpg', frame)

    return frames
