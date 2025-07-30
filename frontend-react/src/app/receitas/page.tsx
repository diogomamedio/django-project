"use client";

import { useEffect, useState } from "react";
import {
  Title,
  Container,
  Image,
  Text,
  Loader,
  Center,
  SimpleGrid,
  Card,
  Button,
  Group,
  Select,
} from "@mantine/core";
import { notifications } from "@mantine/notifications";
import { IconArrowLeft, IconArrowRight } from "@tabler/icons-react";
import axios from "@/lib/axios";
import { Recipe, PaginatedResponse } from "@/types/recipe";

export default function RecipesPage() {
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [nextUrl, setNextUrl] = useState<string | null>(null);
  const [previousUrl, setPreviousUrl] = useState<string | null>(null);

  useEffect(() => {
    async function fetchRecipes(page: number = 1) {
      setLoading(true);
      try {
        const response = await axios.get<PaginatedResponse<Recipe>>(
          `/recipes/api/v2${page > 1 ? `?page=${page}` : ""}`
        );
        setRecipes(response.data.results);
        setNextUrl(response.data.next);
        setPreviousUrl(response.data.previous);
        setTotalPages(Math.ceil(response.data.count / 20)); // page_size = 20
        setLoading(false);
      } catch (error: any) {
        console.error(
          "Erro ao carregar receitas:",
          error.message,
          error.response?.data
        );
        notifications.show({
          title: "Erro",
          message: `Não foi possível carregar as receitas: ${error.message}`,
          color: "red",
        });
        setLoading(false);
      }
    }
    fetchRecipes(currentPage);
  }, [currentPage]);

  const handleNextPage = () => {
    if (nextUrl) {
      setCurrentPage((prev) => prev + 1);
    }
  };

  const handlePreviousPage = () => {
    if (previousUrl) {
      setCurrentPage((prev) => prev - 1);
    }
  };

  const handlePageChange = (value: string | null) => {
    if (value) {
      setCurrentPage(Number(value));
    }
  };

  if (loading) {
    return (
      <Container>
        <Center>
          <Loader size="lg" />
        </Center>
      </Container>
    );
  }

  return (
    <Container size="xl" py="xl">
      <Title order={1} ta="center" mb="xl">
        Lista de Receitas
      </Title>
      <SimpleGrid
        cols={{ base: 1, sm: 2, lg: 3 }}
        spacing="lg"
        verticalSpacing="lg"
      >
        {recipes.map((recipe) => (
          <Card key={recipe.id} shadow="md" padding="md" radius="md" withBorder>
            {recipe.cover && (
              <Card.Section>
                <Image
                  src={recipe.cover}
                  alt={recipe.title}
                  height={160}
                  fit="cover"
                />
              </Card.Section>
            )}
            <Text fw={700} size="lg" mt="md" lineClamp={1}>
              {recipe.title}
            </Text>
            <Text size="sm" c="dimmed" lineClamp={2} mt="xs">
              {recipe.description}
            </Text>
            <Group mt="sm" gap="xs">
              <Text size="sm">
                Tempo: {recipe.preparation_time} {recipe.preparation_time_unit}
              </Text>
              <Text size="sm">
                Porções: {recipe.servings} {recipe.servings_unit}
              </Text>
            </Group>
            {recipe.category && (
              <Text size="sm" mt="xs" c="blue">
                Categoria: {recipe.category.name}
              </Text>
            )}
          </Card>
        ))}
      </SimpleGrid>
      <Group justify="center" mt="xl">
        <Button
          leftSection={<IconArrowLeft size={16} />}
          disabled={!previousUrl}
          onClick={handlePreviousPage}
          variant="filled"
          color="blue"
        >
          Anterior
        </Button>
        <Select
          value={currentPage.toString()}
          onChange={handlePageChange}
          data={Array.from({ length: totalPages }, (_, i) => ({
            value: (i + 1).toString(),
            label: `Página ${i + 1}`,
          }))}
          w={120}
          placeholder="Selecione a página"
        />
        <Button
          rightSection={<IconArrowRight size={16} />}
          disabled={!nextUrl}
          onClick={handleNextPage}
          variant="filled"
          color="blue"
        >
          Próximo
        </Button>
      </Group>
    </Container>
  );
}
