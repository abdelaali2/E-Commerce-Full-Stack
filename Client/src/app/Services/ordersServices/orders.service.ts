import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { httpOptions } from 'src/app/Models/http-options';

@Injectable({
  providedIn: 'root',
})
export class OrdersService {
  private ordersURL = 'http://localhost:8000/orders/';
  private shipmentURL = 'http://localhost:8000/payments/edit/';
  private paymentURL = 'http://localhost:8000/shipments/edit/';

  constructor(private httpClient: HttpClient) {}

  getOrders() {
    return this.httpClient.get(this.ordersURL, httpOptions);
  }

  editShipment(id: number, data = {}) {
    return this.httpClient.put(this.shipmentURL + id + '/', data, httpOptions);
  }

  editPayment(id: number, data = {}) {
    return this.httpClient.put(this.paymentURL + id + '/', data, httpOptions);
  }
}
