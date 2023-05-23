export interface ICartItem {
  id: number;
  product: {
    id: number;
    name: string;
    price: string;
  };
  quantity: number;
}
