# 11th-AWS-Back

### 오류 정리

- LF~~오류가 뜬다면?
    > git config --global core.autocrlf true 입력

- 한글 입력이 안된다면? 
    > db(docker) terminal에서 한글 설정하기

    > **ALTER TABLE (테이블명) convert to charset utf8;** (참고로 docker-compose.yml의 mysql계정으로 해야함.)

- mysql 명령어가 안된다면?
    > [해결사이트](https://realight.tistory.com/5)

- Github Actions가 실행이 안돼요!
    > deploy.yml파일에 push을 해줘도 가끔 git이 못알아먹어요...

    > Actions 탭에서 새로운 yml파일을 만들어줍시다.(안쓰는거)

- github Actions 오류
    > 오류가 너무 다양하지만...경험상 모듈끼리의 충돌이 원인인 경우가 많습니다! pip freeze > requirements.txt 를 한 후 backports.zoneinfo, mysqlclient는 주석처리후 다시 push 해주세요.

    > back~은 필요없고... mysqlclient는 어짜피 설치 명령어 작성해뒀어요.

- 배포 후 데이터베이스 생성이 안돼요~
    > ec2 서버에 접속 후 **sudo docker exec -it web python3 manage.py makemigrations**, **sudo docker exec -it web python3 manage.py migrate** 입력