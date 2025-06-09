from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeViewTest(RecipeTestBase):
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

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

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

    def test_recipe_category_view_function_is_correct(self):
        # Uso o reverso para inserir o argumento category_id ao invés de hardcoded # noqa: E501
        view = resolve(reverse('recipes:category', kwargs={
            'category_id': 1000})
            )
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        # Teste de 404 quando não há recipes com o category_id especificado
        response = self.client.get(reverse(
            'recipes:category', kwargs={
                'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse(
            'recipes:recipe', kwargs={
                'id': recipe.category.id})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve('/recipes/1/')
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse(
            'recipes:recipe', kwargs={
                'id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a detail page - It loads one recipe'
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn(needed_title, content)

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse(
            'recipes:recipe', kwargs={
                'id': recipe.id})
        )
        self.assertEqual(response.status_code, 404)
