__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


def frozen_graph(
        model_frozen_fpn='./frozen_model.pb'
):
    """
    You must use this function using TensorFlow 2x series.

    Parameters
    ----------
    pb_file_path

    Returns
    -------

    """
    import tensorflow as tf

    with tf.io.gfile.GFile(model_frozen_fpn, "rb") as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())

    def wrap_graph():
        tf.compat.v1.import_graph_def(graph_def, name="")

    tf.compat.v1.reset_default_graph()
    wrap_graph()
    graph = tf.compat.v1.get_default_graph()
    return graph