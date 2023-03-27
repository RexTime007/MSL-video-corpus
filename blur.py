import cv2
import mediapipe as mp

for i in range (7,15):
    print('---------------------------------'+str(i)+'----------------------------------')
    cap = cv2.VideoCapture("Z-"+str(i)+".mov")
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('#Z-'+str(i)+'.avi', fourcc, 30, (width, height), isColor=True)

    mpFaceDetection = mp.solutions.face_detection
    mpDraw = mp.solutions.drawing_utils
    faceDetection = mpFaceDetection.FaceDetection(0.75)
    c = 0

    while cap.isOpened():
        # get validity boolean and current frame
        ret, frame = cap.read()
        c = c+ 1
        if ret == True:
            print(c)
            imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = faceDetection.process(imgRGB)
            if results.detections:
                for id, detection in enumerate(results.detections):
                    # mpDraw.draw_detection(img, detection)
                    # print(id, detection)
                    # print(detection.score)
                    # print(detection.location_data.relative_bounding_box)
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, ic = frame.shape

                    # For blur box
                    bbox_x = int(bboxC.xmin * iw)
                    bbox_y = int(bboxC.ymin * ih)
                    old_width = int(bboxC.width * iw)
                    old_height = int(bboxC.height * ih)

                    # For rectange
                    bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

                    
                    frame[bbox_y:bbox_y+old_height,bbox_x:bbox_x+old_width] = cv2.medianBlur( frame[bbox_y:bbox_y+old_height,bbox_x:bbox_x+old_width],75)
                    
            
            frame = cv2.resize(frame, (width, height))
                
            out.write(frame)
        else:
            break
    out.release()
    cap.release()


"""
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    print(results)
    if results.detections:
            for id, detection in enumerate(results.detections):
                # mpDraw.draw_detection(img, detection)
                # print(id, detection)
                # print(detection.score)
                # print(detection.location_data.relative_bounding_box)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape

                # For blur box
                bbox_x = int(bboxC.xmin * iw)
                bbox_y = int(bboxC.ymin * ih)
                old_width = int(bboxC.width * iw)
                old_height = int(bboxC.height * ih)

                # For rectange
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

                
                img[bbox_y:bbox_y+old_height,bbox_x:bbox_x+old_width] = cv2.medianBlur( img[bbox_y:bbox_y+old_height,bbox_x:bbox_x+old_width],75)
                
                # cv2.rectangle(img, bbox, (255,0,255), 2)
    # if valid tag is false, loop back to start
"""