# 比创频谱图像识别

## 项目简介
暂无

## 环境依赖
请确保您的环境中已安装Python 3.12或以上版本。

## 安装依赖
使用以下命令安装所需的Python包：
```bash
pip install -r requirements.txt
```

### 各文件功能简介
- `extract_blue.py` ：获取图像左上方（红线以上）的所有蓝色像素位置（未排序）。
- `extract_red.py` ：获取红线的位置。
- `extract.py` ：将pdf中的文本和图片提取出来。
- `peak.py` ：获取蓝色像素的尖峰位置。
- `rerank.py`：对csv文件进行先x后y的重排。
- `segment.py`：对从pdf文件获取的图片进行切割。
