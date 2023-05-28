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

export interface PaymentDetails {
  id: number;
  amount: number;
  currency: string;
  order_is_paid: boolean;
  payment_date: string | null;
}

export interface ShipmentDetails {
  carrier: string;
  is_delivered: boolean;
  actual_delivery_date: string | null;
  is_shipped: boolean;
  shipping_date: string | null;
  estimated_delivery_date: string;
}

export interface OrderItem {
  product: Product;
  quantity: number;
}

export interface OrderResponse {
  id: string;
  user: number;
  created_at: string;
  updated_at: string;
  order_items: OrderItem[];
  total_price: number;
  payment_details: PaymentDetails;
  shipment_details: ShipmentDetails;
}
