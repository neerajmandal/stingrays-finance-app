# Tech Kata: Stingrays Finance App

**Duration:** 30 minutes  
**Difficulty:** Intermediate  
**Technologies:** Django, Python, HTML/CSS, JavaScript

## Overview

Welcome to the Stingrays Finance App coding kata! This exercise challenges you to enhance a Django-based financial web application by fixing critical bugs and implementing new features. You'll be working with a pre-configured Django project structure and are encouraged to use AI coding assistants to accelerate your development.

**Note:** Stingrays Finance is a small startup with a team of 3 developers who will maintain and evolve this application going forward.

## Prerequisites

- Basic knowledge of Django framework
- Understanding of Python web development
- Familiarity with HTML/CSS
- Git workflow knowledge

## Setup Instructions

**1.1 Initial Setup**

```bash
npm install
```

Ensure npm install executes successfully

**1.2 Start Application**

```bash
./start.sh
```

Ensure the application runs successfully before proceeding with the tasks.

**2. Project Structure Overview**
- `apps/core/`: Core application functionality
- `apps/pro/`: Professional features and dashboard
- `templates/`: HTML templates
- `static/`: CSS and static assets
- `StingraysFinance/`: Main Django project configuration

---

## Tasks

### 🐛 TICKET-001: Logo Display Bug - Stingray Logo Oversized

**Type:** Bug  
**Priority:** High  
**Estimated Time:** 5 minutes

**Description:**

The Stingrays Finance App logo is displaying at an inappropriately large size, negatively impacting the user interface and overall design consistency.

**Steps to Reproduce:**

1. Navigate to the home page
2. Observe the logo in the header/navigation area
3. Notice the logo is significantly oversized

**Expected Behavior:**

The logo should display at a reasonable size that fits proportionally within the navigation bar/header area.

**Acceptance Criteria:**

- [ ] Logo displays at an appropriate size (suggest max-width: 150-200px)
- [ ] Logo maintains aspect ratio
- [ ] Logo is responsive across different screen sizes
- [ ] Visual consistency with overall design is maintained

**Technical Notes:**

- Check CSS styling in templates or static CSS files
- May need to adjust width/height properties or use max-width
- Ensure responsive design considerations

---

### 🐛 TICKET-002: Investment Calculator Throws Error

**Type:** Bug  
**Priority:** Critical  
**Estimated Time:** 10 minutes

**Description:**

The investment calculator feature is currently broken and throws an error when users attempt to perform calculations. This is a critical bug as it affects core functionality.

**Steps to Reproduce:**

1. Navigate to the Investment Calculator page
2. Enter investment details (amount, interest rate, time period)
3. Submit the form
4. Observe error being thrown

**Expected Behavior:**

The calculator should accept user inputs, perform compound interest calculations, and display results without errors.

**Acceptance Criteria:**

- [ ] Users can input initial investment amount, interest rate, and time period
- [ ] Backend calculates compound interest accurately using formula: P(1 + r/n)^(nt)
- [ ] Results are displayed in a user-friendly format
- [ ] Form validation prevents invalid inputs (negative values, empty fields, etc.)
- [ ] Error handling for edge cases is implemented
- [ ] No errors are thrown during normal operation

**Technical Specifications:**

- Debug existing views and forms in `apps/core`
- Implement proper form handling and validation
- Add error handling for edge cases
- Follow Django best practices for URL routing
- Consider adding unit tests for calculation logic

**Investigation Notes:**

- Check `apps/core/views.py` for calculator logic
- Review form validation in templates
- Inspect error logs for specific error messages

---

### ✨ TICKET-003: Implement SEO-Optimized Blog System

**Type:** Feature  
**Priority:** Medium  
**Estimated Time:** 15 minutes

**Description:**

Implement a comprehensive blog system to drive organic traffic through search engine optimization. This feature will enable content marketing and improve the site's search visibility.

**User Story:**

As a marketing admin, I want to create and publish SEO-optimized blog posts so that we can drive organic traffic to the Stingrays Finance App and improve our search engine rankings.

**Requirements:**

- Create a blog model with necessary fields
- Implement Django admin interface for content management
- Build blog listing and detail pages
- Add SEO-friendly features (meta tags, structured URLs, sitemap)
- Ensure responsive design integration

**Acceptance Criteria:**

- [ ] Admin can create, edit, and publish blog posts through Django admin
- [ ] Blog posts have SEO-friendly URLs (auto-generated slugs from titles)
- [ ] Meta descriptions and title tags are automatically generated
- [ ] Blog listing page shows published posts with pagination (10 posts per page)
- [ ] Individual blog post pages are properly formatted and styled
- [ ] Basic search functionality for blog posts is implemented
- [ ] Blog integrates seamlessly with existing design

**SEO Features to Implement:**

- URL slug generation from post titles
- Meta description and keywords fields
- Meta title field (with fallback to post title)
- Open Graph tags for social media sharing (og:title, og:description, og:image)
- XML sitemap generation for search engines
- Published/draft status for posts
- Publication date tracking

**Technical Specifications:**

- Create blog models in `apps/core/models.py` or separate blog app
- Register models with Django admin
- Create views for blog list and detail pages
- Add URL routing for blog endpoints
- Create responsive templates for blog pages
- Consider using libraries like Wagtail or Django-SEO if time permits
- Implement pagination using Django's built-in pagination

**Design Considerations:**

- Match existing site styling and color scheme
- Ensure mobile responsiveness
- Include clear call-to-action buttons
- Add social sharing buttons on blog posts

---

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [SEO Best Practices](https://developers.google.com/search/docs)
- [Django Admin Customization](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
- Investment Calculation Formula: Compound Interest = P(1 + r/n)^(nt)
  - P = Principal amount
  - r = Annual interest rate (decimal)
  - n = Number of times interest is compounded per year
  - t = Time in years

---

## Submission Guidelines

1. Complete tickets in order of priority (TICKET-001, TICKET-002, TICKET-003)
2. Test each fix/feature before moving to the next ticket
3. Commit changes with meaningful commit messages referencing ticket numbers
4. Ensure all acceptance criteria are met before considering a ticket complete

**Good luck! Remember to leverage AI coding assistants to maximize your productivity within the 30-minute timeframe.**
