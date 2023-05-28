import { Component, OnInit } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { ProductsService } from '../Services/productsServices/products.service';
import {
  ProductListResponse,
  Product,
} from '../Models/products_models/product.models';
import { CartService } from '../Services/cartServices/cart.service';
import { PutCartItem } from '../Models/cart_models/cartItem.models.';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss'],
})
export class ProductsComponent implements OnInit {
  productsList!: any;
  product!: any;
  errorMessage = { id: '', error: '' };
  constructor(
    private cartService: CartService,
    private productsService: ProductsService
  ) {}

  ngOnInit(): void {
    // get all products note: pagination settings are set by default
    this.productsService.modifiedProductsList.subscribe((_) =>
      this.getProducts()
    );
    this.getProducts();

    // // get product by id
    // this.productsService.getProduct(1).subscribe({
    //   next: (data) => {
    //     this.product = data;
    //     console.log('getProduct>>>', data);
    //   },
    // });
    // // update specific product
    // this.productsService.putProduct(1).subscribe({
    //   next: (data) => {
    //     console.log('putProduct>>>', data);
    //   },
    // });
    // // create new product
    // this.productsService.createProduct(this.product).subscribe({
    //   next: (response) => {
    //     console.log('Product created successfully:', response);
    //   },
    //   error: (error) => {
    //     console.error('Error creating product:', error);
    //   },
    // });
    // // delete product
    // this.productsService.deleteProduct(55).subscribe({
    //   next: (response) => console.log('deleteProduct>>>', response),
    //   error: (error) => console.error('Error deleting product:', error),
    // });
  }

  getProducts() {
    this.productsService.getProducts().subscribe({
      next: (data: any) => {
        this.productsList = data;
      },
    });
  }

  addToCart(data: any) {
    this.cartService.postCartItem(data).subscribe({
      next: (_) => {
        this.cartService.modifiedCartItems.emit();
        this.errorMessage.error = '';
        this.errorMessage.id = '';
      },
      error: (error) => {
        this.errorMessage.error = error.error.error[0];
        this.errorMessage.id = error.error.id;
        console.log('********************************', this.errorMessage);
      },
    });
  }

  replaceSpacesWithUnderscores(categoryName: string): string {
    return categoryName.replace(/\s+/g, '_');
  }
}
