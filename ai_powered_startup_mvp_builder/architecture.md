# System Architecture - EcoRide MVP

## High-Level System Diagram

+-----------------------------------------------------------------------+
|                        Client Layer (Browser / PWA)                   |
|                 React + Vite + Tailwind CSS (Vercel)                  |
|  [Ride Search UI]   [Post Ride Form]   [Trip Chat]   [Impact Stats]   |
+-----------------------------------+-----------------------------------+
                                    |
                          HTTPS / REST API + WSS
                                    |
                                    v
+-----------------------------------------------------------------------+
|                       Backend & API Layer (Render)                    |
|                     Node.js + Express REST Server                     |
|  - Auth & JWT Middleware       - Ride & Seat Booking Controller       |
|  - CO2 Savings Calculator      - Input Validation & Rate Limiting     |
+--------------------+----------------------------------+---------------+
                     |                                  |
             SQL / Connection Pool              Realtime Subscriptions
                     |                                  |
                     v                                  v
+------------------------------------+  +-------------------------------+
|    Database Layer (Supabase)       |  |   Realtime & Auth Services    |
|         PostgreSQL 15              |  |          (Supabase)           |
|  - users                           |  |  - Email OTP Verification     |
|  - rides                           |  |  - Postgres Realtime Channels |
|  - bookings                        |  |    (Trip Coordination Chat)   |
|  - messages                        |  |                               |
|  - reviews                         |  |                               |
+------------------------------------+  +-------------------------------+

## Component Responsibilities
- **Frontend (React + Tailwind CSS on Vercel):** Renders a mobile-first responsive web interface with client-side routing, optimistic UI updates for seat counts, and real-time chat subscription listeners.
- **Backend API (Node.js + Express on Render):** Enforces business logic including atomic seat-decrement transactions (preventing overbooking), role authorization (driver vs. rider), and CO2/cost savings calculations (`0.21 kg CO2/km` baseline).
- **Database (PostgreSQL on Supabase):** Stores relational entities with foreign-key integrity, row-level security policies, and indexed route/date columns for fast commute searches.
- **Realtime & Auth (Supabase):** Handles university/corporate email verification and broadcasts new trip chat messages over WebSockets without custom socket-server overhead.
