__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
import numpy as np
import tensorflow as tf
import pandas as pd
from src.DataInitializer_dprs import dataInitializer_dprs
from src.SSFasta_dprs import fasta_dprs as sfasta
from src.Fasta_dprs import fasta_dprs as pfasta
from src.Length_dprs import length_dprs as lscenario


def deeptminter_call():
    batch_size = 100
    sess = tf.Session()
    saver = tf.train.import_meta_graph(sys.argv[1])
    saver.restore(sess, sys.argv[2])
    tf_graph = tf.get_default_graph()
    x = tf_graph.get_tensor_by_name("x_1:0")
    prediction = tf_graph.get_tensor_by_name("presoftmax:0")
    print("Protein: {}".format(sys.argv[3] + sys.argv[4]))
    accumulator = []
    x_test, y_test, num_test_samples = dataInitializer_dprs().input2d(
        sys.argv[5] + sys.argv[3] + sys.argv[4] + sys.argv[7],
        bound_inf=676,
        bound_sup=-2,
        sep='\s+'
    )
    num_batch_test = num_test_samples // batch_size
    final_number = num_test_samples % batch_size
    for batch in range(num_batch_test + 1):
        if batch < num_batch_test:
            x_batch_te, y_batch_te = dataInitializer_dprs().batchData(
                x_test, y_test, batch, batch_size
            )
        else:
            x_batch_te = x_test[batch*batch_size: (batch*batch_size+final_number), :]
        feed_dict_test = {x: x_batch_te}
        pred_tmp = sess.run(prediction, feed_dict=feed_dict_test)
        accumulator.append(pred_tmp)
    pred_data = accumulator[0]
    for i in range(1, len(accumulator)):
        pred_data = np.concatenate((pred_data, accumulator[i]), axis=0)
    sequence = sfasta().get(
        fasta_path=sys.argv[5],
        fasta_name=sys.argv[3],
        file_chain=sys.argv[4]
    )
    length_pos_list = lscenario().toSingle(len(sequence))
    position = pfasta(sequence).single(pos_list=length_pos_list)
    res = np.array(position)[:, [0, 1]]
    pred_data = np.concatenate((res, pred_data[:, [1]]), axis=1)
    return pd.DataFrame(pred_data).to_csv(
        sys.argv[6] + sys.argv[3] + sys.argv[4] + sys.argv[8],
        sep='\t',
        header=None,
        index=False
    )
deeptminter_call()