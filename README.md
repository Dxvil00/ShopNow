# 🛒 ShopNow - Modern E-Commerce Platform

A full-featured e-commerce web application built with Django, featuring a modern responsive design, comprehensive user management, and advanced shopping features.

![ShopNow Homepage](docs/screenshots/Screenshot%20(220).png)

## 📋 Table of Contents

- [✨ Features](#-features)
- [🖼️ Screenshots](#️-screenshots)
- [🛠️ Technologies Used](#️-technologies-used)
- [📁 Project Structure](#-project-structure)
- [🚀 Installation & Setup](#-installation--setup)
- [💻 Usage](#-usage)
- [🔧 Configuration](#-configuration)
- [📚 API Documentation](#-api-documentation)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🔗 Useful Resources](#-useful-resources)

---

## ✨ Features

### 🛍️ **Core E-Commerce Features**
- **Product Catalog**: Browse products by category with advanced filtering
- **Shopping Cart**: Add/remove items with real-time quantity updates
- **Secure Checkout**: Complete purchase flow with payment processing
- **Order Management**: Track order status and view order history
- **Wishlist**: Save favorite products for later purchase
- **Product Reviews & Ratings**: User-generated reviews with star ratings
- **Search Functionality**: Find products quickly with search and filters

### 👤 **User Management**
- **User Registration & Authentication**: Secure signup/login system
- **Social Authentication**: Google OAuth integration
- **Profile Management**: Update personal information and preferences
- **Password Reset**: Secure password recovery via email
- **Admin Panel**: Comprehensive admin interface for store management

### 🎨 **UI/UX Features**
- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Modern Interface**: Clean, intuitive user experience
- **Dynamic Pricing**: Support for discounts and promotional codes
- **Multi-currency**: USD and Philippine Peso support
- **Image Gallery**: Product images with zoom and gallery view

### 🔒 **Security & Performance**
- **CSRF Protection**: Built-in security measures
- **Session Management**: Secure user sessions
- **Admin Access Control**: Restricted admin panel access
- **Static File Optimization**: Compressed and cached static assets
- **Database Optimization**: Efficient queries and indexing

---

## 🖼️ Screenshots

### Homepage & Navigation
![Homepage](docs/screenshots/Screenshot%20(220).png)
*Modern homepage with featured products and promotional banners*

### User Authentication
![Login Page](docs/screenshots/Screenshot%20(233).png)
*User-friendly login interface with social authentication*

![Register Page](docs/screenshots/Screenshot%20(232).png)
*User-friendly Register interface with social authentication*

### User Profile
![User Profile](docs/screenshots/Screenshot%20(219).png)
*Comprehensive user profile management*

### Product Catalog
![Product Catalog](docs/screenshots/Screenshot%20(221).png)
*Comprehensive product listing with filtering options*

### Product Details
![Product Details](docs/screenshots/Screenshot%20(234).png)
*Detailed product view with images, reviews, and purchase options*

### Shopping Cart
![Shopping Cart](docs/screenshots/Screenshot%20(225).png)
*Shopping cart with quantity controls and price calculations*

### Checkout Process
![Checkout](docs/screenshots/Screenshot%20(226).png)
*Streamlined checkout process with order summary*

---

## 🛠️ Technologies Used

### **Backend**
- **Django 4.2.20** - High-level Python web framework
- **Python 3.8+** - Programming language
- **SQLite/PostgreSQL** - Database (configurable)
- **Django Allauth** - Authentication system
- **Pillow** - Image processing
- **Gunicorn** - WSGI HTTP Server (production)

### **Frontend**
- **HTML5** - Markup language
- **CSS3** - Styling
- **JavaScript** - Client-side functionality
- **Bootstrap 5** - Responsive CSS framework
- **jQuery** - JavaScript library

### **Development & Deployment**
- **Git** - Version control
- **pip** - Package management
- **virtualenv** - Virtual environment
- **Whitenoise** - Static file serving
- **python-decouple** - Environment configuration

---

## 📁 Project Structure

```
ShopNow/
├── src/                          # Main source code
│   ├── main/                     # Django project settings
│   │   ├── settings.py          # Project configuration
│   │   ├── urls.py              # Main URL routing
│   │   ├── middleware/          # Custom middleware
│   │   └── wsgi.py              # WSGI configuration
│   ├── store/                   # Main e-commerce app
│   │   ├── models.py            # Database models
│   │   ├── views.py             # View logic
│   │   ├── urls.py              # App URL routing
│   │   ├── forms.py             # Form definitions
│   │   ├── admin.py             # Admin interface
│   │   └── templates/           # HTML templates
│   ├── accounts/                # User authentication
│   │   └── adapter.py           # Custom auth adapter
│   ├── static/                  # Static files (CSS, JS, images)
│   ├── media/                   # User-uploaded files
│   └── manage.py                # Django management script
├── docs/                        # Documentation
│   └── screenshots/             # Application screenshots
├── requirements.txt             # Python dependencies
├── LICENSE                      # Project license
└── README.md                    # This file
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ShopNow.git
   cd ShopNow
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Edit .env file with your settings
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```

5. **Database Setup**
   ```bash
   cd src
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

9. **Access the Application**
   - Main site: http://127.0.0.1:8000
   - Admin panel: http://127.0.0.1:8000/admin

---

## 💻 Usage

### For Users
1. **Browse Products**: Visit the homepage to see featured products
2. **Search & Filter**: Use the search bar and category filters
3. **Add to Cart**: Click "Add to Cart" on any product
4. **Checkout**: Complete your purchase in the checkout process
5. **Track Orders**: View order status in your profile

### For Administrators
1. **Access Admin Panel**: Login at `/admin`
2. **Manage Products**: Add, edit, or remove products
3. **Handle Orders**: Process and update order status
4. **User Management**: Manage user accounts and permissions
5. **Analytics**: View sales and user statistics

---

## 🔧 Configuration

### Database Configuration
The application supports multiple database backends:

**SQLite (Default)**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**PostgreSQL**
```python
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
```

### Email Configuration
Configure email settings for password reset and notifications:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### Static Files Configuration
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

---

## 📚 API Documentation

### Key Models

#### Product Model
```python
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=500)
    is_featured = models.BooleanField(default=False)
    discount_percentage = models.PositiveIntegerField(default=0)
```

#### Order Model
```python
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Key Views

#### Product Views
- `product_list()` - Display all products
- `product_detail()` - Show individual product
- `product_search()` - Search functionality

#### Cart Views
- `add_to_cart()` - Add item to cart
- `remove_from_cart()` - Remove item from cart
- `update_cart()` - Update quantities

#### User Views
- `user_profile()` - User profile management
- `order_history()` - View past orders
- `wishlist()` - Manage wishlist

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/ShopNow.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Your Changes**
   - Follow PEP 8 style guidelines
   - Add tests for new features
   - Update documentation

4. **Commit Your Changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```

5. **Push to Branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**

### Development Guidelines
- Write clear, descriptive commit messages
- Test your changes thoroughly
- Update documentation as needed
- Follow the existing code style
- Add appropriate error handling

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Useful Resources

### Django Resources
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Allauth Documentation](https://django-allauth.readthedocs.io/)

### Frontend Resources
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Bootstrap Examples](https://getbootstrap.com/docs/5.3/examples/)
- [CSS Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

### E-Commerce Best Practices
- [E-Commerce UX Design](https://www.nngroup.com/articles/ecommerce-user-experience/)
- [Payment Security](https://stripe.com/docs/security)
- [SEO for E-Commerce](https://developers.google.com/search/docs/advanced/ecommerce)

### Development Tools
- [VS Code Extensions for Django](https://marketplace.visualstudio.com/search?term=django)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/)
- [Django Extensions](https://django-extensions.readthedocs.io/)

### Deployment Resources
- [Deploying Django to Heroku](https://devcenter.heroku.com/articles/deploying-python)
- [Django on DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-deploy-django-to-app-platform)
- [Django Production Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)

### Testing Resources
- [Django Testing](https://docs.djangoproject.com/en/stable/topics/testing/)
- [Pytest for Django](https://pytest-django.readthedocs.io/)
- [Coverage.py](https://coverage.readthedocs.io/)

### Performance Optimization
- [Django Performance](https://docs.djangoproject.com/en/stable/topics/performance/)
- [Database Optimization](https://docs.djangoproject.com/en/stable/topics/db/optimization/)
- [Caching in Django](https://docs.djangoproject.com/en/stable/topics/cache/)

---

## 📞 Support

If you encounter any issues or have questions:

1. **Check the Documentation**: Review this README and Django docs
2. **Search Issues**: Look for similar issues in the repository
3. **Create an Issue**: Report bugs or request features
4. **Contact**: Reach out to the maintainers

---

**Happy Shopping! 🛒✨**
