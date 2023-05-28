import { Component, OnInit } from '@angular/core';
import { CartService } from '../Services/cartServices/cart.service';
import { ICart } from '../Models/cart_models/cart.models';
import { ICartItem } from '../Models/cart_models/cartItem.models.';
import { HttpResponse } from '@angular/common/http';
import { OrdersService } from '../Services/ordersServices/orders.service';
import { ProductsService } from '../Services/productsServices/products.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
})
export class CartComponent implements OnInit {
  cart!: ICart;
  cartItemList!: ICartItem[];
  errorMessage!: string;
  // putResult!: any;
  constructor(
    private cartService: CartService,
    private ordersService: OrdersService,
    private productsService: ProductsService
  ) {}

  ngOnInit() {
    this.cartService.modifiedCartItems.subscribe((_) => {
      this.getCartItems();
    });
    this.getCart();
    this.getCartItems();

    // // update associated cart item
    // this.cartService.putCartItem(2).subscribe({
    //   // specify cart item id and product id
    //   next: (cart) => {
    //     console.log('putCartItem>>', cart);
    //   },
    // });
  }
  deleteCartItem(id: string) {
    // delete cart item from cart
    this.cartService.deleteCartItem(id).subscribe({
      // each user has only one cart so we need to provide only cart item id and with session id the cart will be identified
      next: (cart: any) => this.getCartItems(),
      error: (err: any) => console.log('error deleteCartItem', err),
    });
  }
  getCart() {
    // get the cart
    this.cartService.getUserCart().subscribe({
      /*
          {id: 1, created_at: '2023-05-20T20:18:11.146736Z', updated_at: '2023-05-20T20:18:11.146736Z'}
        */
      next: (cart: any) => {
        this.cart = cart;
      },
      error: (error) => {
        console.log('Error:', error);
      },
    });
  }

  getCartItems() {
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
      next: (cartList) => {
        this.cartItemList = cartList.body as ICartItem[];
        console.log('getCartItems>>', cartList);
      },
      error: (error) => {
        console.log('Error:', error);
      },
    });
  }

  // addCartItem() {
  //   // add new cart item
  //   this.cartService.postCartItem().subscribe({
  //     next: (cart: any) => {
  //       this.getCartItems();
  //     },
  //   });
  // }

  createOrder() {
    this.ordersService.createOrder().subscribe({
      next: (response) => {
        this.getCartItems();
        this.ordersService.orderModified.emit();
        this.productsService.modifiedProductsList.emit();
      },
      error: (error) => {
        this.errorMessage = error.error[0] as string;
      },
    });
  }
}
