import requests
import time

image_urls = [
    "https://images.unsplash.com/photo-1515096788709-a3cf4ce0a4a6",
    "https://images.unsplash.com/photo-1589127939765-27aef18610f6",
    "https://images.unsplash.com/photo-1589044730942-a647d52d75be",
    "https://images.unsplash.com/photo-1570631810442-f20e700b0ce1",
    "https://images.unsplash.com/photo-1557842458-ab4b8925e3cb",
]

start_time = time.time()
counter = 1

for image_url in image_urls:
    image_bytes = requests.get(image_url).content
    image_name = "art_" + str(counter) + ".jpg"
    with open(image_name, 'wb') as image_file:
        image_file.write(image_bytes)
        print("{} was downloaded!".format(image_name))
    counter += 1

print("Finished in {:.2f} secs".format(time.time() - start_time))
