export interface Category {
  id: number;
  name: string;
}

export interface Tag {
  id: number;
  name: string;
}

export interface Recipe {
  id: number;
  title: string;
  description: string;
  author: number;
  category: Category | null;
  tags: number[];
  public: boolean;
  preparation: string;
  tag_objects: Tag[];
  tag_links: string[];
  preparation_time: number;
  preparation_time_unit: string;
  servings: number;
  servings_unit: string;
  preparation_steps: string;
  cover: string;
}

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}
