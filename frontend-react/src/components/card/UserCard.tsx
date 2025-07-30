// app/components/UserCard.tsx
"use client";

import { Card, Text, Button } from "@mantine/core";

export function UserCard() {
  return (
    <Card shadow="sm" padding="lg" radius="md" withBorder>
      <Text size="lg" fw={500}>
        Diogo Mamédio
      </Text>
      <Text size="sm" c="dimmed" mt="xs">
        Desenvolvedor Full Stack apaixonado por boas práticas.
      </Text>
      <Button variant="light" color="blue" fullWidth mt="md">
        Ver perfil
      </Button>
    </Card>
  );
}
