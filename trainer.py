from tqdm import tqdm

import tensorflow as tf
from tensorflow.contrib.framework.python.ops import arg_scope

from network import Network

class Trainer(object):
  def __init__(self, config):
    self.K_d = config.K_d
    self.K_g = config.K_g

    self.initial_K_d = config.initial_K_d
    self.initial_K_g = config.initial_K_g

    self.learning_rate = config.learning_rate

    self.network = Network(config)

  def build_optim(self):
    self.optim = tf.train.GradientDescentOptimizer(self.learning_rate)

  def train(self):
    for k in range(self.initial_K_g):
      pass

    for k in range(self.initial_K_d):
      pass

    for step in range(self.max_step):
      for k in range(self.K_g):
        pass

      for k in range(self.K_d):
        pass