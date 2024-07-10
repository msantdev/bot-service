# Bot Service for Expense Management

This repository contains the Bot Service component of an expense management Telegram chatbot. The bot allows users to add expenses by sending messages to it, which are then processed and stored in a Supabase (PostgreSQL) database.

## Features

- Recognizes authorized Telegram users from a database whitelist.
- Processes incoming messages to extract expense details.
- Automatically categorizes expenses based on message content.
- Persists expense data into a Supabase database.
- Provides feedback to users upon successful expense addition.

## Tech Stack

- **Python 3.8+**
- **Flask** - Micro web framework for Python.
- **Supabase** - Backend as a service (BaaS) providing a PostgreSQL database.
- **supabase-py** - Python client for Supabase.
- **requests** - HTTP library for Python.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Clone the Repository](#clone-the-repository)
  - [Create and Activate a Virtual Environment](#create-and-activate-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Configure Environment Variables](#configure-environment-variables)
  - [Run the Bot Service](#run-the-bot-service)
- [Running the Bot Service](#running-the-bot-service)

## Prerequisites

- Python 3.8+
- Supabase account (for database setup)

## Setup Instructions

### Clone the Repository

```sh
git clone https://github.com/msantdev/bot-service.git
cd bot-service
```

###  Create and Activate a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate
```
windows:
```sh
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Configure Environment Variables
```sh
BOT_SERVICE_API_KEY=
SUPABASE_URL=
SUPABASE_KEY=
```

### Running the Bot Service
```sh
python3 main.py
```

### Additional Notes

Ensure you have the required Supabase URL and API key in your .env file.
The bot only processes messages from users listed in the users table.
The bot categorizes expenses into predefined categories and responds accordingly.


