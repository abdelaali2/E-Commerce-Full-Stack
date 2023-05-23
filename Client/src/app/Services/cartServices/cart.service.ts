import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ICart } from 'src/app/Models/cart_models/cart.models';
import { ICartItem } from 'src/app/Models/cart_models/cartItem.models.';

@Injectable({
  providedIn: 'root',
})
export class CartService {
  private cartDetailsURL = 'http://localhost:8000/cart/';
  private cartItemsURL = 'http://localhost:8000/cart/items/';
  private modifyCartItemsURL = 'http://localhost:8000/cart/cart-item/'; // add id to it

  constructor(private http: HttpClient) {}

  getUserCart(sessionId: string): Observable<ICart> {
    const headers = new HttpHeaders({
      'X-SessionId': sessionId,
    });

    return this.http.get<ICart>(this.cartDetailsURL, { headers });
  }

  getCartItems(sessionId: string) {
    const headers = new HttpHeaders({
      'X-SessionId': sessionId,
    });

    return this.http.get<ICartItem[]>(this.cartItemsURL, { headers });
  }

  putCartItem(
    cartItemId: string,
    sessionId: string,
    quantity: number,
    productId: number
  ) {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'X-SessionId': sessionId,
    });
    const data = {
      product: productId,
      quantity: quantity,
    };
    return this.http.put<ICartItem[]>(
      this.modifyCartItemsURL + `${cartItemId}/`,
      data,
      {
        headers,
      }
    );
  }
  deleteCartItem(cartItemId: string, sessionId: string) {
    const headers = new HttpHeaders({
      'X-SessionId': sessionId,
    });

    return this.http.delete<any>(this.modifyCartItemsURL + `${cartItemId}/`, {
      headers,
    });
  }
}
