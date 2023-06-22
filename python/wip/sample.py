#!/usr/bin/env python

import copy
import math
import time
import numpy

import cv2 as cv
from pupil_apriltags import Detector


def main():
    CAM_ID = 0

    cap = cv.VideoCapture(CAM_ID)

    at_detector = Detector(
        families="tag36h11",
        nthreads=8,
        quad_decimate=2.0,
        quad_sigma=0.0,
        refine_edges=1,
        decode_sharpening=0.25,
        debug=0,
    )

    elapsedTime = 0

    while True:
        startTime = time.time()

        ret, image = cap.read()

        if not ret:
            break
        debugImage = copy.deepcopy(image)

        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        tags = at_detector.detect(
            image,
            estimate_tag_pose=False,
            camera_params=None,
            tag_size=None,
        )

        debugImage = draw_tags(debugImage, tags, elapsedTime)

        elapsedTime = time.time() - startTime

        key = cv.waitKey(1)
        if key == 27:  # ESC
            break

        cv.imshow('AprilTag Detect Demo', debugImage)

    cap.release()
    cv.destroyAllWindows()

def draw_tags(image: numpy.ndarray, tags: list, elapsed_time: int):
    for tag in tags:
        tag_family = tag.tag_family
        tag_id = tag.tag_id
        center = tag.center
        corners = tag.corners

        center = (int(center[0]), int(center[1]))
        corner_01 = (int(corners[0][0]), int(corners[0][1]))
        corner_02 = (int(corners[1][0]), int(corners[1][1]))
        corner_03 = (int(corners[2][0]), int(corners[2][1]))
        corner_04 = (int(corners[3][0]), int(corners[3][1]))

        cv.circle(image, (center[0], center[1]), 5, (0, 0, 255), 2)

        cv.line(image, (corner_01[0], corner_01[1]),
                (corner_02[0], corner_02[1]), (255, 0, 0), 2)
        cv.line(image, (corner_02[0], corner_02[1]),
                (corner_03[0], corner_03[1]), (255, 0, 0), 2)
        cv.line(image, (corner_03[0], corner_03[1]),
                (corner_04[0], corner_04[1]), (0, 255, 0), 2)
        cv.line(image, (corner_04[0], corner_04[1]),
                (corner_01[0], corner_01[1]), (0, 255, 0), 2)
        cv.putText(image, str(tag_id), (center[0] - 10, center[1] - 10),
                cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2, cv.LINE_AA)

    # cv.putText(image,
    #            "Elapsed Time:" + '{:.1f}'.format(elapsed_time * 1000) + "ms",
    #            (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
    #            cv.LINE_AA)

    return image

def calculateDistance(CAM_HEIGHT, CAM_ANGLE, TAG_HEIGHT, VERT_OFFSET):
    # return (TAG_HEIGHT - CAM_HEIGHT) / numpy.tan(numpy.radians(CAM_ANGLE))
    HEIGHT_DIFF = TAG_HEIGHT - CAM_HEIGHT
    VERT_OFFSET += CAM_ANGLE

    return HEIGHT_DIFF/math.tan(math.radians(VERT_OFFSET))

    #A:
    #   angle = VERT_OFFSET
    #   length = HEIGHT_DIFF
    #B:
    #   angle = 90 - angle A
    #   length = ?
    #C:
    #   angle = 90
    #   length = ?



if __name__ == '__main__':
    main()
