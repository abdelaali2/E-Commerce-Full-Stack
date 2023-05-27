import { Component, OnInit } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { ProductsService } from '../Services/productsServices/products.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss'],
})
export class ProductsComponent implements OnInit {
  productsList!: any[];
  product!: any;
  sessionid = this.cookieService.get('sessionid');
  constructor(
    private cookieService: CookieService,
    private productsService: ProductsService
  ) {}

  ngOnInit(): void {
    // get all products note: pagination settings are set by default
    this.productsService.getProducts().subscribe({
      next: (data) => {
        this.productsList = data;
        console.log('getProducts>>>', data);
      },
    });
    // get product by id
    this.productsService.getProduct(1).subscribe({
      next: (data) => {
        this.product = data;
        console.log('getProduct>>>', data);
      },
    });
    // update specific product
    this.productsService.putProduct(1).subscribe({
      next: (data) => {
        console.log('putProduct>>>', data);
      },
    });
    // create new product
    this.productsService.createProduct(this.product).subscribe({
      next: (response) => {
        console.log('Product created successfully:', response);
      },
      error: (error) => {
        console.error('Error creating product:', error);
      },
    });
    // delete product
    this.productsService.deleteProduct(55).subscribe({
      next: (response) => console.log('deleteProduct>>>', response),
      error: (error) => console.error('Error deleting product:', error),
    });
  }
}
