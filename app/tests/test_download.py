from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)


def test_download_video():
    with open(
        os.path.join(os.path.dirname(__file__), "sample_video.mp4"), "rb"
    ) as video_file:
        response = client.post(
            "/upload",
            headers={"Authorization": "static-api-token"},
            files={"file": video_file},
        )
        video_id = response.json()["video_id"]
        response = client.post(
            f"/share/{video_id}",
            headers={"Authorization": "static-api-token"},
            params={"expiry_minutes": 1},
        )
        shared_link_id = response.json()["shared_link"].split("/")[-1]
    response = client.get(
        f"/download/{shared_link_id}", headers={"Authorization": "static-api-token"}
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "video/mp4"


def test_download_video_not_exist():
    shared_link_id = "expired_shared_link_id"
    response = client.get(
        f"/download/{shared_link_id}", headers={"Authorization": "static-api-token"}
    )
    assert response.status_code == 404
