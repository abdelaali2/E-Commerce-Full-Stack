// Modules
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
// import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

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
import { GetLoggedInUserService } from './Services/get-logged-in-user.service';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { CapitalizeFirstLetterPipe } from './Pipes/capitalize-first-letter';
import { UserOrdersComponent } from './user-orders/user-orders.component';
import { UserReviewsComponent } from './user-reviews/user-reviews.component';
import { UserProductsComponent } from './user-products/user-products.component';
import { ProductsService } from './Services/productsServices/products.service';
import { ReviewsService } from './Services/reviewsServices/reviews.service';

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
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ProductsComponent,
    ReviewsComponent,
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    // NgbModule,
  ],
  providers: [
    CookieService,
    GetLoggedInUserService,
    ProductsService,
    ReviewsService,
    { provide: HTTP_INTERCEPTORS, useClass: LoggingInterceptor, multi: true },
  ],
  bootstrap: [AppComponent, HeaderComponent],
})
export class AppModule {}
