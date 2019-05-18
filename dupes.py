#!/usr/bin/env python3
# Corey Goldberg, 2019

"""dupes - Detect visually similar images with perceptual hashing."""


import argparse
import os
import sys
from collections import defaultdict

from imagehash import whash, Image


def main(directory):
    print('starting recursive scan from: {!r}'.format(directory))
    images = scan(directory)
    print('generating image fingerprints...')
    hash_db = hash_images(images)
    dupes = False
    print('detecting duplicate images...\n')
    for image_paths in hash_db.values():
        if len(image_paths) > 1:
            dupes = True
            print('duplicate images detected:')
            for path in sorted(image_paths):
                print(' * {}'.format(path))
            print('\n')
    if not dupes:
        print('no duplicate images detected')
    print('done')


def hash_images(images):
    """Calculate a wavelet hash for every image and group by matching hashes.

    Returns:
        Dictionary of hashes and matching image filenames.

    """
    hash_db = defaultdict(list)
    for image in images:
        hash_value = str(whash(image))
        hash_db[hash_value].append(image.filename)
    return hash_db


def scan(directory):
    """Walk a directory tree and yield images.

    Yields:
        Next image.

    """
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            try:
                image = Image.open(path)
            except IOError:
                continue  # skip files that are not images
            yield image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir',
                        nargs='?',
                        default=os.getcwd(),
                        help='start directory')
    args = parser.parse_args()
    main(args.dir)
