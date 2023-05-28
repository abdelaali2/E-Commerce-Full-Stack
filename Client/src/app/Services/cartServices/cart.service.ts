import { EventEmitter, Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ICart } from 'src/app/Models/cart_models/cart.models';
import {
  ICartItem,
  PutCartItem,
} from 'src/app/Models/cart_models/cartItem.models.';
import { httpOptions } from 'src/app/Models/http-options';

@Injectable({
  providedIn: 'root',
})
export class CartService {
  private apiURL = 'http://localhost:8000/cart/';
  modifiedCartItems = new EventEmitter();
  constructor(private http: HttpClient) {}

  getUserCart() {
    return this.http.get<ICart>(this.apiURL, httpOptions);
  }

  getCartItems() {
    return this.http.get<ICartItem[]>(this.apiURL + 'items/', httpOptions);
  }

  postCartItem(data: PutCartItem) {
    return this.http.post<PutCartItem>(
      this.apiURL + 'add-to-cart/',
      data,
      httpOptions
    );
  }

  putCartItem(cartItemId: number, data = {}) {
    return this.http.put<ICartItem[]>(
      this.apiURL + 'cart-item/' + `${cartItemId}/`,
      data,
      httpOptions
    );
  }
  deleteCartItem(cartItemId: string) {
    return this.http.delete<any>(
      this.apiURL + 'cart-item/' + `${cartItemId}/`,
      httpOptions
    );
  }
}
