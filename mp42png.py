import cv2
import numpy as np
import os
import sys
from datetime import datetime, timedelta

def extract_frames(video_path, start_time_str, interval_sec, threshold=0.5, sample_size=(10, 10)):
    # 動画を読み込む
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("動画ファイルを開けませんでした。")
        return

    # フレームレートを取得
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps

    # 出力ディレクトリを作成
    output_dir = "./movie"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 時刻をパース
    start_time = datetime.strptime(start_time_str, "%Y%m%d%H%M%S")

    # 初期フレームの処理
    success, prev_frame = cap.read()
    if success:
        prev_frame_small = cv2.resize(prev_frame, sample_size)
        cv2.imwrite(f"{output_dir}/{start_time_str}.png", prev_frame)
    else:
        print("最初のフレームを読み込めませんでした。")
        return

    # 指定された間隔でフレームを処理
    current_time = 0
    while success and current_time <= duration:
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(fps * interval_sec * (current_time // interval_sec + 1)))
        success, frame = cap.read()
        if success:
            frame_small = cv2.resize(frame, sample_size)
            # 差分を計算
            diff = np.sum(frame_small != prev_frame_small) / (sample_size[0] * sample_size[1] * 3)
            if diff >= threshold:
                timestamp = (start_time + timedelta(seconds=int(interval_sec * (current_time // interval_sec + 1)))).strftime("%Y%m%d-%H%M%S")
                cv2.imwrite(f"{output_dir}/{timestamp}.png", frame)
                prev_frame_small = frame_small
        current_time += interval_sec

    cap.release()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("使用法: python mp42png.py moviefile.mp4 yyyymmddhhmmss interval_sec")
    else:
        video_file = sys.argv[1]
        start_time_str = sys.argv[2]
        interval_sec = int(sys.argv[3])
        extract_frames(video_file, start_time_str, interval_sec)
      
