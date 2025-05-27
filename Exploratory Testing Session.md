# task1 - Exploratory Testing Session Report by Anam Siddiquee

**Application Name:** Monefy – Money Manager  
**Date & Time:** 3/16/2025  
**Platform:** Android  
**Device & OS Version:** Pixel 6  
**App Version:** Baklava , version 16  
**Tester:** Anam Siddiquee 

---

## Testing  Charter (Mission)

**Objective:**  
Explore the **key functionalities** of the Monefy app, focusing on usability, accuracy, performance, and security. Identify potential bugs, inconsistencies, or user experience issues.  

**Scope:**  
- Expense & Income Tracking  
- Multi-Currency Handling  
- Budgeting & Reports  
- Data Synchronization & Backup  
- Security & Authentication  
- UI/UX & Accessibility  

---

## Test Scenarios & Observations

###  1. Installation & First-Time Setup
 **Steps Performed:**
1. Installed the app from google
2. Launched the app and observed the onboarding experience.
3. Verified the default currency settings and setup process.

 **Issues Found:**
- Currency selection is not asked by user during onboarding, the offer screen causes confusion. 

 **Suggestions:**
- User does not have any option to skip / decline notifications on the app itself.
- Currencies option is not intuitive, although user can change the desired currency later in settings

---

###  2. Test Adding Income 
 **Steps Performed:**
1. Enter add income section by clicking on Income button
2. Entered value and perform addition (negative values, special characters, and very large numbers).
3. Added note to transaction.
4. Chose category for the added Income

---

###  3. Test Adding  expenses
 **Steps Performed:**
1. Enter add expenses section by clicking on expense button
2. Entered value and perform addition (negative values, special characters, and very large numbers).
3. Added note to transaction.
4. Chose category for the added expense

 **Issues Found:**
- [[Bug]:"App allows negative values in expenses, which might cause incorrect balance calculations."]

---

###  4. Test to edit date in the transaction
 **Steps Performed:**
1. Added transactions in Expense and incomes.
2. Checked for automatic exchange rate updates.
3. Changed the date for transaction to a past date. (Put fraction figures)
4. Save transaction with any category

**Issues Found:**
-[[Bug]:"App allows years to be entered in fractions and decimals"]

---

###  5. Test for UI/UX & Performance
 **Steps Performed:**
1. Tested dark mode and accessibility features.
2. Navigated through menus and checked for responsiveness.
3. Rotated the device (portrait/landscape) and checked UI consistency.
4. Added a large number of transactions to test performance.
5. Tested User experience for welcome process

---

## Summary of Findings

 **Number of Bugs Found:** [2]  
 **Severity of Issues:**  
   - **Critical:** [1]  
   - **Major:** [1]  
   - **Minor:** [X]  

---

 **Further Testing:**  
- Perform testing on different devices with different aspect ratios to check consistency.  
- Conduct stress testing by adding a high volume of income and expenditure transactions
- Validate app behavior over extended use long running sessions to check memory leakage and performance issues.  

---

## Prioritization of testing charters
When it comes to prioritizing charters, my first focus is on UI/UX testing. Because before diving into the app's functionality, it's crucial to ensure that the user interface is visually appealing and is user-friendly. The UI is what customers interact with, and it gives them their first impression of the product’s quality. 

After the UI/UX, I move on to functional testing. This step is all about making sure that each part of the app works as intended and serves its purpose. For example, I test features like adding new expenses, managing income, applying filters, creating categories, and other core functionalities to ensure the app performs seamlessly.

Finally, after confirming the UI and functionality are working as expected, I shift focus to integration testing. This phase involves checking the communication between the front end and the back end, ensuring everything is well-connected and operates smoothly together.

---

## Time Planned for Each Charter
Allocated 30 minutes per test charter. Approach is to spend short bursts of time within this hour doing ad-hoc exploratory testing for each feature. Instead of focusing on specific test cases, I’ll explore the application freely, getting a feel for how it works from end to end. Along the way, I’ll report any issues I come across.

---
