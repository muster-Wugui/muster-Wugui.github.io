# CS180 (CS280A): Project 1 starter Python code

# these are just some suggested libraries
# instead of scikit-image you could use matplotlib and opencv to read, write, and display images

import numpy as np
import skimage as sk
import skimage.io as skio


def crop(im):
    dy = int(round(im.shape[0] * 0.2))
    dx = int(round(im.shape[1] * 0.2))
    return im[dy:im.shape[0] - dy, dx:im.shape[1] - dx]


def downsample(im):
    im = im[:im.shape[0] - im.shape[0] % 2, :im.shape[1] - im.shape[1] % 2]
    return (im[0::2, 0::2] + im[1::2, 0::2] + im[0::2, 1::2] + im[1::2, 1::2]) / 4.0


def edges(im):
    dy = im[1:, :-1] - im[:-1, :-1]
    dx = im[:-1, 1:] - im[:-1, :-1]
    return np.sqrt(dy ** 2 + dx ** 2)


def search(shift, base, center, radius):
    cropped_base = crop(base)
    best_score = None
    best_displacement = center
    for dy in range(center[0] - radius, center[0] + radius + 1):
        for dx in range(center[1] - radius, center[1] + radius + 1):
            cropped_shift = crop(np.roll(shift, (dy, dx), axis=(0, 1)))
            score = np.sum((cropped_shift - cropped_base) ** 2)
            if best_score is None or score < best_score:
                best_score = score
                best_displacement = (dy, dx)
    return best_displacement


def find_displacement(shift, base):
    if min(shift.shape) < 300:
        return search(edges(shift), edges(base), (0, 0), 15)
    dy, dx = find_displacement(downsample(shift), downsample(base))
    return search(edges(shift), edges(base), (2 * dy, 2 * dx), 2)


def align(shift, base):
    displacement = find_displacement(shift, base)
    return np.roll(shift, displacement, axis=(0, 1)), displacement


def colorize(imname, out_dir='img', show=False):
    # read in the image
    im = skio.imread('CS180_fa2026_proj1_data/' + imname)

    # convert to double (might want to do this later on to save memory)
    im = sk.img_as_float32(im)

    # compute the height of each part (just 1/3 of total)
    height = int(np.floor(im.shape[0] / 3.0))

    # separate color channels
    b = im[:height]
    g = im[height: 2*height]
    r = im[2*height: 3*height]

    # align the images
    # functions that might be useful for aligning the images include:
    # np.roll, np.sum, sk.transform.rescale (for multiscale)
    ag, dg = align(g, b)
    ar, dr = align(r, b)

    # create a color image
    im_out = np.dstack([ar, ag, b])

    # save the image
    fname = out_dir + '/' + imname.split('.')[0] + '.jpg'
    skio.imsave(fname, sk.img_as_ubyte(np.clip(im_out, 0.0, 1.0)))

    # display the image
    if show:
        skio.imshow(im_out)
        skio.show()

    return dg, dr, fname


# name of the input file
imname = 'cathedral.jpg'

colorize(imname)
