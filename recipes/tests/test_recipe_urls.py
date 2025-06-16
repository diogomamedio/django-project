from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    # Testa se a url home de recipes está correta (apontando para /)
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        # print(f"resultado do reverse = {url}")
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        # Já que a url requer argumentos, vamos testar com um valor específico
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        # normalmente uso kwargs, mas aqui args so para exemplo
        url = reverse('recipes:recipe', args=(1,))
        self.assertEqual(url, '/recipes/1/')

    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')
