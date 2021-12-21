# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../')
from src.vc_proc import equalizeHistogram, Gaussian, borderDetection


url = "../../src/data_especular_crop/"
urlN = "../../data_especular_crop-equalize/"
equalizeHistogram(url, urlN)

"""urlGaussian = "../../data_especular_crop-gaussian/"
Gaussian(urlN, urlGaussian)

urlBorder = "../../data_especular_crop-border/"
borderDetection(urlGaussian, urlBorder)"""