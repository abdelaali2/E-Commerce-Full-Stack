import { Component } from '@angular/core';
import { LoginService } from '../Services/login.service';
import { Route, Router } from '@angular/router';

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

  constructor(private loginService: LoginService, private router: Router) {}

  onSubmit() {
    const user = { username: this.username, password: this.password };
    this.loginService.login(user).subscribe({
      next: (response) => {
        if (response) {
          this.router.navigate(['']);
        }
      },
    });
  }
}
