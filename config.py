'''
Define parameters here.
'''

import os

class config:

    # global parameters
    base_path = '/Users/zou/Desktop/Image-Caption' # path of this project
    caption_model = 'spatial_att' # 'show_tell', 'att2all', 'adaptive_att', 'spatial_att'
                                   # refer to README.md for more info about each model
    
    # dataset parameters
    dataset_image_path = os.path.join(base_path, 'flickr8k/images/')
    dataset_output_path = os.path.join(base_path, 'flickr8k/output/') # folder with data files saved by preprocess.py
    dataset_caption_path = os.path.join(base_path, 'flickr8k/dataset.json')
    dataset_basename = 'test1' # any name you want

    # preprocess parameters
    captions_per_image = 5
    min_word_freq = 5 # words with frenquence lower than this value will be mapped to '<UNK>'
    max_caption_len = 50 # captions with length higher than this value will be ignored,
                         # with length lower than this value will be padded from right side to fit this length

    # model parameters
    emb_dim = 512  # dimension of word embeddings
    attention_dim = 512  # dimension of attention network
    decoder_dim = 512  # dimension of decoder's hidden layer
    dropout = 0.5
    model_path = os.path.join(base_path, 'models/') # path to save models

    # training parameters
    epochs = 20
    batch_size = 32
    fine_tune_encoder = False  # fine-tune encoder or not
    encoder_lr = 1e-4  # learning rate of encoder (if fine-tune)
    decoder_lr = 4e-4  # learning rate of decoder
    grad_clip = 5.  # gradient threshold in clip gradients
    checkpoint = None  # path to load checkpoint, None if none
    workers = 1  # num_workers in dataloader
    tau = 1.  # penalty term τ in for doubly stochastic attention in paper: show, attend and tell
              # you only need to set this when 'caption_model' is set to 'att2all'