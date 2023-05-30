export interface ICartItem {
  id: string;
  product: {
    id: number;
    name: string;
    price: string;
  };
  quantity: number;
}
export interface PutCartItem {
  product: number;
  quantity: number;
}
