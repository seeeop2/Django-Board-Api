from django.db import models


class Article(models.Model):
    # primary_key 없을 시, 자동으로 id 필드 생성

    # 게시글 ID (PK)
    article_id = models.AutoField(primary_key=True)
    # 게시글 제목
    subject = models.CharField(max_length=100)
    # 게시글 내용
    content = models.TextField()
    # 사용자 이름
    name = models.CharField(max_length=30)
    # 조회 수
    view_cnt = models.IntegerField(default=0)
    # 등록일
    reg_date = models.DateTimeField(auto_now_add=True)
