import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UserProductsComponent } from './user-products.component';

describe('UserProductsComponent', () => {
  let component: UserProductsComponent;
  let fixture: ComponentFixture<UserProductsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UserProductsComponent]
    });
    fixture = TestBed.createComponent(UserProductsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
