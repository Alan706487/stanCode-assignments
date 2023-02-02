import keras
from keras.datasets import mnist
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout

# Load the mnist dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape the data
x_train = np.reshape(x_train, (x_train.shape[0], 28, 28, 1))
x_test = np.reshape(x_test, (x_test.shape[0], 28, 28, 1))

# Create a CNN model
model = Sequential()
model.add(Conv2D(32, kernel_size=3, activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, kernel_size=3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5)

# Predict the results
predictions = model.predict(x_test)


# Corrupt the images
def corrupt_image(image, corruption_rate=0.15):
    image_shape = image.shape
    num_pixels = image_shape[0] * image_shape[1]
    num_corrupted_pixels = int(num_pixels * corruption_rate)

    # Generate random indices of the pixels to be corrupted
    corrupted_indices = np.random.choice(num_pixels, num_corrupted_pixels, replace=False)

    # Set the pixels to white (255)
    for i in corrupted_indices:
        image[int(i / image_shape[1]), i % image_shape[1]] = 255

    return image


# Corrupt the test set with different corruption rates
x_test_corrupted_5 = np.array([corrupt_image(x_test[i], 0.05) for i in range(len(x_test))])
x_test_corrupted_10 = np.array([corrupt_image(x_test[i], 0.10) for i in range(len(x_test))])
x_test_corrupted_15 = np.array([corrupt_image(x_test[i], 0.15) for i in range(len(x_test))])

# Make predictions on the corrupted test set
predictions_5 = model.predict(x_test_corrupted_5)
predictions_10 = model.predict(x_test_corrupted_10)
predictions_15 = model.predict(x_test_corrupted_15)

# Report the prediction accuracies for the restored images
print('Accuracy of restored images with 5% corruption rate:', np.mean(np.argmax(predictions_5, 1) == y_test))
print('Accuracy of restored images with 10% corruption rate:', np.mean(np.argmax(predictions_10, 1) == y_test))
print('Accuracy of restored images with 15% corruption rate:', np.mean(np.argmax(predictions_15, 1) == y_test))

# import numpy as np
# import tensorflow as tf
# from tensorflow.keras import datasets, layers, models
# from keras.optimizers import RMSprop
#
# # Load MNIST dataset
# (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
#
# # Create a model
# model = models.Sequential()
#
# # Add 5 convolutional layers
# model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
#
# # Flatten the output of the convolutional layers to a single vector
# model.add(layers.Flatten())
#
# # Add a dense layer with 10 neurons (one for each digit)
# model.add(layers.Dense(10, activation='softmax'))
#
# # Compile the model
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# # Transform from (28, 28) to (28, 28, 1)
# train_images = train_images.reshape((60000, 28, 28, 1))
# test_images = test_images.reshape((10000, 28, 28, 1))
#
# # Convert from integers to floats
# train_images = train_images.astype('float32')
# test_images = test_images.astype('float32')
#
# # Normalize the images
# train_images /= 255
# test_images /= 255
#
# # Train the model
# model.fit(train_images, train_labels, epochs=5)
#
# # Evaluate the model
# test_loss, test_acc = model.evaluate(test_images, test_labels)
#
#
# # Restore the image
# def restore_image(image, corruption_rate):
#     # Convert from integers to floats
#     image = image.astype('float32')
#
#     # Add noise to the image
#     noise_mask = np.random.randint(2, size=image.shape)
#     noise_mask[noise_mask == 0] = 255
#     noisy_image = image + noise_mask * corruption_rate
#
#     # Normalise the image
#     noisy_image /= 255
#
#     # Restore the image
#     restored_image = model.predict(noisy_image)
#
#     # Denormalise the image
#     restored_image *= 255
#
#     return restored_image
#
#
# # Predict the accuracy for different corruption rates
# for corruption_rate in [0.05, 0.1, 0.15]:
#     # Restore the image
#     restored_image = restore_image(test_images, corruption_rate)
#
#     # Evaluate the model
#     test_loss, test_acc = model.evaluate(restored_image, test_labels)
#     print('Accuracy for corruption rate %f: %f' % (corruption_rate, test_acc))

# from __future__ import print_function
# from keras import layers
# from keras import models
# from keras import optimizers
# from keras.utils import to_categorical
# from keras.datasets import mnist
# import random
# import numpy as np
#
# # input image dimensions 28x28
# img_rows, img_cols = 28, 28
#
# # the data, split between train and test sets
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
#
# train_images = train_images.reshape((60000, 28, 28, 1))
# train_images = train_images.astype('float32') / 255
#
# test_images = test_images.reshape((10000, 28, 28, 1))
# test_images = test_images.astype('float32') / 255
#
# train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels)
#
# NUM_EPOCHS = 5
# BATCH_SIZE = 64
#
#
# def add_noise(noise_rate):
#     global test_images
#     for i in range(test_images.shape[0]):
#         gen = list(range(784))
#         temp = random.sample(gen, round(784 * noise_rate)) # select pixel randomly
#         for j in range(28):
#             for k in range(28):
#                 if j * k in temp:
#                     test_images[i][j][k][0] = 1
#
#
# def built_model():
#     model = models.Sequential()
#     model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
#     model.add(layers.MaxPooling2D((2, 2)))
#     model.add(layers.Conv2D(64, (3, 3), activation='relu'))
#     model.add(layers.MaxPooling2D((2, 2)))
#     model.add(layers.Conv2D(64, (3, 3), activation='relu'))
#     model.add(layers.Flatten())
#     model.add(layers.Dense(64, activation='relu'))
#     model.add(layers.Dense(10, activation='sigmoid'))
#     model.compile(loss='binary_crossentropy', optimizer=optimizers.RMSprop(lr=1e-4), metrics=['accuracy'])
#     return model
#
# model = built_model()
#
#
# model.fit(train_images, train_labels, epochs=NUM_EPOCHS, batch_size=BATCH_SIZE)
#
# add_noise(0.05)
# val_crossentropy, val_accuracy_with_noise_v1 = model.evaluate(test_images, test_labels, verbose=0)
#
# add_noise(0.1)
# val_crossentropy, val_accuracy_with_noise_v2 = model.evaluate(test_images, test_labels, verbose=0)
#
# add_noise(0.15)
# val_crossentropy, val_accuracy_with_noise_v3 = model.evaluate(test_images, test_labels, verbose=0)
#
# print('val_accuracy_with_noise_is_0.05 =', val_accuracy_with_noise_v1)
# print('val_accuracy_with_noise_is_0.1 =', val_accuracy_with_noise_v2)
# print('val_accuracy_with_noise_is_0.15 =', val_accuracy_with_noise_v3)
# #importing libraries
# import numpy as np
# import keras
# from keras.datasets import mnist
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Flatten
# from keras.layers import Conv2D, MaxPooling2D
# from keras import backend as K
#
# #loading the data
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
#
# #reshaping the data
# x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
# x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
#
# #setting data type
# x_train = x_train.astype('float32')
# x_test = x_test.astype('float32')
#
# #normalizing the data
# x_train /= 255
# x_test /= 255
#
# #converting labels to one hot encoding
# y_train = keras.utils.to_categorical(y_train, 10)
# y_test = keras.utils.to_categorical(y_test, 10)
#
# #building the model
# model = Sequential()
# model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(10, activation='softmax'))
#
# #compiling the model
# model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])
#
# #training the model
# model.fit(x_train, y_train, batch_size=128, epochs=12, verbose=1, validation_data=(x_test, y_test))
#
# #testing the model
# score = model.evaluate(x_test, y_test, verbose=0)
#
# #corrupting the data
# x_test_5 = x_test.copy()
# x_test_10 = x_test.copy()
# x_test_15 = x_test.copy()
#
# #setting 5%, 10%, and 15% of pixels to 255
# for i in range(x_test.shape[0]):
#   x_test_5[i] = np.where(np.random.rand(*x_test[i].shape) < 0.05, 255, x_test[i])
#   x_test_10[i] = np.where(np.random.rand(*x_test[i].shape) < 0.10, 255, x_test[i])
#   x_test_15[i] = np.where(np.random.rand(*x_test[i].shape) < 0.15, 255, x_test[i])
#
# #evaluating the model
# score_5 = model.evaluate(x_test_5, y_test, verbose=0)
# score_10 = model.evaluate(x_test_10, y_test, verbose=0)
# score_15 = model.evaluate(x_test_15, y_test, verbose=0)
#
# #reporting the prediction accuracy
# print("The prediction accuracy for 5% corruption is:", score_5[1])
# print("The prediction accuracy for 10% corruption is:", score_10[1])
# print("The prediction accuracy for 15% corruption is:", score_15[1])
#
# #comparing results
# print("As the corruption rate increases, the prediction accuracy decreases.")