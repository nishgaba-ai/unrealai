import tensorflow as tf
from tensorflow.keras import layers


class Convolution2D(layers.Layer):
    """
    Convolution 2D layer wrapper for Tensorflow 2.*
    This one is re-implementation of Standard Conv2D, but it is also used in standard form,
    as many more custom blocks will be used, hence this one is redundant but used for consistency in declaration of models
    
    Check for more details:
    https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D?version=stable


    tf.keras.layers.Conv2D
        __init__(
        filters,
        kernel_size,
        strides=(1, 1),
        padding='valid',
        data_format=None,
        dilation_rate=(1, 1),
        activation=None,
        use_bias=True,
        kernel_initializer='glorot_uniform',
        bias_initializer='zeros',
        kernel_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        **kwargs
    )


    """


    def __init__(self, filters, kernel_size, strides = (1, 1), padding = 'valid',
                data_format = None, dilation_rate = (1, 1), activation = None,
                use_bias = True, kernel_initializer = 'glorort_uniform', bias_initializer = 'zeros',
                kernel_regularizer = None, bias_regularizer = None, activity_regularizer = None,
                kernel_constraint = None, bias_constraint = None, **kwargs ):
        super(Convolution2D, self).__init__()
        self.conv = tf.keras.layers.Conv2D(filters = filters, kernel_size = kernel_size, strides = strides, padding = padding,
                data_format = data_format, dilation_rate = dilation_rate, activation = activation,
                use_bias = use_bias, kernel_initializer = kernel_initializer, bias_initializer = bias_initializer,
                kernel_regularizer = kernel_regularizer, bias_regularizer = bias_regularizer, activity_regularizer = activity_regularizer,
                kernel_constraint = kernel_constraint, bias_constraint = bias_constraint)

    @tf.function
    def call(self, inputs):
        return self.conv(inputs)


class Convolution1x1(layers.Layer):
    """
    Convolution 1x1 layer wrapper for Tensorflow 2.*
    Wrapper for easier 1x1 convolution declaration, internal working is same as Convolution 2D
    
    Check for more details:
    https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D?version=stable

    tf.keras.layers.Conv2D
        __init__(
        filters,
        kernel_size =(1, 1),
        strides=(1, 1),
        padding='valid',
        data_format=None,
        dilation_rate=(1, 1),
        activation=None,
        use_bias=True,
        kernel_initializer='glorot_uniform',
        bias_initializer='zeros',
        kernel_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        **kwargs
    )

    """

    def __init__(self, filters, kernel_size = (1, 1), strides = (1, 1), padding = 'valid',
                data_format = None, dilation_rate = (1, 1), activation = None,
                use_bias = True, kernel_initializer = 'glorort_uniform', bias_initializer = 'zeros',
                kernel_regularizer = None, bias_regularizer = None, activity_regularizer = None,
                kernel_constraint = None, bias_constraint = None, **kwargs ):
        super(Convolution1x1, self).__init__()
        self.conv = tf.keras.layers.Conv2D(filters = filters, kernel_size = (1, 1), strides = strides, padding = padding,
                data_format = data_format, dilation_rate = dilation_rate, activation = activation,
                use_bias = use_bias, kernel_initializer = kernel_initializer, bias_initializer = bias_initializer,
                kernel_regularizer = kernel_regularizer, bias_regularizer = bias_regularizer, activity_regularizer = activity_regularizer,
                kernel_constraint = kernel_constraint, bias_constraint = bias_constraint)

    @tf.function
    def call(self, inputs):
        return self.conv(inputs)





