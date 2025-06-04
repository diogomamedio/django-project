from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewTest(TestCase):
    # Testa se a url home de recipes está apontando para view correta
    def test_recipe_home_view_function_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        # Uso o reverso para inserir o argumento category_id ao invés de hardcoded # noqa: E501
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve('/recipes/1/')
        self.assertIs(view.func, views.recipe)
