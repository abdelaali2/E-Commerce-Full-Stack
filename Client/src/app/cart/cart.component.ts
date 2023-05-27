import { Component, OnInit } from '@angular/core';
import { CartService } from '../Services/cartServices/cart.service';
import { CookieService } from 'ngx-cookie-service';
import { ICart } from '../Models/cart_models/cart.models';
import { ICartItem } from '../Models/cart_models/cartItem.models.';

@Component({
  selector: 'app-cart',
  template: `
    <h2>Your Carts</h2>
    <ul>
      {{
        cart
      }}
    </ul>
  `,
})
export class CartComponent implements OnInit {
  sessionId = this.cookieService.get('sessionid');
  cart!: ICart;
  cartList!: ICartItem[];
  putResult!: any;
  constructor(
    private cartService: CartService,
    private cookieService: CookieService
  ) {}

  ngOnInit() {
    // get the cart
    this.cartService.getUserCart(this.sessionId).subscribe({
      /*
      {id: 1, created_at: '2023-05-20T20:18:11.146736Z', updated_at: '2023-05-20T20:18:11.146736Z'}
    */
      next: (cart: ICart) => {
        this.cart = cart;
        console.log('getUserCart>>>', cart);
      },
      error: (error) => {
        console.log('Error:', error);
      },
    });
    // get associated cart items
    this.cartService.getCartItems(this.sessionId).subscribe({
      /* 
        [
      {
        "id": 2,
        "product": {
          "id": 2,
          "name": "IPhone 13",
          "price": "30000.00"
        },
        "quantity": 666
      }
    ]
      */
      next: (cartList: ICartItem[]) => {
        this.cartList = cartList;
        console.log('getCartItems>>', cartList);
      },
      error: (error) => {
        console.log('Error:', error);
      },
    });
    // update associated cart item
    this.cartService.putCartItem('2', this.sessionId, 666, 1).subscribe({
      // specify cart item id and product id
      next: (cart) => {
        this.putResult = cart;
        console.log('putCartItem>>', cart);
      },
    });
    // delete cart item from cart
    this.cartService.deleteCartItem('55', this.sessionId).subscribe({
      // each user has only one cart so we need to provide only cart item id and with session id the cart will be identified
      next: (cart) => console.log('deleteCartItem>>>', cart),
      error: (err) => console.log('error deleteCartItem', err),
    });
  }
}
