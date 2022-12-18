import cv2
import pyshine as ps
import tensorflow as tf

# Load the model and labels
model = tf.keras.models.load_model('model/keras_model.h5')
labels = ['label1', 'label2', 'label3', ...]

# Set up the streaming server
html = """
<html>
<head>
<title>Video Streaming with TensorFlow Model</title>
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
StreamProps = ps.StreamProps
StreamProps.set_Page(StreamProps, html)
address = ('192.168.0.140', 9000)  # Enter your IP address

# Set up the video capture from the USB camera
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_BUFFERSIZE, 4)
# make the stream match a 720 camera
capture.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,  720)
capture.set(cv2.CAP_PROP_FPS, 30)
StreamProps.set_Capture(StreamProps, capture)
StreamProps.set_Quality(StreamProps, 90)
server = ps.Streamer(address, StreamProps)

while True:
    # Capture and preprocess the frame
    _, frame = capture.read()
    preprocessed_frame = preprocess_input(frame)

    # Use the model to classify the frame
    class_probs = model.predict(preprocessed_frame)

    # Extract the class label with the highest probability
    class_label = np.argmax(class_probs)

    # Print the classification results
    print(f'Class label: {class_label}')
    print(f'Class probabilities: {class_probs}')

    # Add the label and probability to the frame
    cv2.putText(frame, f'Label: {labels[class_label]}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)
    cv2.putText(frame, f'Probability: {class_probs[class_label]:.2f}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    # Encode the frame and send it to the server
    server.send_frame(frame)

capture.release()
server.socket.close()
