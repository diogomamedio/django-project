from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
from unittest.mock import patch


class RecipeHomeViewTest(RecipeTestBase):
    # Testa se a url home de recipes está apontando para view correta
    def test_recipe_home_view_function_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200(self):
        # Captura a resposta da requisição
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        # Verifica se o template foi usado corretamente
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_if_no_recipes_exist(self):
        # Simula uma situação onde não há receitas no banco de dados
        response = self.client.get(reverse('recipes:home'))
        # transforma o conteúdo da resposta em string para facilitar a busca e depois verifica se existe um h1 com o texto "No recipes found" # noqa: E501
        self.assertIn(
            'No recipes found',  # Essa frase está no template
            response.content.decode('utf-8')
        )
        # Obs.: geralmente usamos uma frase constante que está em nosso template para verificar se a página foi carregada corretamente # noqa: E501

# Não é uma boa pratica fazer uma fixture como abaixo
    def test_recipe_home_template_loads_recipes(self):
        # Need a recipe for this test
        self.make_recipe()
        # Simula requisição GET para a página com os dados do meu DB temporário
        response = self.client.get(reverse('recipes:home'))
        # transformo o conteúdo da resposta em string para poder verificar
        # se a receita está presente na página
        content = response.content.decode('utf-8')
        # busco o que está no contexto da pagina
        response_context_recipes = response.context['recipes']
        # Verifico se a receita está presente na página, verificando o título
        self.assertIn('Recipe Title', content)
        # verifico se o numero de receitas é igual a 1 conforme meu contexto
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        # Check if one recipe exists
        self.assertIn(
            'No recipes found',
            response.content.decode('utf-8')
        )

    def test_recipe_home_is_paginated(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_recipe(**kwargs)

        with patch('recipes.views.PER_PAGE', new=3):
            response = self.client.get(reverse('recipes:home'))
            recipes = response.context['recipes']
            paginator = recipes.paginator

            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)