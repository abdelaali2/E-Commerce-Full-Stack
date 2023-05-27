import { NgModule } from '@angular/core';
import { UserComponent } from './user/user.component';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { UserOrdersComponent } from './user-orders/user-orders.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserReviewsComponent } from './user-reviews/user-reviews.component';
import { UserProductsComponent } from './user-products/user-products.component';

const profileChildren: Routes = [
  {
    path: '',
    redirectTo: 'my-orders',
    pathMatch: 'full',
  },
  {
    path: 'my-orders',
    component: UserOrdersComponent,
  },
  {
    path: 'my-reviews',
    component: UserReviewsComponent,
  },
  {
    path: 'my-products',
    component: UserProductsComponent,
  },
];

const userChildren: Routes = [
  {
    path: 'login',
    component: LoginComponent,
  },
  {
    path: 'signup',
    component: SignupComponent,
  },
  {
    path: 'my-profile',
    component: UserProfileComponent,
    children: profileChildren,
  },
];

const routes: Routes = [
  {
    path: 'user',
    component: UserComponent,
    children: userChildren,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
