from django.db import models

class VisitLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    page_visited = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.page_visited} - {self.timestamp}"