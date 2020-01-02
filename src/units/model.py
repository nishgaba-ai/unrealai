import tensorflow as tf
from tensorflow.keras import Model



class ModelBlock(Model):
    
    """
        Model Block List for declaring custom models, and adding layers
    """

    def __init__(self):
        self.layers = []

    def add_layer(self, val):
        """"
            Method to add layer to the list
        """"

        self.layers.append(val)

    def add_optimizer(self):
        pass

    def add_loss(self):
        pass

    def compile(self):
        print(self.layers)
    
    def summary(self):
        pass

