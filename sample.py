from __future__ import print_function
import numpy as np
import tensorflow as tf

import argparse
import time
import os
from six.moves import cPickle

from utils import TextLoader
from model import Model

class samples():
     def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--save_dir', type=str, default='save',
                       help='model directory to load stored checkpointed models from')
        parser.add_argument('-n', type=int, default=200,
                       help='number of words to sample')
        parser.add_argument('--prime', type=str, default=" ",
                       help='prime text')
        parser.add_argument('--pick', type=int, default=1,
                       help='1 = weighted pick, 2 = beam search pick')
        parser.add_argument('--width', type=int, default=4,
                       help='width of the beam search')
        parser.add_argument('--sample', type=int, default=1,
                       help='0 to use max at each timestep, 1 to sample at each timestep, 2 to sample on spaces')

        args = parser.parse_args()
        self.sampler(args)
        
     def sampler(self,args):
          self.args = args
          with open(os.path.join(args.save_dir, 'config.pkl'), 'rb') as f:
               self.saved_args = cPickle.load(f)
          with open(os.path.join(args.save_dir, 'words_vocab.pkl'), 'rb') as f:
            self.words, self.vocab = cPickle.load(f,encoding='utf-8')
          self.model = Model(self.saved_args, True)
          
                #return ""+model.sample(sess, words, vocab, args.n, `ss , args.sample, args.pick, args.width)

     def outputer(self,strs):
          with tf.Session() as self.sess:
            tf.global_variables_initializer().run()
            self.saver = tf.train.Saver(tf.global_variables())
            self.ckpt = tf.train.get_checkpoint_state(self.args.save_dir)
            if self.ckpt and self.ckpt.model_checkpoint_path:
                self.saver.restore(self.sess, self.ckpt.model_checkpoint_path)
                return ""+self.model.sample(self.sess, self.words, self.vocab, self.args.n,strs , self.args.sample, self.args.pick, self.args.width)
          
if __name__ == '__main__':
     sam = samples();
     sam.main("heello")
    
