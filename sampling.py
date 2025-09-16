import cv2
import json
import sys
import time

PATH = "./assets/video.mp4"
FPS = 30
W, H = 110, 30
OUTPUT = './sampling/badapple.json'

cap = cv2.VideoCapture(PATH)
if not cap.isOpened():
    raise RuntimeError("영상 파일을 열 수 없습니다.")

original_fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = max(1, round(original_fps / FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

frame_count = 0
saved_frames = 0
result = []

cell_width = max(1, 480 // W)
cell_height = max(1, 360 // H)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % frame_interval != 0:
        continue

    saved_frames += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_data = []

    ###
    for by in range(H):
        row_str = ""
        for bx in range(W):
            y0 = by * cell_height
            x0 = bx * cell_width
            block = gray[y0:y0+cell_height, x0:x0+cell_width]
            avg = block.mean()
            row_str += "▉" if avg > 120 else " "
        frame_data.append(row_str)

    # JSON BUILD
    result.append({
        "frame": frame_count,
        "value": frame_data
    })

    progress = frame_count / total_frames * 100
    sys.stdout.write(f"\r진행률: {progress:.2f}% ({frame_count}/{total_frames})")
    sys.stdout.flush()

    if saved_frames % 100 == 0:
        time.sleep(0.01)

cap.release()

# JSON SAVE
with open(OUTPUT, "w") as f:
    json.dump(result, f, indent=2)

print("JSON 파일 생성 완료:", OUTPUT)
