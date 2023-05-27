import { Component, OnInit } from '@angular/core';
import { CartService } from '../Services/cartServices/cart.service';
import { CookieService } from 'ngx-cookie-service';
import { ICart } from '../Models/cart_models/cart.models';
import { ICartItem } from '../Models/cart_models/cartItem.models.';
import { HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
})
export class CartComponent implements OnInit {
  // cart!: ICart;
  // cartList!: HttpResponse<ICartItem[]>;
  // putResult!: any;
  constructor(private cartService: CartService) {}

  ngOnInit() {
    // get the cart
    this.cartService.getUserCart().subscribe({
      /*
      {id: 1, created_at: '2023-05-20T20:18:11.146736Z', updated_at: '2023-05-20T20:18:11.146736Z'}
    */
      next: (cart: any) => {
        console.log('getUserCart>>>', cart);
      },
      error: (error) => {
        console.log('Error:', error);
      },
    });
    // get associated cart items
    this.cartService.getCartItems().subscribe({
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
      next: (cartList: HttpResponse<ICartItem[]>) => {
        console.log('getCartItems>>', cartList);
      },
      error: (error) => {
        console.log('Error:', error);
      },
    });
    // update associated cart item
    this.cartService.putCartItem(2).subscribe({
      // specify cart item id and product id
      next: (cart) => {
        console.log('putCartItem>>', cart);
      },
    });

    // add new cart item
    this.cartService.postCartItem().subscribe({
      next: (cart: any) => {
        console.log('postCartItem>>', cart);
      },
    });

    // delete cart item from cart
    this.cartService.deleteCartItem('55').subscribe({
      // each user has only one cart so we need to provide only cart item id and with session id the cart will be identified
      next: (cart: any) => console.log('deleteCartItem>>>', cart),
      error: (err: any) => console.log('error deleteCartItem', err),
    });
  }
}
