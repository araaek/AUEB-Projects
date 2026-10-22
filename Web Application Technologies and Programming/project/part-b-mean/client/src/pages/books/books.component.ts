import { Component, OnInit, OnDestroy, ChangeDetectionStrategy, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api.service';
import { Subject, takeUntil, catchError, of } from 'rxjs';

@Component({
  selector: 'app-books',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class BooksComponent implements OnInit, OnDestroy {
  groupedBooks: { courseTitle: string; books: any[] }[] = [];
  loading = false;
  error = '';

  private destroy$ = new Subject<void>();

  constructor(private api: ApiService, private cdr: ChangeDetectorRef) { }

  ngOnInit(): void {
    this.loading = true;
    this.error = '';

    this.api
      .getCourses()
      .pipe(
        takeUntil(this.destroy$),
        catchError(err => {
          console.error('Books API error:', err);
          this.error = 'Πρόβλημα κατά τη φόρτωση βιβλίων.';
          this.loading = false;
          this.cdr.markForCheck();
          return of([]);
        })
      )
      .subscribe(courses => {
        // Πάρε μόνο τα μαθήματα που έχουν books
        const result: { courseTitle: string; books: any[] }[] = [];

        for (const course of courses || []) {
          if (course.books && course.books.length) {
            result.push({
              courseTitle: course.title,
              books: course.books
            });
          }
        }

        this.groupedBooks = result;
        this.loading = false;
        this.cdr.markForCheck();
      });
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
