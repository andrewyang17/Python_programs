import requests
import time
import concurrent.futures

image_urls = [
    "https://images.unsplash.com/photo-1556893334-894d61486a9d",
    "https://images.unsplash.com/photo-1556113275-62dd94fd0578",
    "https://images.unsplash.com/photo-1555616200-465ffa134781",
    "https://images.unsplash.com/photo-1554752698-448c3453bd30",
    "https://images.unsplash.com/photo-1540845692348-b9d2bc813a63",
]

start_time = time.time()


def download_image(image_url):
    image_bytes = requests.get(image_url).content
    image_name = image_url.split("-")[2]
    image_name = f"{image_name}.jpg"
    with open(image_name, 'wb') as image_file:
        image_file.write(image_bytes)
        print("{} was downloaded!".format(image_name))


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, image_urls)

print("Finished in {:.2f} secs".format(time.time() - start_time))
