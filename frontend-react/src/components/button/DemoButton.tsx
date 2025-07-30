// app/components/DemoButton.tsx
"use client";

import Link from "next/link";
import { Button } from "@mantine/core";

export function DemoButton() {
  return (
    <Link href="/hello">
      <Button>Ir para Hello</Button>
    </Link>
  );
}
