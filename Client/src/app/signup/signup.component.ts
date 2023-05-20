import { Component } from '@angular/core';
import { User } from '../Models/user';
import { SignupService } from '../Services/signup.service';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss'],
})
export class SignupComponent {
  constructor(
    private signupService: SignupService,
    private router: Router,
    private cookieService: CookieService
  ) {}

  user: User = {
    first_name: 'ibrahim',
    last_name: 'badr',
    email: 'ibrahim@email.com',
    username: 'ibrahim',
    password1: 'P@ssw0rd11',
    password2: 'P@ssw0rd11',
    is_dealer: false,
  };

  // TODO: handle password confirmation criteria.
  // TODO: handle username exists already error message.

  onSubmit() {
    if (this.user.password1 !== this.user.password2) {
      alert('Passwords do not match');
      return;
    }

    this.signupService
      .signup(this.user)
      ?.subscribe(({ sessionid, csrftoken }) => {
        this.cookieService.set('sessionid', sessionid);
        this.cookieService.set('csrftoken', csrftoken);
        this.router.navigate(['']);
      });
  }
}
