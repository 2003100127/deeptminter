__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np


class DataInitializer:

    def input2d(self, data, bound_inf=None, bound_sup=None,):
        shape = data.shape
        num_samples = shape[0]
        num_features = shape[1]
        if bound_inf is not None and bound_sup is not None:
            x_data = data[:, 0: bound_inf].astype(np.float32)
            y_data = data[:, bound_sup: num_features].astype(np.float32)
            return x_data, y_data, num_samples
        elif bound_inf is None and bound_sup is None:
            return data, num_samples

    def batchData(self, x_data, y_data, totem, batch_size, y_dim=2):
        x_batch_data = x_data[totem*batch_size:(totem+1)*batch_size, :]
        if y_dim == 2:
            y_batch_data = y_data[totem*batch_size:(totem+1)*batch_size, :]
        else:
            y_batch_data = y_data[totem*batch_size:(totem+1)*batch_size]
        return x_batch_data, y_batch_data

    def testData(self, x_test, y_test, truncation_inf, truncation_sup, y_dim=2):
        x_data = x_test[truncation_inf:truncation_sup, :]
        if y_dim == 2:
            y_data = y_test[truncation_inf:truncation_sup, :]
        else:
            y_data = y_test[truncation_inf:truncation_sup]
        return x_data, y_data