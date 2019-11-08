from google_images_download import google_images_download

# =============================================================================
# make sure to 
# * pip install google_images_download *
# before you proceeeeeeeed
# =============================================================================

# =============================================================================
# Enter your search keyword in the place of Racoon,Rabbit
# =============================================================================

response = google_images_download.googleimagesdownload()
arguments = {"keywords":"Racoon,Rabbit","limit":60,"print_urls":False}
paths = response.download(arguments)
print(paths)


# =============================================================================
# creates a downloads folder in the cwd (current working directory) and 
# all your downloaded images will be stored there in a folder matching the keyword
# =============================================================================
