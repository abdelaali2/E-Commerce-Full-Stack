import { Component } from '@angular/core';
import { GetLoggedInUserService } from '../Services/get-logged-in-user.service';
import { UserProfile, newUserProfile } from '../Models/user';
import { map } from 'rxjs';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss'],
})
export class UserProfileComponent {
  constructor(private getUserService: GetLoggedInUserService) {}

  currentUser!: UserProfile;
  updatedUser!: UserProfile;
  loginFlag: boolean = false;
  showEditSection: boolean = true;

  // TODO: show the user profile after the user is logged in without hard refresh

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
}
