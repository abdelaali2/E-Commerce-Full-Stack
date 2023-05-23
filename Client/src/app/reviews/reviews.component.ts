import { Component, OnInit } from '@angular/core';
import { ReviewsService } from '../Services/reviewsServices/reviews.service';

@Component({
  selector: 'app-reviews',
  templateUrl: './reviews.component.html',
  styleUrls: ['./reviews.component.scss'],
})
export class ReviewsComponent implements OnInit {
  constructor(private reviewsService: ReviewsService) {}
  ngOnInit(): void {
    this.reviewsService.getReview(1).subscribe({
      next: (review) => console.log('getReview>>>', review),
      error: (error) => console.log('error getReview>>>', error),
    });
  }
}
