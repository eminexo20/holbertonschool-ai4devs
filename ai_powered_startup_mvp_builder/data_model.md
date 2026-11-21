# Data Model - EcoRide MVP

## Entity-Relationship Overview
- One **User** can create many **Rides** (as a driver) and make many **Bookings** (as a rider).
- One **Ride** can have many **Bookings** and many **Messages** in its trip chat thread.
- One **Booking** belongs to exactly one **Ride** and one **User** (rider), and can produce one **Review** upon completion.

---

## Entities & Schema Definitions

### 1. `users`
Stores registered commuters, institutional verification status, and aggregated trust/impact metrics.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `UUID` | Primary Key, Default `gen_random_uuid()` | Unique user identifier |
| `full_name` | `VARCHAR(100)` | Not Null | Display name of driver or rider |
| `email` | `VARCHAR(150)` | Unique, Not Null | University or corporate email address |
| `is_verified` | `BOOLEAN` | Default `false` | True once institutional email OTP is confirmed |
| `avg_rating` | `DECIMAL(2,1)` | Default `5.0` | Average peer rating across completed trips |
| `total_co2_saved_kg` | `DECIMAL(8,2)` | Default `0.00` | Cumulative CO2 emissions saved in kilograms |
| `created_at` | `TIMESTAMP` | Default `NOW()` | Account creation timestamp |

### 2. `rides`
Stores scheduled commute routes published by drivers.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `UUID` | Primary Key, Default `gen_random_uuid()` | Unique ride listing identifier |
| `driver_id` | `UUID` | Foreign Key -> `users(id)`, Not Null | User offering the ride |
| `origin` | `VARCHAR(150)` | Not Null | Starting neighborhood or transit hub |
| `destination` | `VARCHAR(150)` | Not Null | Target campus or business district |
| `departure_time` | `TIMESTAMP` | Not Null | Scheduled departure date and time |
| `distance_km` | `DECIMAL(5,1)` | Not Null | Estimated route distance for CO2 calculation |
| `total_seats` | `INTEGER` | Not Null, Check (`total_seats > 0`) | Total passenger seats offered |
| `available_seats` | `INTEGER` | Not Null, Check (`available_seats >= 0`) | Remaining unbooked seats |
| `price_per_seat` | `DECIMAL(6,2)` | Not Null, Default `0.00` | Suggested fuel contribution per rider |
| `status` | `VARCHAR(20)` | Default `'open'` | Ride lifecycle state (`open`, `full`, `completed`, `cancelled`) |
| `created_at` | `TIMESTAMP` | Default `NOW()` | Listing creation timestamp |

### 3. `bookings`
Tracks seat reservations linking riders to specific rides.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `UUID` | Primary Key, Default `gen_random_uuid()` | Unique booking identifier |
| `ride_id` | `UUID` | Foreign Key -> `rides(id)`, Not Null | Associated ride listing |
| `rider_id` | `UUID` | Foreign Key -> `users(id)`, Not Null | Passenger requesting the seat |
| `seats_booked` | `INTEGER` | Not Null, Default `1` | Number of seats reserved |
| `status` | `VARCHAR(20)` | Default `'pending'` | Approval state (`pending`, `confirmed`, `declined`, `cancelled`) |
| `created_at` | `TIMESTAMP` | Default `NOW()` | Booking request timestamp |

### 4. `messages`
Stores trip-specific coordination chat messages between drivers and confirmed riders.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `UUID` | Primary Key, Default `gen_random_uuid()` | Unique message identifier |
| `ride_id` | `UUID` | Foreign Key -> `rides(id)`, Not Null | Trip chat room identifier |
| `sender_id` | `UUID` | Foreign Key -> `users(id)`, Not Null | Author of the message |
| `content` | `TEXT` | Not Null | Plain-text chat message body |
| `sent_at` | `TIMESTAMP` | Default `NOW()` | Message delivery timestamp |

### 5. `reviews`
Stores post-trip peer feedback to maintain community safety and reliability.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `UUID` | Primary Key, Default `gen_random_uuid()` | Unique review identifier |
| `booking_id` | `UUID` | Foreign Key -> `bookings(id)`, Unique, Not Null | Completed booking being reviewed |
| `reviewer_id` | `UUID` | Foreign Key -> `users(id)`, Not Null | User submitting the rating |
| `reviewee_id` | `UUID` | Foreign Key -> `users(id)`, Not Null | User receiving the rating |
| `rating` | `INTEGER` | Not Null, Check (`rating BETWEEN 1 AND 5`) | Star rating from 1 to 5 |
| `comment` | `VARCHAR(300)` | Nullable | Optional short written feedback |
| `created_at` | `TIMESTAMP` | Default `NOW()` | Review submission timestamp |
