# Django Blog App

A fully functional blog application built with Django 5, focused on using Django’s built-in templating system — without DRF or external frontend frameworks. The app follows clean architecture principles and includes essential blog features like tagging, full-text searching and with trigram similarity, RSS feeds, and post sharing via email.

This project was developed as part of my Django learning journey — following best practices to strengthen my understanding of core Django.

## Features

- Django templating (no frontend framework)
- SEO-friendly slugs and canonical URLs
- Full blog post CRUD (admin-managed)
- Comment system (linked to each post)
- Post sharing via email
- Tagging system using django-taggit
- Trigram similarity search with PostgreSQL
- Similar posts recommendation
- Custom Django Admin interface for posts/comments
- Pagination for post list views
- RSS feed for latest posts
- Sitemap.xml for SEO and crawler support

## Screenshots

![Screenshot from 2025-06-07 17-47-31](https://github.com/user-attachments/assets/19afc506-feaa-4376-9075-2bfa52b45715)
![Screenshot from 2025-06-07 18-08-31](https://github.com/user-attachments/assets/4b9c591d-3d6b-4b1e-808b-5265ef9a10e4)
![Screenshot from 2025-06-07 18-11-31](https://github.com/user-attachments/assets/157f34de-1282-464d-8062-14a92316fedf)
![Screenshot from 2025-06-07 18-11-00](https://github.com/user-attachments/assets/68bd8ce7-b756-4786-8be6-ef578b587187)
![Screenshot from 2025-06-07 18-11-12](https://github.com/user-attachments/assets/f2114b80-eb8f-4fa2-92a6-1c804b9c9557)
![Screenshot from 2025-06-07 18-09-17](https://github.com/user-attachments/assets/2683f340-8d18-4f74-8a56-c33c87221d38)
![Screenshot from 2025-06-07 18-10-31](https://github.com/user-attachments/assets/6bfb80ed-ec16-44f7-bd4f-666b453ccb4c)
![Screenshot from 2025-06-07 18-12-18](https://github.com/user-attachments/assets/cf0fe26f-f4ff-4025-8c60-779415e34ef5)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Pietruszko/blog-app.git
    cd blog-app
    ```
2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up environment variables:**
    - Copy .env.template to .env:
    ```bash
    cp .env.template .env
    ```
    - Fill in your own values (DB config, email credentials, etc.) inside .env.
5. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```
6. **Create a superuser (for the admin panel):**
    ```bash
    python manage.py createsuperuser
    ```
7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

- Go to http://localhost:8000/blog/ to view the blog
- Admin panel: http://localhost:8000/admin/
- Share any post via email (form on post detail page)
- Use the tag links to filter by topic
- Use the search form to find posts (leveraging trigram similarity)
- Subscribe via RSS: http://localhost:8000/blog/feed/
- Visit the sitemap: http://localhost:8000/sitemap.xml

## Simplified project Structure

```text
blog-app/
├── blog/               # Main app: posts, comments, tags, templates
│   ├── migrations/     # Migrations to database
│   ├── admin.py        # Custom admin for posts & comments
│   ├── forms.py        # Comment and email sharing forms
│   ├── models.py       # Post and Comment models
│   ├── urls.py         # App-specific URLs
│   ├── views.py        # Class and function-based views
│   ├── feeds.py        # RSS feed implementation
│   ├── templates/      # HTML templates
│   │   ├── base.html   # Main template
│   ├── templatetags/   # Template custom tags
│   └── static/css      # Static files (CSS, JS)
├── config/             # Project config
│   ├── settings.py     # Settings with .env support
│   ├── urls.py         # Root URL configuration
├── .env.template       # Environment variables template
├── .env                # Environment variables
├── requirements.txt    # Packages used in project
├── .gitignore          # Files to excludes when commiting to repo
├── manage.py           # Django file to execute commands (django-admin)
```

## Endpoints

| Path                          | Description                             |
| ------------------------------| --------------------------------------- |
| `/blog/`                      | List view of all blog posts (paginated) |
| `/blog/<y>/<m>/<d>/<slug>/`   | Detail view for a single post           |
| `/blog/tag/<tag>/`            | Filter posts by tag                     |
| `/blog/<id>/share/`           | Share post via email                    |
| `/blog/<id>/comment/`         | Add comment to post                     |
| `/blog/search/`               | Full-text search                        |
| `/blog/feed/`                 | RSS feed for latest posts               |
| `/sitemap.xml`                | Sitemap for search engines              |
| `/admin/`                     | Django admin panel                      |

## Purpose

This project was built to strengthen my knowledge of Django fundamentals — views, models, forms, custom admin, tags, template rendering, and email systems. It's a DRF-free application using classic Django tooling.

## Testing

Tests are not included in this version of the project as it's focused on functionality and templating.
