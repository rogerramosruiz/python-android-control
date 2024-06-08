# from control.actions import press, swipe
from screen.screen import Screen
import cv2 as cv
import time


if __name__ == '__main__':
    # press(491.1, 1280.5)
    #swipe(587, 709, 303, 709)

    height = 1920
    width = 1080

    start = time.time()
    fps_s = 0
    buf_size = width * height * 3
    count = 0

    out = cv.VideoWriter('output.mp4', cv.VideoWriter_fourcc(*'mp4v'), 60, (width, height))
    with Screen(width, height) as screen:
        while True:
            start_t = time.time()
            frame = screen.screen_image()
            out.write(frame)
            end_t = time.time() - start_t
            fps = 1.0 / end_t
            fps_s += fps
            count += 1
            if time.time() - start > 20:
                break
    
    out.release()

    print('avg fpgs', fps_s / count)
    print(count)