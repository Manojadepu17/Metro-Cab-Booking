# Metro Cab Booking

## Overview

Metro Cab Booking is a web application project focused on implementing a cab booking workflow with a user-friendly interface and application-level data handling.

The project demonstrates practical web development fundamentals such as form-driven user interactions, route/workflow handling, and structured project organization. It serves as a supporting project in my full-stack portfolio.

---

## Key Features

- Cab booking workflow interface
- Form-based input handling for booking details
- Structured UI for booking-related interactions
- Project modularization for maintainability

---

## Technology Stack

**Frontend**
- HTML5
- CSS3
- JavaScript

**Backend**
- Node.js
- Express.js

**Database**
- MySQL

**APIs**
- RESTful endpoints for booking operations

**Tools**
- Git
- GitHub
- VS Code
- Postman

---

## System Architecture

1. Frontend captures booking details and user actions.
2. Requests are sent to backend API endpoints.
3. Backend processes booking logic and persists records.
4. Database stores booking and user-related information.
5. Responses are rendered in the frontend workflow screens.

---

## Project Structure

```text
metro-cab-booking/
├── client/                # Frontend files
├── server/                # Backend API
├── server/routes/         # Booking-related endpoints
├── server/controllers/    # Booking logic handlers
├── server/models/         # Data models
└── README.md
```

---

## Installation & Setup

```bash
git clone https://github.com/Manojadepu17/metro-cab-booking.git
cd metro-cab-booking
```

Install dependencies:
```bash
cd client
npm install
cd ../server
npm install
```

Create backend `.env`:
```env
PORT=5000
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=metro_cab_booking
```

---

## Running the Application

Backend:
```bash
cd server
npm run dev
```

Frontend:
```bash
cd client
npm start
```

---

## API Documentation (Core Endpoints)

- `POST /api/bookings` – Create new booking
- `GET /api/bookings` – Fetch bookings
- `GET /api/bookings/:id` – Booking details
- `PUT /api/bookings/:id` – Update booking
- `DELETE /api/bookings/:id` – Cancel/delete booking

---

## Screenshots / Demo

Recommended captures:
- Booking form
- Booking confirmation screen
- Booking history/list view

If deployed, add live demo link to README and repo description.

---

## Future Improvements

- Add fare estimation logic
- Add booking status tracking
- Add user authentication for booking history
- Improve validation and error messaging

---

## Author

**Adepu Manoj**  
LinkedIn: https://www.linkedin.com/in/manoj-adepu-4a32a2206  
GitHub: https://github.com/Manojadepu17
