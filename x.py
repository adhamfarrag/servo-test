import cv2
import tensorflow as tf
from preprocessing import preprocess_input

# Load the model and labels
model = tf.keras.models.load_model('model/keras_model.h5')
labels = ['Good fruit', "Bad fruit"]

# Set up the video capture from the streaming server
capture = cv2.VideoCapture('http://192.168.0.140:9000/stream.mjpg')

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

    # Display the frame with the label and probability
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
