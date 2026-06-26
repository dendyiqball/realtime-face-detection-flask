const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const faceCount = document.getElementById("faceCount");

const ctx = canvas.getContext("2d");

navigator.mediaDevices.getUserMedia({
    video: true
})
.then(stream => {
    video.srcObject = stream;
});

video.addEventListener("loadedmetadata", () => {

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

});

function drawMirrorVideo() {

    ctx.save();

    ctx.scale(-1, 1);

    ctx.drawImage(
        video,
        -canvas.width,
        0,
        canvas.width,
        canvas.height
    );

    ctx.restore();

}

video.addEventListener("play", () => {

    setInterval(async () => {

        try {

            ctx.clearRect(
                0,
                0,
                canvas.width,
                canvas.height
            );

            drawMirrorVideo();

            const imageData =
                canvas.toDataURL("image/jpeg");

            const response =
                await fetch("/detect", {

                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        image: imageData
                    })

                });

            const result =
                await response.json();

            ctx.clearRect(
                0,
                0,
                canvas.width,
                canvas.height
            );

            drawMirrorVideo();

            result.faces.forEach(face => {

                ctx.strokeStyle = "#00ff00";
                ctx.lineWidth = 3;

                ctx.strokeRect(
                    face.x,
                    face.y,
                    face.w,
                    face.h
                );

                ctx.fillStyle = "#00ff00";
                ctx.font = "bold 18px Arial";

                ctx.fillText(
                    face.direction,
                    face.x,
                    face.y - 10
                );

            });

            faceCount.innerHTML =
                `Wajah Terdeteksi: ${result.total_faces}`;

        }

        catch(err) {

            console.log(err);

        }

    }, 300);

});