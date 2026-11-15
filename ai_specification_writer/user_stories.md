# User Stories: CarpoolConnect

### User Story 1
As a corporate employee, I want to sign in using my company SSO/email so that I can join a verified network of colleagues.
**Acceptance Criteria**:
- User can authenticate via corporate Single Sign-On (SSO) or verified company email domain.
- Unverified external email domains are automatically blocked from registration.
- User profile displays verified department and office location upon login.
**Priority**: MVP

### User Story 2
As a corporate driver, I want to publish my daily commute route and schedule so that colleagues along my way can request a seat.
**Acceptance Criteria**:
- Driver can set home pickup zone, office destination, departure time, and available seats (1–4).
- Driver can configure recurring weekly commute days (e.g., Monday to Friday).
- Published ride becomes immediately searchable by eligible passengers.
**Priority**: MVP

### User Story 3
As a corporate passenger, I want to search for nearby drivers heading to my office so that I can find a convenient and affordable ride.
**Acceptance Criteria**:
- Passenger enters pickup point, office destination, and desired arrival time.
- System displays matching drivers within a 3 km detour radius sorted by schedule compatibility.
- Passenger can send a seat request and book a ride in under 2 minutes.
**Priority**: MVP

### User Story 4
As a corporate driver, I want to review and accept or decline passenger seat requests so that I maintain full control over who rides in my vehicle.
**Acceptance Criteria**:
- Driver receives an instant push notification when a passenger requests a seat.
- Driver can view the passenger's verified profile, department, and rating before deciding.
- Accepting a request automatically decreases the available seat count by one.
**Priority**: MVP

### User Story 5
As a corporate passenger, I want to split fuel costs automatically based on trip distance so that ride sharing remains fair and hassle-free.
**Acceptance Criteria**:
- System calculates a transparent per-kilometer fuel contribution before booking confirmation.
- Payment is processed automatically via the in-app wallet upon trip completion.
- Both driver and passenger receive a digital trip cost breakdown.
**Priority**: High

### User Story 6
As a corporate passenger, I want to track my driver's live location and arrival time on a map so that I know exactly when to step outside.
**Acceptance Criteria**:
- Live GPS tracking activates 15 minutes prior to the scheduled pickup time.
- Passenger receives automated alerts when the driver is 5 minutes away and upon arrival.
- Built-in in-app chat allows quick coordination at the pickup point.
**Priority**: High

### User Story 7
As a driver or passenger, I want to rate my carpool partner after each trip so that community trust and accountability remain high.
**Acceptance Criteria**:
- Both parties are prompted to submit a 1-to-5-star rating and optional feedback after the ride ends.
- Users with an average rating below 3.5 are flagged for administrative review.
- Aggregated ratings are visible on user profiles prior to ride confirmation.
**Priority**: High

### User Story 8
As a corporate commuter, I want an emergency SOS button and automated trip check-in during rides so that I feel safe commuting with colleagues.
**Acceptance Criteria**:
- An accessible SOS button is visible on the active ride screen at all times.
- Activating SOS shares live GPS coordinates with designated emergency contacts and corporate security.
- System sends a safety check-in prompt if a trip deviates significantly from the planned route.
**Priority**: High

### User Story 9
As a Company HR & Sustainability Administrator, I want to view an analytics dashboard of total CO₂ saved and active carpools so that I can generate corporate ESG reports.
**Acceptance Criteria**:
- Dashboard displays real-time metrics for total shared rides, distance saved, and CO₂ emissions reduced.
- Admin can filter statistics by department, office branch, and custom date ranges.
- Reports can be exported in CSV and PDF formats for annual sustainability audits.
**Priority**: Medium

### User Story 10
As a frequent carpooler, I want to earn eco-points and unlock priority office parking rewards so that I stay motivated to share rides consistently.
**Acceptance Criteria**:
- Users earn points for every completed shared commute based on distance and passenger count.
- A monthly company leaderboard highlights top eco-commuters and earned badges.
- Drivers reaching the monthly threshold automatically receive a digital pass for priority corporate parking.
**Priority**: Low
