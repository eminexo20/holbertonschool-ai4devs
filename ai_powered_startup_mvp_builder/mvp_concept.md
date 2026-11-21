# MVP Concept - EcoRide (Sustainable Campus & Commuter Ride-Sharing App)

## Problem Statement
Daily university and office commuters face high fuel costs, heavy traffic congestion, and unnecessary carbon emissions due to single-occupancy car trips, while existing ride-hailing apps are too expensive for short daily commutes and lack trusted community matching.

## Target Users
- University students commuting daily to campus
- Corporate employees working in shared business districts
- Environmentally conscious drivers looking to split fuel expenses

## Core Features
- **Verified Commute Ride Posting & Search:** Drivers can publish recurring daily routes (origin, destination, departure time, available seats, and cost split) and riders can filter rides by route and schedule.
- **Instant Seat Booking & Status Tracking:** Riders can request and reserve a seat with real-time seat count updates and booking status (`Pending`, `Confirmed`, `Completed`).
- **In-App Ride Coordination Chat:** Lightweight trip-specific messaging allowing confirmed drivers and riders to coordinate exact pickup points.
- **CO2 & Cost Savings Estimator:** Automatically calculates estimated fuel money saved and kilograms of CO2 emissions avoided per shared trip.
- **User Trust Profile & Ride History:** Displays university/company email verification badge, past completed trips count, and peer ratings.

## Constraints
- **Timeline:** 2-week lean MVP sprint built by a solo developer using AI-assisted tooling.
- **Budget & Infrastructure:** Must run entirely on free-tier cloud infrastructure (Vercel frontend + Supabase PostgreSQL/Auth).
- **Payment Scope:** No integrated credit card/payment gateway in v1; cost splitting is handled off-platform (cash or peer-to-peer transfer) to avoid financial compliance delays.
- **Platform Scope:** Mobile-responsive web application (PWA) only; native iOS and Android apps are out of scope for the MVP.
- **Scale Limit:** Designed for a single pilot city/campus community (up to 1,000 active users and 500 concurrent ride listings).
