export interface User {
  first_name: string;
  last_name: string;
  email: string;
  gender: String;
  username: string;
  password1: string;
  password2: string;
  is_dealer: boolean;
  profile_picture?: File;
}

export const newUser: User = {
  first_name: '',
  last_name: '',
  email: '',
  username: '',
  gender: '',
  password1: '',
  password2: '',
  is_dealer: false,
  profile_picture: undefined,
};

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

export interface updatedUserProfile {
  firstName?: string;
  lastName?: string;
  email?: string;
  username?: string;
  profile_picture?: File;
}
