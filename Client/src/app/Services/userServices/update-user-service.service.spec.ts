import { TestBed } from '@angular/core/testing';

import { UpdateUserServiceService } from './update-user-service.service';

describe('UpdateUserServiceService', () => {
  let service: UpdateUserServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UpdateUserServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
