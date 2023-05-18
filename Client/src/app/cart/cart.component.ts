import { Component, OnInit } from '@angular/core';
import { Cart } from '../models/cart.models';
import { CartService } from '../services/cart.service';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  providers: [CartService],
})
export class CartComponent {
  cartIdList!: Cart[];
  cart!: Cart;

  username!: string;
  password!: string;

  constructor(private authService: AuthService) {}

  onSubmit() {
    this.authService.login(this.username, this.password).subscribe((token) => {
      
      console.log('Here is the token: >> ', token);
      document.cookie = `token=${token}; expires=Thu, 01 Jan 2099 00:00:00 UTC; path=/;`;
    });
  }
}
