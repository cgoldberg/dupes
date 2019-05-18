# dupes

Corey Goldberg (2019)
License: MIT

 * https://github.com/cgoldberg/dupes

----

## Detect visually similar images.

`dupes.py` recursively scans a directory tree to find visually similar images.  It identifies similar images by comparing a wavelet hash of each.  A fingerprint is calculated using a perceptual hashing algorithm (wavelet hash) from the `ImageHash` library.  Images that hash to the same value are considered visually similar.  Paths to the suspected duplicate images are printed to the console.

#### Wavelet Hashing:
  * https://fullstackml.com/wavelet-image-hash-in-python-3504fdd282b5

#### Requirements:
  * Python3
  * ImageHash
    * `$ python3 -m pip install imagehash`
    * https://pypi.org/project/ImageHash/
    * Note: `ImageHash` package installation depends on: `numpy`, `Pillow`, `PyWavelets`, `scipy`, `six`

#### Usage:
  * `$ python3 dupes.py [dir]`
  * Note: if no directory is specified, scan starts from the current directory
