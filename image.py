import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

image_size = (150, 150)
batch_size = 32
epochs = 10
dataset_path = r"C:\Users\SEKAR PC\Downloads\model"  # 👈 Make sure this has class folders


def create_data_generators():
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train_data = datagen.flow_from_directory(
        dataset_path,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    val_data = datagen.flow_from_directory(
        dataset_path,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation',
        shuffle=False
    )

    return train_data, val_data
def build_model(input_shape, num_classes):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model


def evaluate_model(model, val_data):
    val_data.reset()
    predictions = model.predict(val_data, verbose=1)
    predicted_classes = np.argmax(predictions, axis=1)
    true_classes = val_data.classes
    class_labels = list(val_data.class_indices.keys())

    print("\n🔹 Classification Report:\n")
    print(classification_report(true_classes, predicted_classes, target_names=class_labels))

    print("\n🔹 Confusion Matrix:\n")
    cm = confusion_matrix(true_classes, predicted_classes)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()


def plot_training(history):
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Val Accuracy')
    plt.title("Accuracy")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Val Loss')
    plt.title("Loss")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    train_data, val_data = create_data_generators()
    model = build_model(input_shape=(*image_size, 3), num_classes=train_data.num_classes)

    print("\n🔹 Starting training...\n")
    print("Training samples:", train_data.samples)
    print("Validation samples:", val_data.samples)
    print("Classes:", train_data.class_indices)

    history = model.fit(train_data, validation_data=val_data, epochs=epochs)

    print("\n🔹 Evaluating on validation data...\n")
    evaluate_model(model, val_data)

    plot_training(history)
