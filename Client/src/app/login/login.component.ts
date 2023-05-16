import { Component } from '@angular/core';
import { LoginService } from '../Services/login.service';
import { Route, Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  csrfToken: string = '';
  loginError: boolean = false;

  constructor(
    private loginService: LoginService,
    private router: Router,
    private cookieService: CookieService
  ) {}

  onSubmit() {
    const user = { username: this.username, password: this.password };
    this.loginService.login(user).subscribe((cookie) => {
      document.cookie = `sessionid=${cookie}; expires=1.0 Day`;
      // this.router.navigate(['']);
      console.log(
        "this.cookieService.get('sessionid')",
        this.cookieService.get('sessionid')
      );
    });
  }
}
