import { Component } from '@angular/core';
import { User } from '../Models/user';
import { SignupService } from '../Services/signup.service';
import { Router } from '@angular/router';
import { GetLoggedInUserService } from '../Services/get-logged-in-user.service';

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

  user: User = {
    first_name: 'ibrahim',
    last_name: 'badr',
    email: 'ibrahim@email.com',
    username: 'ibrahim',
    password1: 'P@ssw0rd11',
    password2: 'P@ssw0rd11',
    is_dealer: false,
    profile_picture: undefined,
  };

  // TODO: handle password confirmation criteria.
  // TODO: handle username exists already error message.

  onSubmit() {
    if (this.user.password1 !== this.user.password2) {
      alert('Passwords do not match');
      return;
    }

    this.signupService.signup(this.user)?.subscribe(({ ok }) => {
      if (ok) {
        this.getLoggedInUserService.getUserProfile();
        this.router.navigate(['']);
      } else {
        // TODO: handle wrong login credentials before redirection.
        // TODO: enhance UI
        alert('Invalid username or password');
      }
    });
  }

  onFileSelected(event: any) {
    this.user.profile_picture = event.target.files[0];
    console.log('this.user.profile_picture', this.user.profile_picture);
  }
}
