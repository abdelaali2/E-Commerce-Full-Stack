import { TestBed } from '@angular/core/testing';

import { GetLoggedInUserService } from './get-logged-in-user.service';

describe('GetLoggedInUserService', () => {
  let service: GetLoggedInUserService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetLoggedInUserService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
