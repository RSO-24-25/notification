# Notification 

## Overview
The Notification Microservice sends email notifications using gmail account and SMTP service. It allows external services to trigger email delivery through gRPC endpoints.

## Features
- **Email Notifications**: Sends emails using google SMTP.
- **Environment-Based Configuration**: Uses environment variables for customizable settings.
- **gRPC Communication**: communicates with other services on port 50051.
- **gRPC Communication**: communicates with other services on port 50051.

---

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- Docker
- Access to an SMTP server (e.g., Gmail, Outlook) + google account app password
- Environment variables for email credentials:
  - `EMAIL`: Sender's email address.
  - `SUPER_SECRET`: Sender's email password or app password.

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables in a `.env` file:
    ```dotenv
    EMAIL=your_email@example.com
    SUPER_SECRET=your_password
    ```

4. Run the gRPC server locally:
    ```bash
    python notification.py
    ```

### Using Docker
1. Build the Docker container:
    ```bash
    docker build -t notification-microservice .
    ```

2. Run the container:
    ```bash
    docker-compose up
    ```

---

## Usage

### CI/CD
- deploy to kubernetes with git push

### gRPC Endpoint

#### 1. **SendEmail**
- **Request**:
  - `recipient_email` (string): The recipient's email address.
  - `subject` (string): The subject of the email.
  - `message` (string): The email's body.
- **Response**:
  - `status` (string): Indicates the success or failure of the operation.
