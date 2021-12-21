# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../')

from src.vc_proc import treinarVGG

training_dir_1 = '../../data_especular_crop-equalize/test_images'
validation_dir_1 = '../../data_especular_crop-equalize/train_images'
test_dir_1 = '../../data_especular_crop-equalize/val_images'

x, y = treinarVGG(training_dir_1, validation_dir_1, test_dir_1)
print('Sensibilidade: ' + str(x))
print('Precisão: ' + str(y))