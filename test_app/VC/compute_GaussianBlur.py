# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../')
from src.vc_proc import equalizeHistogram, Gaussian, borderDetection

url = "../../data_especular_crop-equalize/"
urlN = "../../data_especular_crop-gaussian/"
Gaussian(url, urlN)
