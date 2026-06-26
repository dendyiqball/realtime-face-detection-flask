from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

face_cascade = cv2.CascadeClassifier(
    "model/haarcascade_frontalface_default.xml"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():

    try:

        data = request.json["image"]

        encoded = data.split(",")[1]

        img_bytes = base64.b64decode(encoded)

        np_arr = np.frombuffer(
            img_bytes,
            np.uint8
        )

        img = cv2.imdecode(
            np_arr,
            cv2.IMREAD_COLOR
        )

        # MIRROR AGAR SAMA DENGAN SELFIE
        img = cv2.flip(img, 1)

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=6,
            minSize=(60, 60)
        )

        height, width = gray.shape

        center_x = width // 2
        center_y = height // 2

        result = []

        for (x, y, w, h) in faces:

            face_center_x = x + (w // 2)
            face_center_y = y + (h // 2)

            if face_center_x < center_x - 120:
                direction = "Posisi Kiri"

            elif face_center_x > center_x + 120:
                direction = "Posisi Kanan"

            elif face_center_y < center_y - 100:
                direction = "Posisi Atas"

            elif face_center_y > center_y + 100:
                direction = "Posisi Bawah"

            else:
                direction = "Posisi Tengah"

            result.append({
                "x": int(x),
                "y": int(y),
                "w": int(w),
                "h": int(h),
                "direction": direction
            })

        return jsonify({
            "status": "success",
            "total_faces": len(result),
            "faces": result
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )