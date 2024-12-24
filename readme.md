```
Video upload Service have below functionalities
1. upload
2. trim
3. merge
4. share
5. Download
```


```Setup on local 
1. Without docker 
 a. Create virtaul environment 
    python -m venv venv
    pip install -r requirements.txt
 b. uncomment load dotenv in main.py 
 c. run command python app/main.py
```
```
2. With  docker 
 a. docker-compose build .
 b. docker-compose up 
```

```
Testing API (Go to swagger docs and execute them)
https://localhost:8000/docs
```

```
Upload Api
Endpoint :- POST
URL:- http://localhost:8000/upload/
```
Case 1 :- upload valid video

![Local Image](readme-tests/upload_video_valid.png)

Case 2 :- Upload Video invalid > 25MB
![Local Image](readme-tests/upload_video>25MB.png)

Case 3:- Upload video which are not in defined duration 

![Local Image](readme-tests/upload_video_invalid_duration.png)

```
Trim API 
Endpoint :- http://localhost:8000/trim/{video-id}
Method:-  POST 
```
Case 1 :- Trim non existing video 
![Local Image](readme-tests/trim_non_existent_video.png)

Case 2 :- Trim existing video

![Local Image](readme-tests/trim_existing_video.png)


```
Merge API 
Endpoint :- http://localhost:8000/merge
Method:-  POST 
```
Case 1 :- Merge Video request with invalid videoid

![Local Image](readme-tests/merge_request_invalid_videoid.png)

Case 2 :- Merge Video with valid video id
![Local Image](readme-tests/merge_request_valid_videoid.png)



```
Share API 
Endpoint :- http://localhost:8000/share/{video-id}
Method:-  POST 
```
Case 1:- Share api with invalid videoid

![Local Image](readme-tests/share_api_invalid_videoid.png)

Case 2:- Share api with valid videoid

![Local Image](readme-tests/share_api_valid_videoid.png)

```
Download API 
Endpoint :- http://localhost:8000/download/{link-id}
Method:-  POST 
```
Case 1 :- Link is expired


![Local Image](readme-tests/download_video_link_expired.png)

Case 2 :- Link is valid

![Local Image](readme-tests/download_video_valid_link.png)

```
Run Unit test cases
Command : pytest --cov=app --cov-report=term-missing
Attach Report below 
```

![Local Image](readme-tests/unit_test_case_coverage.png)
