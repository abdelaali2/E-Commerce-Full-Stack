import { Component, OnInit } from '@angular/core';
// import { Cart } from '../models/cart.models';
// import { CartService } from '../services/cart.service';
import { LoginService } from '../Services/login.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  providers: [],
  // providers: [CartService],
})
export class CartComponent {
  // cartIdList!: Cart[];
  // cart!: Cart;

  username!: string;
  password!: string;

  constructor(private loginService: LoginService) {}

  onSubmit() {
    this.loginService
      .login({ username: this.username, password: this.password })
      .subscribe((token) => {
        console.log('Here is the token: >> ', token);
        document.cookie = `token=${token}; expires=Thu, 01 Jan 2099 00:00:00 UTC; path=/;`;
      });
  }
}
