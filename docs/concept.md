# Inventory and Cash Management System - Concepts Explanation

## 1. Core System Concepts

### 1.1 Inventory Management
- **Item**: A product or service tracked in the system, with attributes like name, description, quantity, price, and status.
- **Availability Control**: Real-time tracking of stock levels, automatically updated when items are added to orders or restocked.
- **CRUD Operations**: Create, Read, Update, Delete - the four basic functions for persistent storage of item data.

### 1.2 Cash Flow Components
- **Register**: Virtual representation of a physical cash drawer with opening/closing amounts.
- **Transaction Types**:
  - *Income*: Money entering the system (sales, deposits)
  - *Outcome*: Money leaving the system (refunds, withdrawals)
- **Payment Methods**:
  - *Cash*: Physical currency transactions
  - *MBWay*: Portuguese mobile payment service
  - *Bank Transfer*: Electronic funds transfer

### 1.3 Order Lifecycle
- **Order Status Flow**:
- Created → Items Added → Processing → Completed/Canceled

Copy
- **Order Items**: Individual products/services within an order with their own status (ordered/delivered)
- **Order ID**: Unique identifier (could be sequential number, UUID, or custom format)

## 2. User Types and Permissions

| User Type       | Capabilities                              | Restrictions                  |
|-----------------|------------------------------------------|-------------------------------|
| Admin           | Full system access                       | None                          |
| Staff           | Manage inventory, process orders        | Cannot modify user accounts   |
| Cashier         | Handle transactions, basic order ops    | Limited inventory changes     |
| Consumer        | View order status by ID                 | Read-only access              |

## 3. Technical Concepts

### 3.1 System Architecture
- **Client-Server Model**: Browser (client) ↔ Django Application (server) ↔ Database
- **Local Network Operation**: System runs on an internal network without requiring internet access

### 3.2 Data Management
- **Audit Log**: Immutable record of all significant actions containing:
- Timestamp (ISO 8601 format)
- User who performed action
- Action type (create/update/delete)
- Affected entity
- Before/after values (for modifications)

### 3.3 Security Concepts
- **Authentication**: Process of verifying user identity (username/password)
- **Authorization**: Determining what authenticated users are permitted to do
- **CSRF Protection**: Security measure that prevents unauthorized commands from being executed

## 4. Key Processes

### 4.1 Daily Cash Management
1. Opening balance recorded
2. Transactions processed throughout day
3. Reconciliation:
 - System calculates expected cash
 - User enters actual cash
 - Discrepancies flagged

### 4.2 Order Processing Workflow
1. Order created with unique ID
2. Items added to order
3. Payment method selected
4. Transaction completed
5. Items marked as delivered when fulfilled

## 5. Glossary

- **MBWay**: A Portuguese mobile payment solution allowing transfers via phone number
- **CRUD**: Acronym for Create, Read, Update, Delete - fundamental data operations
- **UUID**: Universally Unique Identifier - a 128-bit number used to identify information
- **CSRF**: Cross-Site Request Forgery - a type of malicious exploit
- **Responsive Design**: Approach where design adapts to different screen sizes
