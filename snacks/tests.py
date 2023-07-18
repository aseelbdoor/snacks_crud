from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse,reverse_lazy

class SnacksTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='random',
            email='random@random.com',
            password='random@12345'
        )
        self.snack = Snack.objects.create(
            title='test',
            purchaser=self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack), 'test')

    def test_detail_view(self):
        url = reverse('details', args=[self.snack.id])  
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'details.html')

    def test_create_view(self):
        url = reverse('create')
        data={
            "title": "test_2",
            "purchaser" : self.user.id,
            "description": "there is no description"
        }

        response = self.client.post(path=url,data = data,follow = True)
        self.assertTemplateUsed(response,'details.html')
        self.assertEqual(len(Snack.objects.all()),2)
        self.assertRedirects(response, reverse('details',args=[2]))
    

    def test_delete_view(self):
        url = reverse('delete',args=[self.snack.id])
        response = self.client.post(path=url,follow = True)
        self.assertTemplateUsed(response,'home.html')
        self.assertEqual(len(Snack.objects.all()),0)
        self.assertRedirects(response, reverse('home'))
        
        
    def test_update_view(self):
        url = reverse('update',args=[self.snack.id])
        data={
            "title": "test_2",
            "purchaser" : self.user.id,
            "description": "there is no description"
        }
        response = self.client.post(path=url,data = data,follow = True)
        self.assertTemplateUsed(response,'home.html')
        self.assertEqual(len(Snack.objects.all()),1)
        self.assertRedirects(response, reverse('home'))   
