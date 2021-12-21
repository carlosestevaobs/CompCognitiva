# -*- coding: utf-8 -*-
import sys
# sys.path.insert(0, '../../')
from src.vc_proc import borderDetection

url = "../../data_especular_crop-gaussian/"
urlN = "../../data_especular_crop-border/"
borderDetection(url, urlN)