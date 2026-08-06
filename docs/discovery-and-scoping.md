# Discovery & Scoping

## 1. Scope Questionnaire

### Inventory

1. What type of inventory will the system manage?
2. What types of users will use the system on a daily basis?
3. What rules should determine when a low-stock alert is triggered?
4. What level of access should each user type have?
5. What information should be recorded for each inventory item?
6. What security restrictions or system limitations should we consider?
7. How should stock movements be recorded and displayed?

---

## 2. MVP Scope

### In Scope

* Create inventory items
* Update inventory information
* Record stock-in transactions
* Record stock-out transactions
* Record manual stock adjustments
* View current inventory quantities
* View stock movement history
* Display low-stock alerts
* Provide a basic inventory dashboard

### Out of Scope

* POS functionality
* Accounting features
* Barcode scanner integration
* E-commerce integration

### Planned for Later

* Supplier management
* Automatic purchase order generation
* Email or SMS notifications for low-stock items

### Open Questions

* Do different user types require different permission levels?
* Should the store and storage room track inventory separately?

---

# 3. Project Schedule

## Phase 1: Foundation and System Setup

**Period:** July 23, 2026 to August 30, 2026
**Duration:** Approximately 5.5 weeks

### Objective

Establish the technical architecture, domain model, database schema, and security foundation required to support the core inventory management system.

### Deliverables

* Software architecture and database schema design
* Development environment setup

  * Repository
  * CI/CD pipeline
  * Staging environment
* User authentication
* Role-Based Access Control (RBAC)
* Item catalog management

  * Product CRUD
  * Category CRUD

### Dependencies

* Project kickoff
* Initial requirements approval

---

## Phase 2: Requirements and UX Design

**Period:** August 3, 2026 to August 12, 2026
**Duration:** Approximately 1.5 weeks

### Objective

Define the detailed user stories, inventory business rules, system architecture, and data model required for implementation.

### Deliverables

* User stories
* Acceptance criteria
* Inventory business rules
* Data model draft
* System architecture definition
* UX requirements

### Dependencies

* Phase 1 outputs
* Discovery answers

---

## Phase 3: Foundation and Core Catalog

**Period:** August 13, 2026 to August 30, 2026
**Duration:** Approximately 2.5 weeks

### Objective

Build the technical foundation, authentication framework, and core inventory catalog functionality.

### Deliverables

* RBAC module
* Item catalog CRUD
* Product management
* Category management
* Database schema implementation
* CI/CD pipeline setup

### Dependencies

* Approved Phase 2 scope
* Approved data model

---

## Phase 4: Inventory Operations

**Period:** August 31, 2026 to September 30, 2026
**Duration:** Approximately 4.5 weeks

### Objective

Implement the core inventory operations required to record stock entries, stock removals, and manual adjustments safely and accurately.

### Deliverables

* Stock movement management

  * `STOCK_IN`
  * `STOCK_OUT`
  * `ADJUSTMENT`
* Inventory quantity management
* Concurrency controls
* Negative stock validation
* Negative stock approval workflow
* Stock movement audit history
* Interim progress report
* Mid-semester checkpoint demo

### Dependencies

* Completion of the core foundation
* Active item catalog
* Active database schema

---

## Phase 5: Inventory Monitoring and Intelligence

**Period:** October 1, 2026 to October 30, 2026
**Duration:** Approximately 4.5 weeks

### Objective

Provide management with better visibility into inventory levels, stock movements, low-stock conditions, and key inventory metrics.

### Deliverables

* Real-time low-stock alerts
* Executive inventory dashboard

  * Stock summaries
  * Movement metrics
* Inventory reporting module
* PDF export
* CSV export

### Dependencies

* Stock movement functionality must be operational
* Stock movement history must be available
* Inventory data must be reliable

---

## Phase 6: Quality Assurance and Final Delivery

**Period:** October 31, 2026 to November 15, 2026
**Duration:** Approximately 2.5 weeks

### Objective

Complete end-to-end testing, user acceptance testing, documentation, production deployment, and final project handover to Cornerline Home Goods.

### Deliverables

* End-to-end (E2E) testing
* Bug identification and resolution
* QA report
* User acceptance testing
* System user manual
* Technical documentation in `/docs`
* Final production deployment
* Final system verification
* Project sign-off and handover

### Dependencies

* All MVP features must be complete
* System must be ready for end-to-end testing

