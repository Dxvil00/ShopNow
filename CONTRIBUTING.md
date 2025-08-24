# 🤝 Contributing to ShopNow

Thank you for your interest in contributing to ShopNow! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Feature Requests](#feature-requests)
- [Code of Conduct](#code-of-conduct)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git
- A code editor (VS Code, PyCharm, etc.)
- Basic knowledge of Django, HTML, CSS, and JavaScript

### Fork and Clone
1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/ShopNow.git
   cd ShopNow
   ```
3. Add the original repository as upstream:
   ```bash
   git remote add upstream https://github.com/original-owner/ShopNow.git
   ```

---

## 🔧 Development Setup

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt  # if available
```

### 2. Database Setup
```bash
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 3. Environment Variables
Create a `.env` file based on the example in [SETUP.md](SETUP.md)

### 4. Run Development Server
```bash
python manage.py runserver
```

---

## 📝 Code Style Guidelines

### Python (Django)
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions small and focused
- Use type hints where appropriate

### Example Code Style
```python
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product, Category


@login_required
def product_detail(request, product_id: int) -> JsonResponse:
    """
    Display detailed information about a specific product.
    
    Args:
        request: HTTP request object
        product_id: ID of the product to display
        
    Returns:
        JsonResponse: Product details in JSON format
    """
    product = get_object_or_404(Product, id=product_id)
    
    context = {
        'product': product,
        'related_products': product.category.product_set.exclude(id=product.id)[:4]
    }
    
    return render(request, 'store/product-detail.html', context)
```

### HTML/CSS
- Use semantic HTML elements
- Follow BEM methodology for CSS classes
- Keep CSS organized and commented
- Use Bootstrap classes when appropriate
- Ensure responsive design

### JavaScript
- Use ES6+ features
- Follow consistent naming conventions
- Add comments for complex logic
- Handle errors gracefully

---

## 🧪 Testing Guidelines

### Running Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test store

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### Writing Tests
- Write tests for all new features
- Test both success and failure cases
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)

### Example Test
```python
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from store.models import Product, Category


class ProductViewsTest(TestCase):
    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            price=99.99
        )

    def test_product_list_view(self):
        """Test that product list view returns correct response."""
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

    def test_product_detail_view(self):
        """Test that product detail view returns correct product."""
        response = self.client.get(
            reverse('product_detail', args=[self.product.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
```

---

## 🔄 Pull Request Process

### 1. Create a Feature Branch
```bash
git checkout -b feature/amazing-feature
# or
git checkout -b fix/bug-fix
```

### 2. Make Your Changes
- Write clean, well-documented code
- Add tests for new functionality
- Update documentation if needed
- Follow the code style guidelines

### 3. Commit Your Changes
```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "feat: add shopping cart functionality

- Add cart model and views
- Implement add/remove cart items
- Add cart template with Bootstrap styling
- Include unit tests for cart operations"
```

### 4. Push to Your Fork
```bash
git push origin feature/amazing-feature
```

### 5. Create Pull Request
1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Select your feature branch
4. Fill out the PR template
5. Submit the PR

### 6. PR Template
```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Screenshots (if applicable)
Add screenshots to help explain your changes.

## Checklist
- [ ] Code follows project style guidelines
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No console errors
- [ ] Responsive design maintained
```

---

## 🐛 Issue Reporting

### Before Creating an Issue
1. Check existing issues to avoid duplicates
2. Search the documentation for solutions
3. Try to reproduce the issue locally

### Issue Template
```markdown
## Bug Description
Clear and concise description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g., Windows 10, macOS 12.0]
- Browser: [e.g., Chrome 96, Firefox 95]
- Python Version: [e.g., 3.9.7]
- Django Version: [e.g., 4.2.20]

## Additional Context
Add any other context, screenshots, or logs about the issue.
```

---

## 💡 Feature Requests

### Feature Request Template
```markdown
## Feature Description
Clear and concise description of the feature.

## Problem Statement
What problem does this feature solve?

## Proposed Solution
Describe the solution you'd like to see.

## Alternative Solutions
Describe any alternative solutions you've considered.

## Additional Context
Add any other context, mockups, or examples.
```

---

## 📚 Documentation

### Updating Documentation
- Keep README.md up to date
- Update docstrings for new functions
- Add comments for complex code
- Update setup instructions if needed

### Documentation Standards
- Use clear, concise language
- Include code examples
- Add screenshots for UI changes
- Keep documentation organized

---

## 🔒 Security

### Security Guidelines
- Never commit sensitive information (API keys, passwords)
- Use environment variables for configuration
- Validate all user inputs
- Follow Django security best practices
- Report security vulnerabilities privately

### Reporting Security Issues
If you discover a security vulnerability, please report it privately to the maintainers rather than creating a public issue.

---

## 🎯 Code of Conduct

### Our Standards
- Be respectful and inclusive
- Use welcoming and inclusive language
- Be collaborative and constructive
- Focus on what is best for the community
- Show empathy towards other community members

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or insulting comments
- Publishing others' private information
- Other conduct inappropriate in a professional setting

---

## 🏆 Recognition

Contributors will be recognized in:
- Project README.md
- Release notes
- Contributor hall of fame (if applicable)

---

## 📞 Getting Help

If you need help with contributing:
1. Check the documentation
2. Search existing issues
3. Ask questions in discussions
4. Contact maintainers

---

**Thank you for contributing to ShopNow! 🚀**
