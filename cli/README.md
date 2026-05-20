# CLI Grocery Store Management System

A lightweight, terminal-based application for managing grocery store inventory, handling user accounts, and processing basic sales. Built entirely in Python, it uses a local SQLite database to persist data, meaning no external database setup is required.

## Features

* **Secure Authentication:** User passwords are hashed and salted using `bcrypt`.
* **Admin Panel:** Add, delete, and view inventory items, and view registered users.
* **User Dashboard:** Browse the store and process simulated purchases.
* **Persistent Storage:** Automatically creates and manages a local `info.db` SQLite database.
* **Clean UI:** Terminal screens are cleared automatically between actions, with custom ASCII banners powered by `pyfiglet`.

## Prerequisites

You must have **Python 3.x** installed on your system. You can check if Python is installed by running:
`python --version` (or `python3 --version` on Mac/Linux).

## Installation & Quick Start

Follow these steps to get the app running right away:

**1. Clone or download the repository**
Ensure `main.py` and `requirements.txt` are in the same folder.

**2. Install dependencies**
Open your terminal, navigate to the folder containing the files, and run:
```bash
pip install -r requirements.txt
```