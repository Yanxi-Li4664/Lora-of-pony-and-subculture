import os
import urllib.request
from tqdm import tqdm  # For progress bar

def download_file(url, save_path):
    try:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Download the file and show progress
        with urllib.request.urlopen(url) as response, open(save_path, 'wb') as out_file:
            file_size = int(response.info().get('Content-Length', 0))
            chunk_size = 1024  # Adjust as needed
            with tqdm(total=file_size, unit='B', unit_scale=True, desc="Downloading") as pbar:
                while True:
                    data = response.read(chunk_size)
                    if not data:
                        break
                    out_file.write(data)
                    pbar.update(len(data))

        print("Download complete! File saved at:", save_path)
    except Exception as e:
        print("Error:", str(e))

# URL to download
url = "https://srba.ac.cn/somedata/srba-v2-r4.6.safetensors"

# Save path (change this to your desired folder and filename)
save_path = r"C:\lora\srba-v2-r4.6.safetensors"

download_file(url, save_path)

# Add a prompt to exit after download
input("Press any key to exit.")
