import requests
import time
import concurrent.futures

image_urls = [
    "https://images.unsplash.com/photo-1535850836387-0f9dfce30846",
    "https://images.unsplash.com/photo-1530903677198-7c9f3577a63e",
    "https://images.unsplash.com/photo-1518204919429-b447980c73bc",
    "https://images.unsplash.com/photo-1515096788709-a3cf4ce0a4a6",
    "https://images.unsplash.com/photo-1545147986-7ad5b0ea2caa",
]

start_time = time.time()


def download_image(image_url):
    image_bytes = requests.get(image_url).content
    image_name = image_url.split("-")[2]
    image_name = f"{image_name}.jpg"
    with open(image_name, 'wb') as image_file:
        image_file.write(image_bytes)
        print("{} was downloaded!".format(image_name))


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(download_image, image_urls)

print("Finished in {:.2f} secs".format(time.time() - start_time))
