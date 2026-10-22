import { Component, OnInit, OnDestroy, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { Subject, switchMap, takeUntil, of } from 'rxjs';

@Component({
  selector: 'app-course-details',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './course-details.component.html',
  styleUrls: ['./course-details.component.css']
})
export class CourseDetailsComponent implements OnInit, OnDestroy {

  course: any = null;
  loading = false;
  error = '';

  private destroy$ = new Subject<void>();

  constructor(
    private api: ApiService,
    private route: ActivatedRoute,
    private cdr: ChangeDetectorRef
  ) { }

  ngOnInit(): void {
    this.route.paramMap
      .pipe(
        takeUntil(this.destroy$),
        switchMap(params => {
          const slug = params.get('slug');

          if (!slug) {
            this.error = 'Δεν δόθηκε μάθημα.';
            this.loading = false;
            this.course = null;
            this.cdr.markForCheck();
            return of(null);
          }

          this.loading = true;
          this.error = '';
          this.course = null;
          this.cdr.markForCheck();

          return this.api.getCourse(slug);
        })
      )
      .subscribe({
        next: course => {
          this.course = course;
          this.loading = false;
          this.cdr.markForCheck();
        },
        error: err => {
          console.error('[Details] API error:', err);
          this.error = 'Το μάθημα δεν βρέθηκε ή υπάρχει πρόβλημα στον server.';
          this.loading = false;
          this.cdr.markForCheck();
        }
      });
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
