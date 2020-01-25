'''
    This file allows to convert the dataset to a tf_record compatible set using
    tf.train.Example format,
    currently implemented using tf.train.Feature

    # For details about the tf_record format and its use, please check the blog post below
    https://medium.com/mostly-ai/tensorflow-records-what-they-are-and-how-to-use-them-c46bc4bbb564

    # Corresponding reference of the functions used in TF Object Detection API are provided in the below file:
    https://github.com/tensorflow/models/blob/master/research/object_detection/utils/dataset_util.py

'''

# Imports
import tensorflow as tf


# Int 64 features for tf.train.Example
def int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

# Int 64 List for tf.train.Example
def int64_list_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=value))

# Int 64 features for tf.train.Example
def bytes_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

# Bytes List features for tf.train.Example
def bytes_list_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))

# Float List features for tf.train.Example
def float_list_feature(value):
  return tf.train.Feature(float_list=tf.train.FloatList(value=value))



def create_detection_pipeline( image_dir, annotations_path, labels_definition):
    '''
        Inputs image directory, the path of annotations and creates a TF record format to be used


        Args::
            image_dir (directory path): Directory path containing the images to be pipelined
            annotations_path (file_path):  File containing details about the annotations and labels for each corresponding image in image_dir, JSON Fromat File
            labels_definition (file path): File containing definition of total number of classes, JSON Format FILE

        
        Returns::
            records (TF Records): TF Record to be used in detection model
    '''





    return records


def create_classification_pipeline( image_dir, labels_path, labels_definition):
    '''
        Inputs image directory, labels path and creates a TF record format to be used

        Args::
            Args::
            image_dir (directory path): Directory path containing the images to be pipelined
            labels_path (file_path):  File containing details about the class lables for each corresponding image in image_dir, JSON Fromat File
            labels_definition (file path): File containing definition of total number of classes, JSON Format FILE

        Returns::
            records (TF Records): TF Record to be used in classification model

    '''


    return records


