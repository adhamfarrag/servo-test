import cv2
import pyshine as ps


HTML = """
<html>
<head>
<title>PyShine Live Streaming</title>
<style>
body {
    margin: 0;
    }
img {
    width: 100%;
    height: 100%;
    }
</style>
</head>
<body>
<center><img src="stream.mjpg" width='1280' height='720' autoplay playsinline></center>
</body>
</html>
"""


def main():
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps, HTML)
    address = ('192.168.0.139', 9000)  # Enter your IP address
    try:
        StreamProps.set_Mode(StreamProps, 'cv2')
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_BUFFERSIZE, 4)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        capture.set(cv2.CAP_PROP_FPS, 30)
        StreamProps.set_Capture(StreamProps, capture)
        StreamProps.set_Quality(StreamProps, 90)
        server = ps.Streamer(address, StreamProps)
        print('Server started at', 'http://'+address[0]+':'+str(address[1]))
        server.serve_forever()

    except KeyboardInterrupt:
        capture.release()
        server.socket.close()


if __name__ == '__main__':
    main()
