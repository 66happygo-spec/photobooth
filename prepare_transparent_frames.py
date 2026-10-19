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
        'bounds': (185, 1615, 175, 1145),
        'thresh': 220
    },
    {
        'key': 'frames/frame_festive_blessings.png',
        'src': 'frames/new_style2_festive.jpg',
        'name': '喜慶歡騰・新春紅韻吉祥',
        'bounds': (95, 1705, 195, 1105),
        'thresh': 220
    },
    {
        'key': 'frames/frame_golden_sunflower.png',
        'src': 'frames/new_style1_sunshine.jpg',
        'name': '冬日暖陽・金色向日葵活力',
        'bounds': (85, 1715, 195, 1120),
        'thresh': 220
    }
]

def make_frame_cutout(item):
    xmin, xmax, ymin, ymax = item['bounds']
    thresh = item['thresh']
    
    im = Image.open(item['src']).convert('RGB').resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    arr = np.array(im)
    h, w, _ = arr.shape
    
    # Create RGBA array with 100% opaque alpha by default
    rgba = np.zeros((h, w, 4), dtype=np.uint8)
    rgba[:, :, :3] = arr
    rgba[:, :, 3] = 255
    
    # Sub-region of inner central window
    sub_rgb = arr[ymin:ymax, xmin:xmax]
    is_white = (sub_rgb[:, :, 0] >= thresh) & (sub_rgb[:, :, 1] >= thresh) & (sub_rgb[:, :, 2] >= thresh)
    
    # Flood-fill from window center
    center_y = (ymax - ymin) // 2
    center_x = (xmax - xmin) // 2
    mask = is_white.astype(np.uint8) * 255
    flood_mask = np.zeros((mask.shape[0] + 2, mask.shape[1] + 2), dtype=np.uint8)
    flood_img = mask.copy()
    cv2.floodFill(flood_img, flood_mask, (center_x, center_y), 128)
    hole_connected = (flood_img == 128)
    
    # Set hole alpha to 0 (completely transparent)
    window_alpha = rgba[ymin:ymax, xmin:xmax, 3]
    window_alpha[hole_connected] = 0
    rgba[ymin:ymax, xmin:xmax, 3] = window_alpha
    
    # Save PNG
    out_im = Image.fromarray(rgba, 'RGBA')
    out_im.save(item['key'])
    
    ys, xs = np.where(rgba[:, :, 3] == 0)
    actual_xmin, actual_xmax = int(xs.min()), int(xs.max())
    actual_ymin, actual_ymax = int(ys.min()), int(ys.max())
    actual_w = actual_xmax - actual_xmin
    actual_h = actual_ymax - actual_ymin
    
    print(f"Saved {item['key']}:")
    print(f"  Hole: X=[{actual_xmin}, {actual_xmax}] (W={actual_w}), Y=[{actual_ymin}, {actual_ymax}] (H={actual_h})")
    print(f"  Ratios: rx={actual_xmin/TARGET_W:.4f}, rw={actual_w/TARGET_W:.4f}, ry={actual_ymin/TARGET_H:.4f}, rh={actual_h/TARGET_H:.4f}")

for item in inputs:
    make_frame_cutout(item)
