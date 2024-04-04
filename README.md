# Hotel-Booking-analysis-using-python


## Overview

This project aims to analyze hotel booking data for both city hotels and resort hotels. The dataset used for this analysis contains information about bookings, including booking dates, hotel type, guest demographics, and booking cancellations.

## Dataset

The dataset used for this analysis is provided in the file `hotel_bookings.csv`. It contains the following columns:

- `hotel`: Type of hotel (City Hotel or Resort Hotel)
- `is_canceled`: Whether the booking was canceled (0 = not canceled, 1 = canceled)
- `lead_time`: Number of days between booking date and arrival date
- `arrival_date_year`: Year of arrival date
- `arrival_date_month`: Month of arrival date
- `arrival_date_day_of_month`: Day of the month of arrival date
- `stays_in_weekend_nights`: Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel
- `stays_in_week_nights`: Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel
- `adults`: Number of adults
- `children`: Number of children
- `babies`: Number of babies
- `meal`: Type of meal booked
- `country`: Country of origin
- `market_segment`: Market segment designation
- `distribution_channel`: Booking distribution channel
- `is_repeated_guest`: Whether the booking is from a repeated guest (0 = first-time booking, 1 = repeated booking)
- `previous_cancellations`: Number of previous bookings that were canceled by the guest
- `previous_bookings_not_canceled`: Number of previous bookings that were not canceled by the guest
- `reserved_room_type`: Type of room reserved
- `assigned_room_type`: Type of room assigned
- `booking_changes`: Number of changes/amendments made to the booking
- `deposit_type`: Type of deposit made for the booking
- `agent`: ID of the travel agency
- `company`: ID of the company/entity that made the booking
- `days_in_waiting_list`: Number of days the booking was in the waiting list
- `customer_type`: Type of booking
- `adr`: Average daily rate (price)
- `required_car_parking_spaces`: Number of car parking spaces required by the guest
- `total_of_special_requests`: Number of special requests made by the guest
- `reservation_status`: Reservation last status (Canceled, Check-Out, No-Show)
- `reservation_status_date`: Date at which the last status was set

## Analysis

The analysis of the hotel booking data includes the following aspects:

1. **Exploratory Data Analysis (EDA)**:
   - Understanding the distribution of various parameters such as lead time, booking cancellations, guest demographics, and booking trends over time.
   - Identifying patterns and trends specific to city hotels and resort hotels.

2. **Booking Patterns**:
   - Analyzing booking patterns based on lead time, booking channel, customer type, and market segment.
   - Examining the impact of different factors on booking cancellations.

3. **Revenue Analysis**:
   - Investigating average daily rates (ADR) for both city hotels and resort hotels.
   - Identifying peak booking periods and pricing strategies.

4. **Customer Segmentation**:
   - Segmenting guests based on demographics, booking behavior, and special requests.
   - Understanding the preferences and needs of different guest segments.

5. **Predictive Modeling (Optional)**:
   - Building predictive models to forecast booking cancellations or demand for hotel rooms.
   - Evaluating model performance and identifying key predictors.

## Tools Used

The analysis is performed using Python programming language and various libraries including:

- Pandas: Data manipulation and analysis
- Matplotlib and Seaborn: Data visualization
- Scikit-learn: Machine learning models (if applicable)

## Usage

To reproduce the analysis:

1. Clone this repository to your local machine.
2. Ensure you have Python and necessary libraries installed.
3. Run the Jupyter Notebook `hotel_booking_analysis.ipynb`.
4. Follow the step-by-step instructions in the notebook to execute the analysis.

## Conclusion

The analysis provides valuable insights into hotel booking trends, customer behavior, and revenue optimization strategies for both city hotels and resort hotels. Understanding these patterns can help hotel management make informed decisions to improve guest experience and maximize revenue.

---

Feel free to customize this README template based on your specific project details and findings.
