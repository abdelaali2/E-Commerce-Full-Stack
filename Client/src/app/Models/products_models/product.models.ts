export interface ProductCategory {
  id: number;
  name: string;
  description: string;
}

export interface Product {
  categories: ProductCategory[];
  name: string;
  description: string;
  quantity: number;
  id: number;
  dealer: number;
  dealer_name: string;
}

export interface ProductListResponse {
  links: {
    next: string | null;
    previous: string | null;
  };
  count: number;
  page_size: number;
  results: [
    {
      categories: ProductCategory[];
      name: string;
      description: string;
      quantity: number;
      id: number;
      dealer: number;
      dealer_name: string;
    }
  ];
}
