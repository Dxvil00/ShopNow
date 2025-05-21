from django.urls import path
from . import views

urlpatterns = [
    # 📌 Public Pages
    path('', views.home, name='store_home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('contact_us/', views.contact, name='contact_us'),  # Consider merging with /contact/
    path('subscribe/', views.subscribe_email, name='subscribe'),

    # 🛍️ Product Listings & Search
    path('products/', views.product_view, name='products'),
    path('products/<str:category>/', views.product_view, name='products_by_category'),
    path('product-details/<str:product_id>/', views.product_details, name='product-details'),
    path('search-product/', views.search_product, name='search-product'),

    # 👤 User Account Pages
    path('profile-page/', views.profile_view, name='profile-page'),
    path('edit-profile-page/', views.edit_profile_view, name='edit-profile-page'),
    path('change-password/', views.change_password_view, name='change-password'),

    # 🛒 Cart Operations
    path('cart-view/', views.cart_view, name='cart-view'),
    path('add-to-cart/<str:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('update-cart/<str:product_id>/', views.update_cart, name='update-cart'),
    path('remove-from-cart/<str:product_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('apply-promo/', views.apply_promo, name='apply-promo'),

    # ✅ Checkout & Orders
    path('checkout-view/', views.checkout_view, name='checkout-view'),
    path('order-success-page/', views.order_success_page, name='order-success-page'),
    path('orders-page/', views.orders_view, name='orders-page'),
    path('order-details-view/<str:order_id>/', views.order_details_view, name='order-details-view'),

    # 🌟 Product Reviews
    path('product-review-view/<str:order_id>/', views.product_review_view, name='product-review-view'),
    path('add-review/<str:product_id>/', views.add_review, name='add-review'),

    # ❤️ Wishlist
    path('add-to-wishlist/<str:product_id>/', views.add_to_wishlist, name='add-to-wishlist'),
    path('remove-from-wishlist/<str:product_id>/', views.remove_from_wishlist, name='remove-from-wishlist'),
    path('wishlist-page/', views.wishlist_view, name='wishlist-page'),
    path('wishlist-toggle/', views.toggle_wishlist, name='toggle-wishlist'),

    # 🔐 Authentication
    path('login/', views.login_user, name='login-page'),
    path('register/', views.register_user, name='register-page'),
    path('logout/', views.logout_view, name='logout'),

    # 🔑 Password Reset
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.password_reset_sent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.reset_password, name='reset-password'),
    path('enter-reset-code/', views.enter_reset_code, name='enter-reset-code'),
]
