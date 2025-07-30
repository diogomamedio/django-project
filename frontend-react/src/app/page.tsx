import { DemoButton } from "@/components/button/DemoButton";
import { UserCard } from "@/components/card/UserCard";

export default function HomePage() {
  return (
    <div>
      <h1>Página Inicial</h1>
      <UserCard />
      <hr />
      <DemoButton />
    </div>
  );
}
