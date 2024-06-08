import subprocess
import numpy as np

class Screen:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.buffer_size = self.width * self.height * 3
        ffmpeg_command = ["ffmpeg",
                        "-hide_banner", "-loglevel", "error",
                        "-i", "pipe:",
                            "-max_delay", "30000000",
                            "-f", "rawvideo",
                            "-pix_fmt", "bgr24",
                            "pipe:"]

        screen_capture_command = ["screenrecord", "--output-format=h264", "--size", f"{self.width}x{self.height}",  "-"]
        self.screen_capture_process = subprocess.Popen(screen_capture_command, stdout=subprocess.PIPE)
        self.ffmpeg_process = subprocess.Popen(ffmpeg_command, stdin=self.screen_capture_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        self.buf_size = width * height * 3

    def __enter__(self):
        return self
    
    def screen_image(self):
        raw_frame = self.ffmpeg_process.stdout.read(self.buf_size)
        if len(raw_frame) != (self.buf_size):
            print("Error reading frame")
            raise Exception('Eror reading frame')
        return np.frombuffer(raw_frame, np.uint8).reshape((self.height, self.width, 3))

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Closing process')
        self.ffmpeg_process.terminate()
        self.ffmpeg_process.stdout.flush()
        self.screen_capture_process.terminate()
        self.screen_capture_process.stdout.flush()
        print('Closed all process')