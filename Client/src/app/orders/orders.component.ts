import { Component, OnInit, SimpleChanges } from '@angular/core';
import { OrdersService } from '../Services/ordersServices/orders.service';
import { OrderResponse } from '../Models/orders_models/orders.models';
import { Subscription } from 'rxjs';
import { CartService } from '../Services/cartServices/cart.service';

@Component({
  selector: 'app-orders',
  templateUrl: './orders.component.html',
  styleUrls: ['./orders.component.scss'],
})
export class OrdersComponent implements OnInit {
  ordersList!: OrderResponse[];
  errorMessage!: string;

  constructor(
    private ordersService: OrdersService,
    private cartService: CartService
  ) {}

  ngOnInit(): void {
    this.ordersService.orderModified.subscribe((_) => this.getOrders());
    this.getOrders();
  }

  getOrders() {
    this.ordersService.getOrders().subscribe({
      next: (order) => {
        this.ordersList = order.body as OrderResponse[];
      },
      error: (err) => {
        console.log(err.error[0]);
        this.ordersList = [];
      },
    });
  }

  deleteOrder(id: string) {
    this.ordersService.deleteOrder(id).subscribe({
      next: (response) => {
        this.getOrders();
      },
    });
  }
}
