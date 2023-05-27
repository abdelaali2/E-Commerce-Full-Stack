import { Component, OnInit } from '@angular/core';
import { OrdersService } from '../Services/ordersServices/orders.service';

@Component({
  selector: 'app-orders',
  templateUrl: './orders.component.html',
  styleUrls: ['./orders.component.scss'],
})
export class OrdersComponent implements OnInit {
  constructor(private ordersService: OrdersService) {}
  ngOnInit(): void {
    this.ordersService.getOrders().subscribe({
      next: (order) => {
        console.log('getOrders >>> ', order);
      },
    });

    this.ordersService.editPayment(1).subscribe({
      next: (payment) => {
        console.log('editPayment >>> ', payment);
      },
    });

    this.ordersService.editShipment(2).subscribe({
      next: (shipment) => {
        console.log('editShipment >>> ', shipment);
      },
    });
  }
}
