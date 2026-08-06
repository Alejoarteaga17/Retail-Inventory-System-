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
