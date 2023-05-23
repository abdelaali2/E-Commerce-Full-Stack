import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';

@Injectable({
  providedIn: 'root',
})
export class ProductsService {
  productsURL = 'http://localhost:8000/products';
  headers = new HttpHeaders({
    'X-SessionId': this.cookieService.get('sessionid'),
  });
  
  constructor(
    private httpClient: HttpClient,
    private cookieService: CookieService
  ) {}

  getProducts(sortBy: string = '-id', page = 1, pageSize = 50) {
    const params = {
      page: page,
      page_size: pageSize,
      sort_by: sortBy,
    };
    return this.httpClient.get<any[]>(this.productsURL, { params });
  }

  getProduct(id: number) {
    return this.httpClient.get<any>(`${this.productsURL}/${id}/`);
  }

  putProduct(id: number) {
    return this.httpClient.put<any>(
      `${this.productsURL}/${id}/`,
      {},
      { headers: this.headers }
    );
  }

  createProduct(productData: any) {
    return this.httpClient.post(`${this.productsURL}/add/`, productData, {
      headers: this.headers,
    });
  }

  deleteProduct(id: number) {
    return this.httpClient.delete(`${this.productsURL}/${id}/`, {
      headers: this.headers,
    });
  }
}
