import os
import sys
sys.path.append(os.getcwd())
from speakerlab.process.processor import WavReader, SpkVeriAug
import torchaudio

aug=SpkVeriAug()

  
# 定义源目录和目标目录  
source_folder = 'VPR/data/test'  
# target_folder = 'VPR/data/test_pad3'
# reader=WavReader(duration=3)

# target_folder = 'VPR/data/test_pad2'
# reader=WavReader(duration=2)

target_folder = 'VPR/data/test_pad2_new'
reader=WavReader(duration=2)

target_folder = 'VPR/data/test_pad1_new'
reader=WavReader(duration=1)

# 遍历源目录  
for root, dirs, files in os.walk(source_folder):  
    for file in files:  
        if file.endswith('.wav'):  
            # 构建完整的文件路径  
            source_path = os.path.join(root, file)  
              
            # 加载音频文件  
            wav,speed_idx=reader(source_path)
            print(len(wav))
            print(speed_idx)
            # 翻倍音频长度  
            pad_audio = wav
              
            # 构建目标路径  
            target_path = os.path.join(target_folder, os.path.relpath(root, source_folder), file)  
              
            # 确保目标路径的文件夹存在  
            os.makedirs(os.path.dirname(target_path), exist_ok=True)  
              
            # 保存处理后的音频文件 
            torchaudio.save(target_path,wav.unsqueeze(0),sample_rate=16000)

            print(f"文件 {target_path} 已处理并保存。")  