## 4. Risks, Assumptions, and Dependencies

### 1. Risks

| Risk                                                                         | Impact                                                                                       | Mitigation                                                                                            |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Staff may find the inventory system difficult to use.                        | Low adoption and continued use of manual records, spreadsheets, or WhatsApp.                 | Keep the interface simple, test the main workflows with staff, and provide a short onboarding guide.  |
| Inventory business rules may be unclear.                                     | Incorrect stock calculations, inconsistent inventory records, or unexpected system behavior. | Confirm inventory rules, stock thresholds, adjustment rules, and approval workflows during discovery. |
| Scope may grow beyond the MVP.                                               | Project delays and unfinished core functionality.                                            | Clearly separate features into IN, OUT, LATER, and UNKNOWN scope.                                     |
| Staff may enter incorrect stock movements.                                   | Inventory quantities may become inaccurate.                                                  | Use validation rules, clear movement types, required reasons, and an audit history for all changes.   |
| Negative stock may be handled incorrectly.                                   | Inventory records may become inconsistent or misleading.                                     | Prevent negative stock by default and require manager approval for exceptional cases.                 |
| Store and storage room inventory requirements may change during development. | Changes to the data model and inventory logic may increase development effort.               | Confirm whether inventory locations need to be tracked separately before finalizing the data model.   |
| Low-stock thresholds may not be clearly defined.                             | Incorrect or ineffective low-stock alerts.                                                   | Define how thresholds are determined and whether they are set per product during discovery.           |
| Multiple users may modify the same inventory item at the same time.          | Race conditions or incorrect inventory quantities.                                           | Implement concurrency controls and transactional stock updates.                                       |
| Inventory movement history may be incomplete or inaccurate.                  | Management may not be able to understand why stock changed.                                  | Record every stock movement with the product, quantity, type, date, user, and reason.                 |

---

### 2. Assumptions

| Assumption                                                                            | Why It Matters                                                                             |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Staff will manually record stock-in, stock-out, and adjustment transactions.          | Avoids the need for barcode scanners or other automated inventory integrations in the MVP. |
| The MVP does not require POS functionality.                                           | Keeps the project focused on inventory management rather than sales processing.            |
| The MVP does not require accounting functionality.                                    | Avoids introducing financial and accounting workflows outside the project scope.           |
| The MVP does not require e-commerce integration or payment processing.                | Keeps the system aligned with the current inventory management requirements.               |
| Staff, Managers, and Owners are the main system users.                                | Defines the initial authentication and authorization model.                                |
| All inventory movements should be recorded in the system.                             | Provides an audit trail and allows management to understand changes in stock levels.       |
| Negative stock should not be allowed without manager approval.                        | Protects inventory accuracy while allowing controlled exceptions.                          |
| A dashboard and movement history are sufficient for the initial reporting needs.      | Avoids building a more complex reporting system for the MVP.                               |
| Low-stock alerts will be based on a defined stock threshold.                          | Provides a clear rule for identifying products that require attention.                     |
| Product and inventory information will be entered and maintained by authorized users. | Reduces the need for external product catalog integrations in the MVP.                     |

---

### 3. Dependencies and Pending Decisions

| Dependency or Decision                                                                                                                | Owner                 |
| ------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Confirm whether the MVP should support one inventory location or separate inventory for the store and storage room.                   | Client / Project Team |
| Confirm the exact capacity and behavior of each inventory location, if multiple locations are required.                               | Client / Project Team |
| Confirm how low-stock thresholds should be defined and maintained.                                                                    | Client / Manager      |
| Confirm the exact permissions for Staff, Manager, and Owner roles.                                                                    | Client / Project Team |
| Confirm the workflow for requesting and approving negative stock adjustments.                                                         | Client / Manager      |
| Confirm the required product fields for the MVP.                                                                                      | Client / Project Team |
| Confirm the required fields for stock movement records.                                                                               | Client / Project Team |
| Confirm whether inventory adjustments require a reason in all cases.                                                                  | Client / Manager      |
| Confirm whether Managers and Owners should have identical administrative permissions.                                                 | Client / Project Team |
| Confirm the dashboard metrics and inventory reports required for the MVP.                                                             | Client / Project Team |
| Confirm whether identifying popular products based on stock movements is required in the MVP or should be considered a later feature. | Client / Project Team |
| Confirm the expected number of users and whether multiple users may perform inventory operations concurrently.                        | Client / Project Team |
