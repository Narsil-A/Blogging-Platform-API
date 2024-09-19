import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import Post

@pytest.mark.django_db
def test_update_post():

    post = Post.objects.create(
        title="Original Title",
        content="Original content.",
        category="Original Category",
        tags=["original", "test"]
    )

    client = APIClient()
    url = reverse('post-detail', args=[post.id])  

    updated_data = {
        "title": "Updated Title",
        "content": "Updated content.",
        "category": "Updated Category",
        "tags": ["updated", "test"]
    }
   
    response = client.put(url, updated_data, format='json')

    assert response.status_code == status.HTTP_200_OK
    post.refresh_from_db()
    assert post.title == updated_data['title']
    assert post.content == updated_data['content']
    assert post.category == updated_data['category']
    assert post.tags == updated_data['tags']
