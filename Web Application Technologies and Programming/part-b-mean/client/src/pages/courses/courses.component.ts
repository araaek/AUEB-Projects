import {
  Component,
  OnInit,
  OnDestroy,
  ChangeDetectorRef,
  ChangeDetectionStrategy
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { Subject, takeUntil, catchError, of } from 'rxjs';

@Component({
  selector: 'app-courses',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class CoursesComponent implements OnInit, OnDestroy {
  // Όλα τα μαθήματα από το API
  courses: any[] = [];
  // ΜΟΝΟ τα φιλτραρισμένα
  filteredCourses: any[] = [];

  // Τρέχουσα κατάσταση (για debug / URL)
  currentCategory = '';
  currentLevel = '';

  loading = false;
  error = '';

  // Τιμές dropdowns – αρχικά Όλες / Όλα
  selectedCategory: string = '';
  selectedLevel: string = '';

  private destroy$ = new Subject<void>();

  constructor(
    private api: ApiService,
    private route: ActivatedRoute,
    private router: Router,
    private cdr: ChangeDetectorRef
  ) { }

  ngOnInit(): void {
    this.route.queryParams
      .pipe(takeUntil(this.destroy$))
      .subscribe(params => {
        // Sync URL → filters
        this.selectedCategory = params['category'] || '';
        this.selectedLevel = params['level'] || '';

        this.currentCategory = this.selectedCategory;
        this.currentLevel = this.selectedLevel;

        console.log('[Courses] params:', {
          category: this.selectedCategory || '(all)',
          level: this.selectedLevel || '(all)'
        });

        this.loadCourses(); // refresh λίστας
      });
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }

  // Φέρνει όλα τα courses (ή from server-side filter αν θέλεις)
  loadCourses(): void {
    this.loading = true;
    this.error = '';
    this.courses = [];

    this.api
      .getCourses({}) // ⬅ εδώ μπορείς να περάσεις server-side φίλτρα αν θελήσεις
      .pipe(
        takeUntil(this.destroy$),
        catchError(err => {
          console.error('[Courses] API error:', err);
          this.error = 'Σφάλμα φόρτωσης μαθημάτων';
          this.courses = [];
          this.loading = false;
          this.cdr.markForCheck();
          return of([]);
        })
      )
      .subscribe(data => {
        console.log('[Courses] loaded:', data.length, 'courses');
        this.courses = data || [];
        this.applyFilters(); // ✅ client-side φίλτρο
        this.loading = false;
        this.cdr.markForCheck();
      });
  }

  // Εφαρμόζει φίλτρα category + level πάνω στα courses
  applyFilters(): void {
    this.filteredCourses = this.courses.filter(course => {
      const catOk =
        !this.selectedCategory || course.category === this.selectedCategory;
      const levelOk =
        !this.selectedLevel || course.level === this.selectedLevel;
      return catOk && levelOk;
    });

    // Ενημέρωση URL (ώστε να θυμάται φίλτρα)
    this.router.navigate(['/courses'], {
      queryParams: {
        category: this.selectedCategory || undefined,
        level: this.selectedLevel || undefined
      }
    });

    this.cdr.markForCheck();
  }

  getCategoryName(code: string): string {
    const categories: Record<string, string> = {
      programming: 'Προγραμματισμός',
      networks: 'Δίκτυα',
      security: 'Ασφάλεια',
      data: 'Δεδομένα'
    };
    return categories[code] || code;
  }

  getLevelName(code: string): string {
    const levels: Record<string, string> = {
      basic: 'Βασικό',
      intermediate: 'Μέσο',
      advanced: 'Προχωρημένο'
    };
    return levels[code] || code;
  }

  trackByFn(index: number, course: any): string | number {
    return course._id || course.slug || index;
  }
}
