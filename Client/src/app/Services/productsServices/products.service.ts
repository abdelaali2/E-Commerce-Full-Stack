import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { EventEmitter, Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Observable } from 'rxjs';
import { httpOptions } from 'src/app/Models/http-options';
import { ProductListResponse } from 'src/app/Models/products_models/product.models';

@Injectable({
  providedIn: 'root',
})
export class ProductsService {
  productsURL = 'http://localhost:8000/products';
  modifiedProductsList = new EventEmitter();

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
    return this.httpClient.get(this.productsURL, {
      params,
    });
  }

  getProduct(id: number) {
    return this.httpClient.get<any>(`${this.productsURL}/${id}/`);
  }

  putProduct(id: number, data = {}) {
    return this.httpClient.put<any>(
      `${this.productsURL}/adjust/${id}/`,
      data,
      httpOptions
    );
  }

  createProduct(productData: any) {
    return this.httpClient.post(
      `${this.productsURL}/add/`,
      productData,
      httpOptions
    );
  }

  deleteProduct(id: number) {
    return this.httpClient.delete(
      `${this.productsURL}/adjust/${id}/`,
      httpOptions
    );
  }
}
