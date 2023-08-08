# 11th-AWS-Back

- [gitignore 작성 도움 사이트](https://www.toptal.com/developers/gitignore)
- env.prod는 없기 때문에...나중에 따로 작성해주세요!

- [django secret key 생성기](https://miniwebtool.com/django-secret-key-generator/)

- [Docker Desktop 설치 - mac](https://docs.docker.com/desktop/mac/install/)
- [Docker Desktop 설치 - window](https://docs.docker.com/desktop/windows/install/)

- django의 버전은 3.0.8에서 작업해주세요
- 처음 설치할 때 django-environ, mysqlclient 설치 필요

- mysql에 직접 접속해서 database를 만들어 주어야 합니다!
- mysql -u root -p 입력 후 비밀번호 입력 -> create database {database 이름}
```
# .env

DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
DJANGO_SECRET_KEY={secretkey}

DATABASE_NAME={database 이름}
DATABASE_USER=root
DATABASE_PASSWORD={mysql 비밀번호}
DATABASE_HOST=localhost
DATABASE_PORT=3306
```


-----

### 오류

- **LF will be replaced by CRLF in config/docker/config/docker/entrypoint.prod.sh.**
- git config --global core.autocrlf true 입력
- **ALTER TABLE (테이블명) convert to charset utf8;** -> 참고로 docker-compose.yml의 계정으로 해야함.