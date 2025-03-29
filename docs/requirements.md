# Requirements

## 1. Introduction
This document outlines the functional and non-functional requirements for a fullstack inventory and cash management system built with Django (Python).

## 2. Functional Requirements

### 2.1 Inventory Management
- **FR1.1**: The system shall allow authorized users to add new items to inventory
- **FR1.2**: The system shall allow authorized users to update existing item details
- **FR1.3**: The system shall allow authorized users to delete items from inventory
- **FR1.4**: The system shall display real-time item availability status

### 2.2 Cash Flow Management
- **FR2.1**: The system shall record opening cash amount at start of day
- **FR2.2**: The system shall record closing cash amount at end of day
- **FR2.3**: The system shall calculate and display current balance (incomes - outcomes)
- **FR2.4**: The system shall provide quick calculation of change (order total - received cash)
- **FR2.5**: The system shall record payment method (cash, MBWay, bank transfer)

### 2.3 Order Management
- **FR3.1**: The system shall generate unique order IDs/codes for each costumer
- **FR3.2**: The system shall allow adding/removing items to/from specific orders
- **FR3.3**: The system shall allow updating order item status (ordered, delivered)
- **FR3.4**: The system shall allow enabling/disabling orders
- **FR3.5**: The system shall display order history and details

### 2.4 User Management
- **FR4.1**: The system shall authenticate staff users before allowing modifications
- **FR4.2**: The system shall provide consumer access to view orders by ID/number/code
- **FR4.3**: The system shall maintain different permission levels for staff roles

### 2.5 Audit Logging
- **FR5.1**: The system shall maintain a complete log of all system actions
- **FR5.2**: The system shall record timestamp, user, and action details for each event

## 3. Non-Functional Requirements

### 3.1 System Architecture
- **NFR1.1**: The system shall operate within a local network environment
- **NFR1.2**: The system shall be accessible via web browser on both mobile and desktop devices

### 3.2 Performance
- **NFR2.1**: The system shall respond to user actions within 2 seconds for typical operations
- **NFR2.2**: The system shall support concurrent access by multiple users

### 3.3 Security
- **NFR3.1**: All sensitive data transmissions shall be encrypted
- **NFR3.2**: User passwords shall be stored using secure hashing algorithms
- **NFR3.3**: The system shall implement CSRF protection

### 3.4 Usability
- **NFR4.1**: The interface shall be responsive and adapt to mobile/desktop screens
- **NFR4.2**: Common operations shall be achievable in 3 clicks or less
- **NFR4.3**: The system shall provide clear feedback for user actions

### 3.5 Reliability
- **NFR5.1**: The system shall maintain data integrity during power outages
- **NFR5.2**: The system shall automatically backup data daily

### 3.6 Compatibility
- **NFR6.1**: The system shall support modern browsers (Chrome, Firefox, Edge, Safari)
- **NFR6.2**: The system shall be compatible with Python 3.8+ and Django 4.0+

## 4. Future Considerations
- Integration with accounting software
- Barcode scanning support
- Advanced reporting features
- Multi-language support
