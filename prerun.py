# download assets files to asset directory
# links:
# [INFO] #1.2 get: https://huggingface.co/2Noise/ChatTTS/resolve/main/asset/DVAE_full.pt
# [INFO] #1.5 get: https://huggingface.co/2Noise/ChatTTS/resolve/main/asset/Vocos.pt
# [INFO] #1.1 get: https://huggingface.co/2Noise/ChatTTS/resolve/main/asset/DVAE.pt
# [INFO] #1.3 get: https://huggingface.co/2Noise/ChatTTS/resolve/main/asset/Decoder.pt
# [INFO] #1.4 get: https://huggingface.co/2Noise/ChatTTS/resolve/main/asset/GPT.pt

import os
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

url_list = [
    "https://huggingface.co/2Noise/ChatTTS/resolve/main/asset/DVAE_full.pt",
    "https://huggingface.co/2Noise/ChatTTS/resolve/main/asset/Vocos.pt",
    "https://huggingface.co/2Noise/ChatTTS/resolve/main/asset/DVAE.pt",
    "https://huggingface.co/2Noise/ChatTTS/resolve/main/asset/Decoder.pt",
    "https://huggingface.co/2Noise/ChatTTS/resolve/main/asset/GPT.pt"
]
download_path = "./asset/"
proxy = "http://127.0.0.1:7890"

def download_asset() :
    if os.path.exists(download_path):
        print("Asset directory exists.")
        return 
    else:
        os.mkdir(download_path)
        print("Asset directory does not exist. Downloading assets...")
            # 使用线程池并发下载
        with ThreadPoolExecutor() as executor:
            # 提交所有下载任务到线程池
            futures = [executor.submit(download_file_with_progress, url , download_path + url.split('/')[-1]) for url in url_list]
            
            # 等待所有任务完成
            for future in futures:
                future.result()  # 如果有任何异常，会在这里抛出

def download_file_with_progress(url, local_filename):
    proxies = {
        'http': proxy,
        'https': proxy
    }
    # 发送 GET 请求并流式获取响应
    with requests.get(url, stream=True , proxies=proxies) as response:
        # 获取文件总大小（字节）
        total_size = int(response.headers.get('content-length', 0))
        
        # 打开本地文件进行写入（以二进制模式）
        with open(local_filename, 'wb') as file, tqdm(
            desc=local_filename,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as progress_bar:
            # 按块大小（比如 1024 字节）逐块下载文件
            for chunk in response.iter_content(chunk_size=1024):
                # 如果块不为空则写入文件
                if chunk:
                    file.write(chunk)
                    # 更新进度条
                    progress_bar.update(len(chunk))

