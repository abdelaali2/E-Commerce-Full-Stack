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

    // this.reviewsService.getReview(1).subscribe({
    //   next: (review) => console.log('getReview>>>', review),
    //   error: (error) => console.log('error getReview>>>', error),
    // });

    // this.reviewsService.getReviewsByUserId(1).subscribe({
    //   next: (reviews: any) => console.log('getReviewsByUserId>>>', reviews),
    //   error: (error: any) => console.log('error getReviewsByUserId>>>', error),
    // });

    // this.reviewsService.getReviewsByProductId(2).subscribe({
    //   next: (reviews: any) => console.log('getReviewsByProductId>>>', reviews),
    //   error: (error: any) =>
    //     console.log('error getReviewsByProductId>>>', error),
    // });

    // this.reviewsService.editReview(2).subscribe({
    //   next: (review) => console.log('editReview>>>', review),
    //   error: (error) => console.log('error editReview>>>', error),
    // });

    // this.reviewsService.deleteReview(5).subscribe({
    //   next: (review) => console.log('deleteReview>>>', review),
    //   error: (error) => console.log('error deleteReview>>>', error),
    // });

    // this.reviewsService.createReview().subscribe({
    //   next: (review) => console.log('createReview>>>', review),
    //   error: (error) => console.log('error createReview>>>', error),
    // });

  }
}
