import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Cart } from '../models/cart.models';

@Injectable({
  providedIn: 'root',
})
export class CartService {
  private apiUrl = 'http://127.0.0.1:8000/carts/';

  constructor(private http: HttpClient) {}

  // get a list of related carts
  getCartsId(): Observable<Cart[]> {
    return this.http.get<Cart[]>(this.apiUrl);
  }

  // get the cart items
  getCartItems(cartId: number) {
    return this.http.get<Cart[]>(this.apiUrl + `/${cartId}/items`);
  }

  createCart(cart: Cart): Observable<Cart> {
    return this.http.post<Cart>(this.apiUrl, cart);
  }
}
