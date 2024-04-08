# FrameExtractor

## Overview
FrameExtractor is a simple yet powerful tool for extracting frames from video files. It allows users to specify a start time, interval between frames, and a threshold for frame difference to filter out similar frames. This is particularly useful for creating datasets or for video analysis tasks.

## Installation
First, ensure you have Python installed on your system. Then, clone this repository and install the required dependencies by running:
```
pip install -r requirements.txt
```

## Usage
To use FrameExtractor, run:

```
python mp42png.py <video_file_path> <start_time_yyyymmddhhmmss> <interval_in_seconds>
```
- `video_file_path`: Path to the video file.
- `start_time_yyyymmddhhmmss`: Start time in `YYYYMMDDHHMMSS` format.
- `interval_in_seconds`: Interval between frames in seconds.

## Notes
- The tool creates an output directory named `./movie` to store the extracted frames.
- Ensure the video file path and start time are correctly specified to avoid errors.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---
# FrameExtractor

## 概要
FrameExtractorは、指定された間隔でビデオファイルからフレームを抽出するシンプルかつ強力なツールです。開始時間、フレーム間の間隔、そして似たフレームをフィルタリングするためのフレーム差分のしきい値をユーザーが指定できます。これは、データセットの作成やビデオ分析タスクに特に便利です。

## インストール
まず、システムにPythonがインストールされていることを確認してください。次に、このリポジトリをクローンし、次のコマンドを実行して必要な依存関係をインストールします：
```
pip install -r requirements.txt
```

## 使い方
FrameExtractorを使用するには、次のコマンドを実行します：
```
python mp42png.py <ビデオファイルパス> <開始時刻_YYYYMMDDHHMMSS> <秒単位の間隔>
```

- `ビデオファイルパス`：ビデオファイルへのパス。
- `開始時刻_YYYYMMDDHHMMSS`：`YYYYMMDDHHMMSS`形式の開始時刻。
- `秒単位の間隔`：フレーム間の間隔（秒）。

## 注意点
- このツールは、抽出されたフレームを保存するために`./movie`という名前の出力ディレクトリを作成します。
- ビデオファイルのパスと開始時刻が正しく指定されていることを確認してください。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています - 詳細についてはLICENSEファイルを参照してください。
