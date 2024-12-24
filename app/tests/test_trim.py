from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)


def test_trim_video():
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
        f"/trim/{video_id}",
        headers={"Authorization": "static-api-token"},
        params={"start_time": 5, "end_time": 10},
    )
    assert response.status_code == 200
    assert "video_id" in response.json()
    assert "Video trimmed successfully" in response.json()["message"]


def test_trim_video_not_found():
    video_id = "non_existent_video_id"
    response = client.post(
        f"/trim/{video_id}",
        headers={"Authorization": "static-api-token"},
        params={"start_time": 5, "end_time": 10},
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Video not found"
