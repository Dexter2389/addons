"""
The TF-GAN project provides a lightweight GAN training/testing framework.
This file contains the core helper functions to create and train a GAN model.
See the README or examples in `tensorflow_models` for details on how to use.
TF-GAN training occurs in four steps:
1) Create a model
2) Add a loss
3) Create train ops
4) Run the train ops
The functions in this file are organized around these four steps. Each function
corresponds to one of the steps.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_addons.gan.python import namedtuples
