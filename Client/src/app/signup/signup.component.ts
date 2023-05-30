import { Component } from '@angular/core';
import { User, newUser } from '../Models/user';
import { SignupService } from '../Services/userServices/signup.service';
import { Router } from '@angular/router';
import { GetLoggedInUserService } from '../Services/userServices/get-logged-in-user.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss'],
})
export class SignupComponent {
  constructor(
    private signupService: SignupService,
    private router: Router,
    private getLoggedInUserService: GetLoggedInUserService
  ) {}

  // user: User = newUser;
  user: User = {
    first_name: 'ibrahim',
    last_name: 'badr',
    email: 'ibrahim@email.com',
    gender: 'Male',
    username: 'ibrahim',
    password1: 'P@ssw0rd11',
    password2: 'P@ssw0rd11',
    is_dealer: false,
    profile_picture: undefined,
  };

  passwordsMatchingFlag: boolean = true;
  responseError!: string;

  onSubmit() {
    if (this.user.password1 !== this.user.password2) {
      this.passwordsMatchingFlag = false;
      return;
    }

    this.signupService.signup(this.user)?.subscribe({
      next: () => {
        this.getLoggedInUserService.getUserProfile();
        this.router.navigate(['']);
      },
      error: (err) => {
        this.responseError = err.error.errors.username[0];
        console.log(
          'err.error.errors.username[0]',
          err.error.errors.username[0]
        );
      },
    });
  }

  // TODO: handle username exists already error message.
  // TODO: handle wrong login credentials before redirection.
  // TODO: enhance UI(Loading screen).

  onFileSelected(event: any) {
    this.user.profile_picture = event.target.files[0];
    console.log('this.user.profile_picture', this.user.profile_picture);
  }
}
