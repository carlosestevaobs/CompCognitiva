# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
from keras.models import Model
from keras.layers import Flatten, Dense
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import preprocess_input
from keras.callbacks import ModelCheckpoint,EarlyStopping
import seaborn as sns
from sklearn.metrics import confusion_matrix, precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score

import cv2
import os
import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from keras.applications.inception_v3 import preprocess_input
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint,EarlyStopping
import seaborn as sns
from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score
from keras.preprocessing.image import ImageDataGenerator

def equalizeHistogram(url, urlN):
    os.mkdir(urlN)
    arr = os.listdir(url)
    for i in range(len(arr)):
        os.mkdir(urlN+arr[i])
        urlC = os.listdir(url+arr[i])
        for j in range(len(urlC)):
            os.mkdir(urlN+arr[i]+"/"+urlC[j])
            arrImagens = os.listdir(url+arr[i]+"/"+urlC[j])
            for k in range(len(arrImagens)):
                img = cv2.imread(url+arr[i]+"/"+urlC[j]+"/"+arrImagens[k], cv2.IMREAD_GRAYSCALE)
                equ = cv2.equalizeHist(img)
                cv2.imwrite(urlN+arr[i]+"/"+urlC[j]+"/"+arrImagens[k],equ)

def Gaussian(url, urlN):
    os.mkdir(urlN)
    arr = os.listdir(url)
    for i in range(len(arr)):
        os.mkdir(urlN+arr[i])
        urlC = os.listdir(url+arr[i])
        for j in range(len(urlC)):
            os.mkdir(urlN+arr[i]+"/"+urlC[j])
            arrImagens = os.listdir(url+arr[i]+"/"+urlC[j])
            for k in range(len(arrImagens)):
                img = cv2.imread(url+arr[i]+"/"+urlC[j]+"/"+arrImagens[k], cv2.IMREAD_GRAYSCALE)
                blur = cv2.GaussianBlur(img,(5,5),0)
                cv2.imwrite(urlN+arr[i]+"/"+urlC[j]+"/"+arrImagens[k],blur)

def borderDetection(url, urlN):
    os.mkdir(urlN)
    arr = os.listdir(url)
    for i in range(len(arr)):
        os.mkdir(urlN+arr[i])
        urlC = os.listdir(url+arr[i])
        for j in range(len(urlC)):
            os.mkdir(urlN+arr[i]+"/"+urlC[j])
            arrImagens = os.listdir(url+arr[i]+"/"+urlC[j])
            for k in range(len(arrImagens)):
                img = cv2.imread(url+arr[i]+"/"+urlC[j]+"/"+arrImagens[k], cv2.IMREAD_GRAYSCALE)
                img = cv2.GaussianBlur(img, (3,3), 0)

                sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
                sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
                cv2.imwrite(urlN+arr[i]+"/"+urlC[j]+"/"+arrImagens[k],sobelx + sobely)

def treinarCNN(training_dir, validation_dir, test_dir):
    # verificar total de classes
    folders = glob(training_dir + '/*')
    num_classes = len(folders)

    # criar novas amostras
    batchSize = 32
    IMAGE_SIZE = [299, 299]
    training_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        preprocessing_function=preprocess_input)

    validation_datagen = ImageDataGenerator(rescale=1. / 255,
                                            preprocessing_function=preprocess_input)

    test_datagen = ImageDataGenerator(rescale=1. / 255,
                                      preprocessing_function=preprocess_input)

    training_generator = training_datagen.flow_from_directory(training_dir, target_size=IMAGE_SIZE, batch_size=32,
                                                              class_mode='categorical')
    validation_generator = validation_datagen.flow_from_directory(validation_dir, target_size=IMAGE_SIZE, batch_size=32,
                                                                  class_mode='categorical')
    test_generator = validation_datagen.flow_from_directory(test_dir, target_size=IMAGE_SIZE, batch_size=32,
                                                            class_mode='categorical')

    # criação da rede
    model = Sequential()
    model.add(Conv2D(filters=128, kernel_size=2, activation='relu', input_shape=(299, 299, 3)))
    model.add(MaxPooling2D(pool_size=2, padding='same'))
    model.add(Conv2D(filters=64, kernel_size=2, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, padding='same'))
    model.add(Conv2D(filters=32, kernel_size=2, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, padding='same'))
    model.add(Dropout(0.3))
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))

    model.summary()

    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    # criar ponto de salvamento com base no melhor modelo obtido
    checkpointer = ModelCheckpoint('BestCheckPoint.hdf5', verbose=1, save_best_only=True)
    stopper = EarlyStopping(monitor='val_acc', min_delta=0.1, patience=0, verbose=1, mode='auto')

    # treinamento
    batchSize = 32
    history = model.fit_generator(training_generator,
                                  steps_per_epoch=training_generator.n // batchSize,
                                  validation_data=validation_generator,
                                  validation_steps=validation_generator.n // batchSize,
                                  epochs=1,
                                  verbose=1,
                                  callbacks=[checkpointer])

    # gerar resultados
    Y_pred = model.predict_generator(test_generator)
    y_pred = np.argmax(Y_pred, axis=1)

    ax = sns.heatmap(confusion_matrix(test_generator.classes, y_pred), annot=True, cmap='Blues')

    ax.set_title('Matriz de confusão');
    plt.show()
    return recall_score(test_generator.classes, y_pred, average='micro'), precision_score(test_generator.classes, y_pred, average='micro')

def treinarVGG(training_dir, validation_dir, test_dir):
    folders = glob(training_dir + '/*')
    num_classes = len(folders)

    IMAGE_SIZE = [299, 299]

    vgg = VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)

    for layer in vgg.layers:
        layer.trainable = False

    x = Flatten()(vgg.output)
    x = Dense(num_classes, activation='softmax')(x)

    model = Model(inputs=vgg.input, outputs=x)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # model.summary()

    batchSize = 32

    training_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        preprocessing_function=preprocess_input)

    validation_datagen = ImageDataGenerator(rescale=1. / 255, preprocessing_function=preprocess_input)
    test_datagen = ImageDataGenerator(rescale=1. / 255, preprocessing_function=preprocess_input)
    training_generator = training_datagen.flow_from_directory(training_dir, target_size=IMAGE_SIZE, batch_size=32,
                                                              class_mode='categorical')
    validation_generator = validation_datagen.flow_from_directory(validation_dir, target_size=IMAGE_SIZE,
                                                                  batch_size=32, class_mode='categorical')
    test_generator = test_datagen.flow_from_directory(test_dir, target_size=IMAGE_SIZE, batch_size=32,
                                                      class_mode='categorical')

    # criar ponto de salvamento com base no melhor modelo obtido
    checkpointer = ModelCheckpoint('BestCheckPointVGG.hdf5', verbose=1, save_best_only=True)
    stopper = EarlyStopping(monitor='val_acc', min_delta=0.1, patience=0, verbose=1, mode='auto')

    history = model.fit(training_generator,
                        steps_per_epoch=training_generator.n // batchSize,
                        epochs=1,
                        validation_data=validation_generator,
                        validation_steps=validation_generator.n // batchSize,
                        callbacks=[checkpointer])

    Y_pred = model.predict_generator(test_generator)
    y_pred = np.argmax(Y_pred, axis=1)

    ax = sns.heatmap(confusion_matrix(test_generator.classes, y_pred), annot=True, cmap='Blues')
    ax.set_title('Matriz de confusão');
    plt.show()
    return recall_score(test_generator.classes, y_pred, average='micro'), precision_score(test_generator.classes,
                                                                                          y_pred, average='micro')