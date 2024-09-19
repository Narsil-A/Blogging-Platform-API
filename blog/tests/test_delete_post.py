import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import Post

@pytest.mark.django_db
def test_delete_post():
    
    post = Post.objects.create(
        title="Title to Delete",
        content="Content to delete.",
        category="Category to delete",
        tags=["delete", "test"]
    )

    client = APIClient()
    url = reverse('post-detail', args=[post.id])  

    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Post.objects.filter(id=post.id).count() == 0
