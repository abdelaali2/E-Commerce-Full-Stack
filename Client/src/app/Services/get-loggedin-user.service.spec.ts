import { TestBed } from '@angular/core/testing';

import { GetLoggedinUserService } from './get-loggedin-user.service';

describe('GetLoggedinUserService', () => {
  let service: GetLoggedinUserService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetLoggedinUserService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
