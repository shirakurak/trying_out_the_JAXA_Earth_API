# Load module
from jaxa.earth import je

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
