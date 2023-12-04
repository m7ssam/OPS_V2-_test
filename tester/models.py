from audioop import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class T1(models.Model):
  id = models.AutoField(primary_key=True)
  a = models.CharField(max_length=10, blank=True, null=True)
  b = models.CharField(max_length=10, blank=True, null=True)
  c = models.CharField(max_length=10, blank=True, null=True)
  displayfields = ["a", "b", "c"]
  search_fields = ["a", "b", "c"]
  class Meta:
    ordering = ['id']
  def __str__(self):
      return str(self.a)
  
class T2(models.Model):
  id = models.AutoField(primary_key=True)
  d = models.CharField(max_length=10, blank=True, null=True)
  e = models.ForeignKey("T1", verbose_name=("e from T1"), on_delete=models.CASCADE)
  displayfields = ["d", "e"]
  search_fields = ["d", "e"]
  def __str__(self):
      return str(self.d)
  

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    displayfields =["title","content"]
    search_fields =[]
    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})

  



class ExampleModel(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=50)
    # Content of the blog post
    content = models.TextField()
    # Author of the blog post (using ForeignKey to link to the User model)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Publication date of the blog post
    pub_date = models.DateTimeField(auto_now_add=True)
    # Last modification date of the blog post
    last_modified = models.DateTimeField(auto_now=True)
    # Boolean field to indicate if the blog post is published
    is_published = models.BooleanField(default=False)
    displayfields = ["title","author"]
    search_fields = ["title","author"]
    def __str__(self):
        return self.title
    def get_short_content(self):
        # Return a short preview of the content (e.g., first 100 characters)
        return self.content[:100]
    class Meta:
        # Set the default ordering for the BlogPost model based on publication date
        ordering = ['-pub_date']
        # Define a verbose name for the model (used in the Django admin interface)
        verbose_name = 'Blog Post'
        # Define a verbose name plural for the model (used in the Django admin interface)
        verbose_name_plural = 'Blog Posts'
        # Define any unique constraints if needed (e.g., unique_together)
        unique_together = [['title', 'author']]
        # Specify permissions for the model (e.g., for custom user roles)
        permissions = [
            ('can_publish', 'Can publish blog posts'),
        ]
        # Add any additional index or constraints for database optimization
        indexes = [
            models.Index(fields=['title', 'pub_date']),
        ]

        """
        Explanation of the added attributes:
          verbose_name: A human-readable name for the model, used in the Django admin interface. In this case, it's set to 'Blog Post'.
          verbose_name_plural: A human-readable plural name for the model, used in the Django admin interface. It's set to 'Blog Posts'.
          unique_together: An example of how to define a unique constraint for the model. In this case, it's commented out, but you can uncomment and modify it as needed. It ensures that no two blog posts with the same title and author can exist.
          permissions: Define custom permissions for the model. In this example, a permission named 'can_publish' is added, which can be assigned to users or groups in the Django admin interface.
          indexes: Specify indexes for database optimization. In this example, an index is added for the 'title' and 'pub_date' fields.
        """



