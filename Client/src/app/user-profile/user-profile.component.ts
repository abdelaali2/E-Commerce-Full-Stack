import { Component } from '@angular/core';
import { GetLoggedInUserService } from '../Services/userServices/get-logged-in-user.service';
import {
  UserProfile,
  newUserProfile,
  updatedUserProfile,
} from '../Models/user';
import { map } from 'rxjs';
import { UpdateUserServiceService } from '../Services/userServices/update-user-service.service';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss'],
})
export class UserProfileComponent {
  constructor(
    private getUserService: GetLoggedInUserService,
    private updateUserService: UpdateUserServiceService
  ) {}

  currentUser!: UserProfile;
  updatedUser: updatedUserProfile = {};
  loginFlag: boolean = false;
  showEditSection: boolean = true;

  // TODO: show the user profile after the user is logged in without hard refresh
  // TODO: Email Confirmation.

  ngOnInit(): void {
    console.log('this.currentUser before subscribe', this.currentUser);
    this.getUserService.loggedInUser.subscribe((user) => {
      this.currentUser = user;
      console.log('this.currentUser inside subscribe', this.currentUser);
    });
    console.log('this.currentUser after subscribe', this.currentUser);
    this.getUserService.loginFlag.subscribe((flag) => {
      this.loginFlag = flag;
    });
  }

  toggleEdit() {
    this.showEditSection = !this.showEditSection;
  }

  onNewImageSelected(event: any) {
    this.updatedUser.profile_picture = event.target.files[0];
  }

  onSubmitChanges(event: any) {
    const { 0: firstName, 1: lastName, 2: email, 3: username } = event.target;

    if (firstName.value) {
      this.updatedUser.firstName = firstName.value;
    }
    if (lastName.value) {
      this.updatedUser.lastName = lastName.value;
    }
    if (username.value) {
      this.updatedUser.username = username.value;
    }
    if (email.value) {
      this.updatedUser.email = email.value;
    }

    this.updateUserService
      .updateUser(this.updatedUser)
      .subscribe((response) => {
        console.log('response', response);
      });
  }
}
