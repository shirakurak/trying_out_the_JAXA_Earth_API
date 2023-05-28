# Load module
from jaxa.earth import je

import matplotlib.pyplot as plt

# Get an image
data = je.ImageCollection(ssl_verify=True)\
  .filter_date()\
    .filter_resolution()\
      .filter_bounds()\
        .select()\
          .get_images()

# Process and show an image
img = je.ImageProcess(data)\
  .show_images()

plt.imshow(img.raster.img[0])
plt.show()
