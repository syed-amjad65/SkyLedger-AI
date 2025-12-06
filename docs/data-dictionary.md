# SkyLedger data dictionary

## Flights
- **PK:** FlightID
- **Fields:** flight_no, date, route, aircraft_type, seats, managed_capacity
- **Purpose:** Schedule and capacity backbone

## DemandSignals
- **PK:** SignalID
- **Fields:** dpd, bookings, daily_intakes, cancellations, no_show_rate
- **Purpose:** Demand telemetry & booking kinetics

## Revenue
- **PK:** RevenueID
- **Fields:** forecast_revenue, yield, rask, lf_target, class_mix
- **Purpose:** Yield/RASK tracking and targets

## Influences
- **PK:** InfluenceID
- **Fields:** event_type, route, start_date, end_date, influence_weight, notes
- **Purpose:** Holidays, disruptions, promos affecting demand

## OverbookingSettings
- **PK:** RuleID
- **Fields:** seats, bookings, no_show_rate, safety_buffer, overbooking_level, decrement_rate, risk_flag
- **Purpose:** Overbooking controls per route/aircraft

## InventoryControl
- **PK:** ControlID
- **Fields:** class_code, action_type, reason, dpd_band, min_yield, expiry_dpd, owner
- **Purpose:** Fare class open/close actions

## GroupsPolicy
- **PK:** GroupPolicyID
- **Fields:** route, season, target_ratio, holdback_seats, accepted_groups, review_date
- **Purpose:** Group allocation strategy

## PDDCorrections
- **PK:** CorrectionID
- **Fields:** actual_show_up, actual_no_show, denied_boarding, correction_notes
- **Purpose:** Price/day-of-departure correction audit

## AlertsLog
- **PK:** AlertID
- **Fields:** alert_type, root_cause, action_taken, owner, next_review
- **Purpose:** Exceptions and operational follow-up
