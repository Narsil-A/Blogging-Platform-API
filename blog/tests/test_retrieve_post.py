import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import Post

@pytest.mark.django_db
def test_retrieve_post():

    post = Post.objects.create(
        title="Test Post",
        content="This is a test post.",
        category="Testing",
        tags=["test", "read"]
    )

    client = APIClient()
    url = reverse('post-detail', args=[post.id])  

    response = client.get(url, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == post.id
    assert response.data['title'] == post.title
    assert response.data['content'] == post.content
    assert response.data['category'] == post.category
    assert response.data['tags'] == post.tags


@pytest.mark.django_db
def test_list_posts():

    Post.objects.create(
        title="Test Post 1",
        content="Content for post 1.",
        category="Category 1",
        tags=["tag1", "tag2"]
    )
    Post.objects.create(
        title="Test Post 2",
        content="Content for post 2.",
        category="Category 2",
        tags=["tag3", "tag4"]
    )

    client = APIClient()
    url = reverse('post-list-create') 

    response = client.get(url, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    titles = [post['title'] for post in response.data]
    assert "Test Post 1" in titles
    assert "Test Post 2" in titles
