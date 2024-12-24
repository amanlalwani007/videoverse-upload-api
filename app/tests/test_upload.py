from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)


def test_upload_video():
    with open(
        os.path.join(os.path.dirname(__file__), "sample_video.mp4"), "rb"
    ) as video_file:
        response = client.post(
            "/upload",
            headers={"Authorization": "static-api-token"},
            files={"file": video_file},
        )
    assert response.status_code == 200
    assert "video_id" in response.json()
