import argparse
import importlib
import os
import torch
import shutil
from huepy import red, green 

# Define main args
parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add = parser.add_argument

parser.add('--exp_dir', type=str, default="", help='')
parser.add('--no-dry-run', action='store_true')
parser.add('--min_checkpoints', type=int, default=1)

args = parser.parse_args()

import glob

for exp_path in glob.glob(f'{args.exp_dir}/*'):

    checkpoints = glob.glob(f'{exp_path}/checkpoints/*')

    if len(checkpoints) < args.min_checkpoints:
        print('Deleting ', red(exp_path))

        if args.no_dry_run:
            shutil.rmtree(exp_path)
    else:
       print('Leaving ', green(exp_path))
