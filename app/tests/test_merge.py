from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)


def test_merge_videos():
    with open(
        os.path.join(os.path.dirname(__file__), "sample_video.mp4"), "rb"
    ) as video_file:
        response = client.post(
            "/upload",
            headers={"Authorization": "static-api-token"},
            files={"file": video_file},
        )
        video_id_1 = response.json()["video_id"]
        response = client.post(
            "/upload",
            headers={"Authorization": "static-api-token"},
            files={"file": video_file},
        )
        video_id_2 = response.json()["video_id"]

    video_ids = [video_id_1, video_id_2]
    response = client.post(
        "/merge",
        headers={"Authorization": "static-api-token"},
        json=video_ids,
    )
    assert response.status_code == 200
    assert "video_id" in response.json()


def test_merge_videos_invalid_ids():
    video_ids = ["invalid_id_1", "invalid_id_2"]
    response = client.post(
        "/merge",
        headers={"Authorization": "static-api-token"},
        json=video_ids,
    )
    assert response.status_code == 404
