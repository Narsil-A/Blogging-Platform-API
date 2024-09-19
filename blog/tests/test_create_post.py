import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import Post

@pytest.mark.django_db
def test_create_post():
    
    client = APIClient()
    url = reverse('post-list-create')
    data = {
        "title": "Test Post",
        "content": "This is a test post.",
        "category": "Testing",
        "tags": ["test", "api"]
    }
    response = client.post(url, data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED
    assert Post.objects.count() == 1
    post = Post.objects.first()
    assert post.title == "Test Post"
    print(post.title == "Test Post")
    assert post.content == "This is a test post."
    print(post.content == "This is a test post")
    assert post.category == "Testing"
    assert post.tags == ["test", "api"]
