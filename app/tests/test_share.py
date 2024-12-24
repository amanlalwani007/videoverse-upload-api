from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)


def test_share_video():
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
    assert response.status_code == 200
    assert "shared_link" in response.json()


def test_share_video_not_found():
    video_id = "test_id"
    response = client.post(
        f"/share/{video_id}",
        headers={"Authorization": "static-api-token"},
        params={"expiry_minutes": 1},
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Video not found"
