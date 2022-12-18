import cv2
import pyshine as ps
import tensorflow as tf

# Load the Keras model that you trained in Teachable Machine
model = tf.keras.models.load_model('model/keras_model.h5')

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
    address = ('192.168.0.140', 9000)  # Enter your IP address
    try:
        StreamProps.set_Mode(StreamProps, 'cv2')
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_BUFFERSIZE, 4)
        # make the stream match a 720 camera
        capture.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)
        capture.set(cv2.CAP_PROP_FPS, 30)
        StreamProps.set_Capture(StreamProps, capture)
        StreamProps.set_Quality(StreamProps, 90)
        server = ps.Streamer(address, StreamProps)
        print('Server started at', 'http://'+address[0]+':'+str(address[1]))

        while True:
            # Capture and preprocess the frame
            _, frame = capture.read()
            # Add your own preprocessing function here
            preprocessed_frame = preprocess_input(frame)

            # Use the model to classify the frame
            class_probs = model.predict(preprocessed_frame)

            # Extract the class label with the highest probability
            class_label = np.argmax(class_probs)

            # Print the classification results
            print(f'Class label: {class_label}')
            print(f'Class probabilities: {class_probs}')

        server.serve_forever()

    except KeyboardInterrupt:
        capture.release()
        server.socket.close()


if __name__ == '__main__':
    main()
