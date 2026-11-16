# Customer-Churn-Analysis

## Table of contents
- [The problem we're solving.](#The problem we're solving.)
- [About the project and datasets.](#About the project and datasets.)

## The problem we're solving.

The problem we're trying to is to find out why subscribers of a fitness app [Peloton](https://www.onepeloton.com/) is cancelling their membership. 
In this project we are tasked with finding out leading factors for churning out and build a model to predict customers with high likelihood of churning.

### About the project and datasets. 
Both project description and both datasets where obtained through [Data Career School](https://www.datacareerschool.com/), a website to learn and practice Machine Learning and 
AI with contents like hands-on projects to build up your portfolio. More information about the project can be found [here](https://www.datacareerschool.com/datalabs/customer-churn-analysis).

#### About the datasets.
```diff
* subscriptions.csv — Customer records containing information about each customer's personal, account and subscription information. Contains 4200 records.
    * customer_id — A unique id assigned to each customer.
    * signup_date — The date the customer first signed up to join the fitness app, in 'YYYY-MM-DD' format
    * plan_type — Describes the subscription billing type is tied to the customer's account, either 'monthly' or 'annually'.
    * plan_tier — Shows which pricing model the customer's account is tied to, either 'basic', 'plus' or 'premium'.
    * monthly_price — Price the customer is billed for the subscriptions.
    * acquisition_channel — Information about how the customer was introduced to the fitness app.
    * primary_device — Devices the customer mostly uses to interact with the app.
    * age_group — Describes which age group the customer is in.
    * churned — Whether the customer's membership is still active or churned. 
    * churn_date — Date when customers churned in 'YYYY-MM-DD' format. Missing values for memberships that are still active.
    * cancel_reason — Customer's choice for churning out. Missing values for memberships that are still active. 

* usage.csv — Data about customer's visit to the gym on a monthly basis. Contains 30.685 records.
    * customer_id — Id tied to the customer going to the gym.
    * month — Date for when visit took place in 'YYYY-MM' format.
    * workouts_completed — Total number of workouts completed.
    * minutes_active — Total number of minutes spent in the gym per month.
    * classes_booked — Number of classes booked.
    * support_tickets — Number of support tickets created.
```
