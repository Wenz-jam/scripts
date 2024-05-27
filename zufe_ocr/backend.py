#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
from PIL import Image
import io
import pytesseract
import numpy as np
import re

app = Flask(__name__)
CORS(app)


def convert(_gif: str) -> str:
    image_data = base64.b64decode(_gif.split(',')[1])
    image = Image.open(io.BytesIO(image_data))
    combined_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
    alpha_value = int(255 / image.n_frames)
    for frame in range(image.n_frames):
        image.seek(frame)
        frame_image = image.convert('RGBA')
        assert image is not None
        assert frame_image is not None

        overlay = frame_image.copy()
        assert overlay is not None
        overlay.putalpha(alpha_value)

        combined_image = Image.alpha_composite(combined_image, overlay)

    combined_image_np = np.array(combined_image.convert('L'))
    kernel_size = 3
    kernel_radius = kernel_size // 2

    processed_image_np = np.zeros_like(combined_image_np)

    height, width = combined_image_np.shape

    # 遍历图像的每个像素点
    for y in range(height):
        for x in range(width):
            # 获取当前像素点的中心5*5范围内的像素值
            region = combined_image_np[max(0, y - kernel_radius): min(height, y + kernel_radius + 1),
                     max(0, x - kernel_radius): min(width, x + kernel_radius + 1)]
            # 计算中心5*5范围内接近白色的像素数量
            white_pixel_count = np.sum(region >= 200)

            # 如果超过50% 接近白色，则将当前像素点设置为白色
            if white_pixel_count / kernel_size ** 2 > 0.5:
                processed_image_np[y, x] = 255

    _text_cleaned = re.sub(r'[^0-9a*-zA-Z]', '', str(pytesseract.image_to_string(Image.fromarray(processed_image_np))))
    return _text_cleaned[0:4]


app = Flask(__name__)


@app.route('/recognize', methods=['POST'])
def recognize():
    try:
        # 获取请求中的图像数据
        data = request.json
        image_data = data['image']

        return jsonify({'text': convert(image_data)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='ocr.wenz-ubuntu', port=8503)
