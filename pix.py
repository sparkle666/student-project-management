import pixabay.core

# init pixabay API
px = pixabay.core("13832130-119c011db028a4f8b19a396c9")

# search for space
space = px.query("house")


for x in range(10):
    space[x].download(f"hotel{x}.jpg", "largeImage")
    print("Downloaded success")