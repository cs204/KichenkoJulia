n=input("File name: ")
v=n.split(".")
index=v[-1]

correkt_types=["gif","jpg","jpeg","png","pdf","txt","zip"]

if index == "jpg":
    index = "jpeg"
if index in correkt_types:
    if index == "gif" or index == "jpg" or index == "jpeg" or index == "png":

        print (f"image/{index}")
    elif index == "txt":

        print(f"image/{index}")
    elif index == "zip" or index == "pdf":

        print(f"application/{index}")
else:
    print("application/oktet-stream")
