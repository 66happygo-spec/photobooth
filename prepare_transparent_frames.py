import cv2
import numpy as np
from PIL import Image

TARGET_W = 1800
TARGET_H = 1200

inputs = [
    {
        'key': 'frames/frame_macaron_balloons.png',
        'src': 'frames/new_style3_balloons.jpg',
        'name': '繽紛慶典・馬卡龍氣球彩帶',
        'threshold': 240
    },
    {
        'key': 'frames/frame_festive_blessings.png',
        'src': 'frames/new_style2_festive.jpg',
        'name': '喜慶歡騰・新春紅韻吉祥',
        'threshold': 240
    },
    {
        'key': 'frames/frame_golden_sunflower.png',
        'src': 'frames/new_style1_sunshine.jpg',
        'name': '冬日暖陽・金色向日葵活力',
        'threshold': 240
    }
]

results = {}

for item in inputs:
    # 1. Load and upscale to 1800 x 1200
    src_img = Image.open(item['src']).convert('RGBA')
    resized = src_img.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    arr = np.array(resized) # (1200, 1800, 4)

    # 2. Extract RGB
    rgb = arr[:, :, :3]
    # Check whiteness
    thresh = item['threshold']
    is_white = (rgb[:, :, 0] >= thresh) & (rgb[:, :, 1] >= thresh) & (rgb[:, :, 2] >= thresh)
    mask = is_white.astype(np.uint8) * 255

    # 3. Flood fill from center (900, 600) to find the contiguous cutout area
    h, w = mask.shape
    flood_mask = np.zeros((h + 2, w + 2), np.uint8)
    # cv2.floodFill fills connected component
    flood_img = mask.copy()
    cv2.floodFill(flood_img, flood_mask, (w // 2, h // 2), 128)
    hole_mask = (flood_img == 128)

    # Calculate bounding box of hole
    coords = np.argwhere(hole_mask)
    ymin, xmin = coords.min(axis=0)
    ymax, xmax = coords.max(axis=0)
    hole_w = xmax - xmin
    hole_h = ymax - ymin

    # 4. Set alpha to 0 for hole pixels
    arr[hole_mask, 3] = 0

    # Slight feathering on the 1-2 pixel border to prevent harsh stepping
    kernel = np.ones((3, 3), np.uint8)
    eroded_hole = cv2.erode(hole_mask.astype(np.uint8), kernel, iterations=1)
    edge_zone = (hole_mask.astype(np.uint8) - eroded_hole).astype(bool)
    # Blend alpha on edge
    arr[edge_zone, 3] = 120

    out_img = Image.fromarray(arr, 'RGBA')
    out_img.save(item['key'])
    print(f"Saved {item['key']}:")
    print(f"  Hole: X=[{xmin}, {xmax}] (W={hole_w}), Y=[{ymin}, {ymax}] (H={hole_h})")
    print(f"  Ratios: rx={xmin/TARGET_W:.4f}, rw={hole_w/TARGET_W:.4f}, ry={ymin/TARGET_H:.4f}, rh={hole_h/TARGET_H:.4f}")

    results[item['key']] = {
        'rx': round(xmin / TARGET_W, 4),
        'rw': round(hole_w / TARGET_W, 4),
        'ry': round(ymin / TARGET_H, 4),
        'rh': round(hole_h / TARGET_H, 4),
        'name': item['name']
    }

print("\nFinal Results Dictionary for index.html:")
import json
print(json.dumps(results, indent=2, ensure_ascii=False))
