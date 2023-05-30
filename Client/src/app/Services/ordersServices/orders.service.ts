import { HttpClient, HttpResponse } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { httpOptions } from 'src/app/Models/http-options';
import { OrderResponse } from 'src/app/Models/orders_models/orders.models';

@Injectable({
  providedIn: 'root',
})
export class OrdersService {
  private ordersURL = 'http://localhost:8000/orders/';
  private shipmentURL = 'http://localhost:8000/payments/edit/';
  private paymentURL = 'http://localhost:8000/shipments/edit/';
  orderModified = new EventEmitter();
  constructor(private httpClient: HttpClient) {}

  getOrders(): Observable<HttpResponse<OrderResponse[]>> {
    return this.httpClient.get<OrderResponse[]>(this.ordersURL, httpOptions);
  }

  createOrder(): Observable<HttpResponse<OrderResponse>> {
 
    return this.httpClient.post<OrderResponse>(
      this.ordersURL + 'create/',
      {},
      httpOptions
    );
  }

  deleteOrder(id: string) {
    return this.httpClient.delete<OrderResponse>(
      this.ordersURL + 'delete/' + id + '/',
      httpOptions
    );
  }

  editShipment(id: number, data = {}) {
    return this.httpClient.put(this.shipmentURL + id + '/', data, httpOptions);
  }

  editPayment(id: number, data = {}) {
    return this.httpClient.put(this.paymentURL + id + '/', data, httpOptions);
  }
}
