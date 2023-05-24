export interface User {
  first_name: string;
  last_name: string;
  email: string;
  username: string;
  password1: string;
  password2: string;
  is_dealer: boolean;
  photo?: File;
}

export interface UserProfile {
  first_name: string;
  last_name: string;
  email: string;
  username: string;
  is_dealer: boolean;
  photo?: File;
}

export const newUserProfile: UserProfile = {
  first_name: '',
  last_name: '',
  email: '',
  username: '',
  is_dealer: false,
};
