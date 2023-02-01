import requests
import json
import os

def get_manifest():
    try:
        if os.path.exists("manifest.json"):
            print("It's not necessary to download the manifest")
            create_folders_and_files()
        get_manifest_url = "https://piston-meta.mojang.com/v1/products/dungeons/f4c685912beb55eb2d5c9e0713fe1195164bba27/windows-x64.json"
        response = requests.get(get_manifest_url)

        manifest_url = response.json()['dungeons'][0]['manifest']['url']
        manifest = requests.get(str(manifest_url))
        write_manifest = open("manifest.json", "w")
        write_manifest.write(str(manifest.json()).replace("'", '"').replace("False", "false").replace("True", "true"))
    except Exception as error:
        print("Something went wrong: ", error)
def create_folders_and_files():
    try:
        print("Now it's time to create the files and folders!")
        manifest = open("manifest.json")
        data = json.load(manifest)
        for i in data["files"]:
            if not os.path.exists("Dungeons/" + i):
                if str(i).find(".") == -1:
                    print("Creating Folder", i)
                    os.mkdir("Dungeons/" + i)
                else:
                    print("Downloading files")
                    open("Dungeons/" + i, "a").close()
    except Exception as error:
        print("Something went wrong: ", error)
def download_assets():
    try:
        print("Now it's time to download the assets and files")
        manifest = open("manifest.json")
        data = json.load(manifest)
        for file_name, file_data in data['files'].items():
            if str(file_name).find(".") == -1:
                print("Skipping folder")
            else:
                for download_type, download_data in file_data['downloads'].items():
                    raw_url = file_data["downloads"]["raw"]["url"]
                    print(raw_url)
                    response = requests.get(raw_url)
                    with open("Dungeons/" + file_name, "wb") as file:
                        file.write(response.content)
    except Exception as error:
        print("Something went wrong: ", error)

get_manifest()
create_folders_and_files()
download_assets()
print("")