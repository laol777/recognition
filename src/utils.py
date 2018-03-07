import importlib
import sys
import random
import os.path
import cv2
import time
import torchvision.transforms as transforms
import torch
import torch.nn as nn
import torchvision.models as models
print_freq = 1

def setup(args):
    torch.set_num_threads(1)
    cv2.setNumThreads(1)

    args.cuda = True
    torch.backends.cudnn.benchmark = True
    
    torch.set_num_threads(4)

    try:
        os.makedirs(args.save_dir)
    except OSError:
        print('Directory was not created.')

    if args.manual_seed is None:
        args.manual_seed = random.randint(1, 10000)

    print("Random Seed: ", args.manual_seed)
    random.seed(args.manual_seed)
    torch.manual_seed(args.manual_seed)
    torch.cuda.manual_seed_all(args.manual_seed)


def get_optimizer(args):
    # Parse parameters 
    optimizer_args = {}
    for entry in args.optimizer_args.split(";"):
      k, v = entry.split('=')
      optimizer_args[k] = eval(v)

    # Optimizer
    optimizer = torch.optim.__dict__[args.optimizer](model.parameters(), **optimizer_args)

    return optimizer    


# def load_model(args):
#     '''
#     Loads generator model.
#     '''
#     m = importlib.import_module('models.' + args.model)
#     model, criterion = m.get_net(args)

    
#     return model, criterion
