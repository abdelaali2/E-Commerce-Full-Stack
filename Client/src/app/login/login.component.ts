import { Component } from '@angular/core';
import { LoginService } from '../Services/login.service';
import { Router } from '@angular/router';
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
      this.cookieService.set('sessionid', cookie);
      this.router.navigate(['']);
    });
  }
}
