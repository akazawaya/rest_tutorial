# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
# **'auth.User' は「外部キーの“名前”ではなく、**Django の アプリ名＋モデル名 で既存モデルを参照する“モデル指定子”**
# 標準ユーザモデル＝django.contrib.auth アプリの User モデルを指している
# これはINSTALLED_APPS = ['django.contrib.auth']で呼ばれるやつだ
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language) # 使用するプログラミング言語の構文定義を取得
        linenos = 'table' if self.linenos else False # 行番号をつけるかどうか
        options = {'title': self.title} if self.title else {}  # タイトルがある場合はオプションに含める
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
