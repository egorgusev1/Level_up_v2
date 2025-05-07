import re

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from app.managers import UserProfileManager

ARTICLE_STATUS = (
    ("draft","draft"),
    ("inprogress","in progress"),
    ("published","published"),
)

# -------------------------------
# Custom User Model
# -------------------------------
class UserProfile(AbstractUser):
    # Override the default username field with a unique email field
    email = models.EmailField(_("email address"),max_length=255,unique=True)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def article_count(self):
        return self.articles.count()
    
    @property
    def written_words(self):
        return self.articles.aggregate(models.Sum("word_count")) ["word_count__sum"] or 0
    
    # my_user.article_count

# -------------------------------
# Article Model
# -------------------------------
class Article(models.Model):
    title = models.CharField(_("title"),max_length=100)
    content = models.TextField(_("content"),blank=True, default="")
    word_count = models.IntegerField(_("word count"),blank = True, default="")
    twitter_post = models.TextField(_("twitter post"),blank=True,default="")
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=ARTICLE_STATUS,
        default="draft",
    )
    # Timestamps for creation and update
    created_at = models.DateTimeField(_("created at"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"),auto_now=True)
    # Reference to the user who created the article
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_("creator"), on_delete = models.CASCADE, related_name="articles")

    # -------------------------------
    # Overriding save() method
    # -------------------------------
    # This method calculates the word count of the content before saving.
    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*","",self.content).replace("&nbsp;","")
        self.word_count = len(re.findall(r"\b\w+\b",text))
        super().save(*args, **kwargs)



# Create your models here.
