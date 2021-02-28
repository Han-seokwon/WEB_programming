from django.db import models

# Create your models here.

class Question(models.Model): # 테이블 컴럼
    # 클래스 변수들
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('data published')
    
    def __str__(self): # 객체를 문자열로 표현할 때 사용함
        # Admin 사이트에서 테이블명을 보여줄 때 필요함
        return self.question_text

class Choice(models.Model):
    # ForeignKey : 다대일 관계; on_delete : ForeignKey가 가르키는 대상이 사라질 때 어떻게 처리할지에 대한 옵션(SQL의 내용)
    # models.CASCADE SQL의 ON DELETE CASCADE 방식: 가르키는 대상이 삭제되면 같이 삭제됨; Question이 사라지면 Choice도 사라짐

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class NameList(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name