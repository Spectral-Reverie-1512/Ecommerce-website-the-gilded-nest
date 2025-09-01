# 🛒 E-Commerce Website (Django)

A full-featured e-commerce platform built with **Django**, featuring product management, categories, shopping cart, wishlist, checkout, and sale sections. This project demonstrates how to design scalable online store logic with clean models, reusable templates, and user-friendly interfaces.

## 🚀 Features

* **Product & Category Management** with slugs for SEO-friendly URLs
* **Shopping Cart** to add, update, and remove products
* **Wishlist** to save favorite items for later
* **Orders & OrderItems** separation for structured purchase history
* **Mega Sale Section** with dynamic discounts and prices
* **Responsive UI** built with Bootstrap for seamless browsing
* **Reusable Templates** with Django template inheritance
* **Admin Panel** for managing products, orders, and users

## ⚙️ Tech Stack

* **Backend:** Django, Python
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **Other:** Django ORM, Template Inheritance, Slug-based URLs

## 📂 Project Structure (Important Files)

* `models.py` → Defines Products, Categories, Orders, OrderItems, Wishlist
* `views.py` → Handles logic for products, cart, checkout, wishlist, and sales
* `urls.py` → Maps URLs to views
* `templates/` → HTML templates (base, product detail, sale, wishlist, etc.)
* `admin.py` → Registers models for easy management in Django Admin
