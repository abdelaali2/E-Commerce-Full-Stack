// Modules
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';

// Components
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { UserComponent } from './user/user.component';
import { ProductsComponent } from './products/products.component';
import { ReviewsComponent } from './reviews/reviews.component';
import { CartComponent } from './cart/cart.component';
// Services
import { CookieService } from 'ngx-cookie-service';
import { LoggingInterceptor } from './Interceptors/HttpInterceptor';
import { GetLoggedInUserService } from './Services/userServices/get-logged-in-user.service';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { CapitalizeFirstLetterPipe } from './Pipes/capitalize-first-letter';
import { UserOrdersComponent } from './user-orders/user-orders.component';
import { UserReviewsComponent } from './user-reviews/user-reviews.component';
import { UserProductsComponent } from './user-products/user-products.component';
import { ProductsService } from './Services/productsServices/products.service';
import { ReviewsService } from './Services/reviewsServices/reviews.service';
import { OrdersComponent } from './orders/orders.component';
import { OrdersService } from './Services/ordersServices/orders.service';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    LoginComponent,
    SignupComponent,
    UserComponent,
    CartComponent,
    UserProfileComponent,
    CapitalizeFirstLetterPipe,
    UserOrdersComponent,
    UserReviewsComponent,
    UserProductsComponent,
    ProductsComponent,
    ReviewsComponent,
    OrdersComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [
    CookieService,
    GetLoggedInUserService,
    ProductsService,
    ReviewsService,
    OrdersService,
    { provide: HTTP_INTERCEPTORS, useClass: LoggingInterceptor, multi: true },
  ],
  bootstrap: [AppComponent, HeaderComponent],
})
export class AppModule {}
