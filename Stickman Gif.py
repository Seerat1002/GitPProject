#Compilation of images to create a stickman dancing gif

import imageio.v3 as iio

filenames = ['Stickman1.jpg', 'Stickman2.jpg', 'Stickman3.jpg', 'Stickman4.jpg', 'Stickman5.jpg', 'Stickman6.jpg', 'Stickman7.jpg', 'Stickman8.jpg']
images = []

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('Stickmangif.gif', images, duration = 500, loop = 0)
