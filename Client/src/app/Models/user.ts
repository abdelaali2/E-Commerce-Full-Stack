export interface User {
  first_name: string;
  last_name: string;
  email: string;
  username: string;
  password1: string;
  password2: string;
  is_dealer: boolean;
  profile_picture?: File;
}

export interface UserProfile {
  first_name: string;
  last_name: string;
  email: string;
  username: string;
  joined_at: string;
  is_dealer: boolean;
  profile_picture?: File;
}

export const newUserProfile: UserProfile = {
  first_name: '',
  last_name: '',
  email: '',
  username: '',
  joined_at: '',
  is_dealer: false,
  profile_picture: undefined,
};
