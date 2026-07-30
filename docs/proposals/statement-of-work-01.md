# Statement Of Work

- [Statement](#statement)
  - [Title](#title)
  - [Abstract](#abstract)
  - [Value](#value)
  - [Scope](#scope)
  - [Payment](#payment)
- [Purpose](#purpose)
  - [Objectives](#objectives)
  - [Performance](#performance)
- [Who Does What](#who-does-what)
  - [People](#people)
  - [Roles](#roles)
  - [Responsibilities](#responsibilities)
- [Context](#context)
  - [Present](#present)
  - [Future](#future)
- [Planning](#planning)
  - [Requirements](#requirements)
- [Other Terms and Conditions](#other-terms-and-conditions)
  - [Client's Obligations](#clients-obligations)
- [Schedule](#schedule)
  - [Expected Start Date and Completion Date](#expected-start-date-and-completion-date)
  - [Sign-off](#sign-off)

---

# Statement

## Title

# Retail Inventory Management System

---

## Abstract

This Statement of Work (SOW) outlines the objectives, scope, deliverables, and timelines for the development and implementation of a new Retail Inventory Management System for **Cornerline Home Goods**.

The project aims to replace the company's manual inventory process, reducing human error, improving inventory accuracy, preventing stock shortages, and providing real-time inventory visibility. **Software Solutions SAS** will be responsible for designing, developing, deploying, documenting, and supporting the system, while Cornerline Home Goods will perform the data migration using its own staff.

---

## Value

The total project value is currently **pending negotiation**.

The estimated value of this project covers the design, development, customization, deployment, maintenance, user training, and post-implementation support for the inventory management system. Payments will be made according to project milestones to ensure alignment with the successful completion of each phase.

The budget also includes software configuration, system documentation, testing, technical support, and maintenance during the first year after deployment.

> [!NOTE]
> On **July 23, 2026**, **Cornerline Home Goods** agreed that the data migration process will be performed by its own staff. Therefore, the labor cost associated with data migration is excluded from this proposal and will be covered by the client.

---

## Scope

The project includes the design, development, deployment, documentation, and support of a Retail Inventory Management System.

The scope includes:

- Item catalog management.
- Real-time inventory quantity tracking.
- Stock-in and stock-out transaction management.
- Inventory adjustment history.
- Low-stock alerts.
- Inventory dashboard.
- Low-stock reporting.
- User authentication with role-based access (Store Staff, Store Manager, and Owner).
- User guide and technical documentation.
- User training.
- One year of post-deployment maintenance.

---

## Payment

The total project cost is currently pending negotiation.

Unless otherwise agreed, payments will be divided into the following milestones:

- 20% upon contract signing.
- 30% upon completion and approval of the system design.
- 30% upon successful completion of development and testing.
- 20% upon deployment, user training, and final project acceptance.

Payments shall be made via bank transfer within fifteen (15) calendar days after invoice submission.

Any work requested outside the agreed project scope will require written approval from both parties and will be billed separately.

---

# Purpose

## Objectives

The primary objective of this project is to design, develop, and implement a Retail Inventory Management System that enables Cornerline Home Goods to efficiently manage inventory records, stock movements, current inventory levels, and reorder alerts.

Upon completion, the project will deliver:

- A centralized inventory management system.
- Accurate real-time inventory tracking.
- Automated low-stock alerts.
- Inventory movement history.
- Role-based access control.
- Administrative dashboards for inventory visibility.
- User documentation and training.
- Post-deployment technical support.

The new system will improve operational efficiency, reduce inventory inaccuracies, and support better business decision-making.

---

## Performance

### Business Performance Metrics

1. **Data Migration Rate:** At least 98% of inventory records shall be successfully migrated to the new system.

2. **Inventory Accuracy:** Inventory discrepancies should be reduced by at least 90% compared to the current manual process.

3. **Net Revenue Impact:** The system should contribute to increased sales by reducing stock shortages and improving inventory availability.

### System Performance Metrics

1. **System Availability (Uptime):**
   - Minimum 99.9% uptime during business operations.

2. **Data Accuracy:**
   - Inventory quantities and stock movements must always reflect the correct values.

3. **User Adoption:**
   - 100% of employees currently using the manual inventory process should transition to the new system.

4. **Response Time:**
   - Inventory updates performed within the application should be reflected in one (1) second or less.

---

# Who Does What

## People

The project involves the following stakeholders:

- Store Staff
- Store Manager
- Owner
- Software Solutions SAS (Development Team)

---

## Roles

### Store Staff

- Register stock entries and exits.
- Update product information.
- Perform inventory adjustments within assigned permissions.

### Store Manager

- Supervise inventory operations.
- Review reports and inventory movements.
- Manage store inventory.
- Monitor employee activities.

### Owner

- Full system access.
- View business dashboards.
- Monitor inventory performance.
- Manage users and system settings.

### Software Solutions SAS

- System analysis.
- System design.
- Software development.
- Testing.
- Deployment.
- User training.
- Technical support.
- Maintenance.

---

## Responsibilities

| Task | Store Staff | Store Manager | Owner | Software Solutions SAS |
|------|-------------|---------------|--------|------------------------|
| Define business requirements | C | R | A | R |
| Provide inventory data | R | A | C | I |
| Data migration | R | A | I | C |
| System analysis | I | C | C | R/A |
| Software development | I | I | C | R/A |
| Testing | R | A | C | R |
| Deployment | I | C | C | R/A |
| User training | R | R | C | A |
| Final approval | I | C | A | C |

**Legend**

- **R** = Responsible
- **A** = Accountable
- **C** = Consulted
- **I** = Informed

---

# Context

## Present

Cornerline Home Goods currently manages inventory through manual processes, resulting in inaccurate inventory records, delayed stock updates, human errors, and limited visibility of inventory levels.

These issues frequently lead to stock shortages, unnecessary purchases, and inefficient inventory management.

---

## Future

The new inventory management system will centralize inventory operations and provide real-time visibility into stock levels, inventory movements, and reorder alerts.

The solution will improve operational efficiency, reduce inventory discrepancies, and provide management with dashboards that support better business decisions.

The system should also support future enhancements such as barcode scanning, supplier management, purchase orders, and integration with accounting software if required.

---

# Planning

## Requirements

### Functional Requirements

#### Inventory Item Management

- The system shall allow users to create, update, view, and deactivate inventory items.
- The system shall maintain an item catalog containing, at minimum, an item identifier, name, current quantity, and reorder threshold.
- The system shall display the current inventory quantity for each item.
- The system shall validate all required input fields before processing inventory item requests.

#### Stock Movement Management

- The system shall allow users to record stock-in transactions.
- The system shall allow users to record stock-out transactions.
- The system shall allow authorized users to perform manual inventory adjustments.
- The system shall automatically update inventory quantities after every stock movement.
- The system shall prevent inventory quantities from becoming negative.
- The system shall prevent inventory movements for non-existent inventory items.

#### Inventory Movement History

- The system shall maintain a complete history of all inventory movements.
- The system shall record the movement type, quantity, timestamp, affected inventory item, and user responsible for each inventory movement.
- The system shall allow users to view the inventory movement history for individual inventory items.

#### Low Stock Alerts

- The system shall automatically detect when an inventory item's quantity reaches or falls below its configured reorder threshold.
- The system shall notify users of low-stock inventory items.
- The system shall display low-stock alerts within the application.

#### Inventory Dashboard and Reporting

- The system shall provide an inventory dashboard displaying current inventory information.
- The system shall provide a dashboard highlighting inventory items with low stock.
- The system shall generate low-stock reports.

#### Authentication and Authorization

- The system shall require user authentication before allowing access.
- The system shall support the following user roles:
  - Store Staff
  - Store Manager
  - Owner
- The system shall enforce role-based access control (RBAC) for all inventory operations.

#### Documentation and Training

- The project shall include a user guide.
- The project shall include technical documentation.
- The project shall include user training before project acceptance.

#### Support and Maintenance

- The project shall include one year of post-deployment maintenance and technical support.

---

### Non-Functional Requirements

#### Performance

- Inventory updates shall be reflected within one (1) second or less.
- The system shall provide real-time inventory visibility.

#### Availability

- The system shall maintain at least 99.9% availability during business operations.

#### Security

- Only authenticated users shall access the system.
- Inventory operations shall follow role-based permissions.

#### Reliability

- Inventory quantities shall remain accurate after every transaction.
- The system shall prevent invalid inventory operations.

#### Maintainability

- The project shall include technical documentation.
- Core functionality shall be covered by automated tests.

#### Scalability

- The system shall support future integration with barcode scanning.
- The system shall support future supplier management.
- The system shall support future accounting system integration.

---

### Business Requirements

- The system shall replace the client's manual inventory process.
- The system shall provide centralized inventory management.
- The system shall reduce inventory discrepancies.
- The system shall reduce stock shortages.
- The system shall improve inventory visibility.
- The system shall support better business decision-making through dashboards and reports.

---

### Constraints

- Data migration shall be performed by the client.
- Barcode scanning is outside the scope of the initial implementation.
- Supplier management is outside the scope of the initial implementation.
- Purchase order management is outside the scope of the initial implementation.
- Accounting system integration is outside the scope of the initial implementation.

---

# Other Terms and Conditions

## Client's Obligations

The client agrees to:

- Provide complete and accurate inventory information before development begins.
- Assign a project representative as the primary point of contact.
- Ensure the availability of staff for meetings, testing, training, and project validation.
- Perform the data migration process using their own personnel.
- Provide timely feedback and approval of project deliverables.
- Provide access to existing documentation, business procedures, and operational information required for development.
- Ensure the required hardware, internet connection, and local infrastructure are available before deployment.
- Submit any requested changes to the project scope through a formal change request.

---

# Schedule

## Expected Start Date and Completion Date

**Pending**

---

## Sign-off

**NOTE:** Before signing this Statement of Work, if either party has any questions or concerns, they should discuss them before execution of this agreement.

By signing below, both parties acknowledge that they understand and accept the scope, responsibilities, terms, and conditions described in this Statement of Work.

### Printed Name

__________________________________________

### Signature

__________________________________________

### Date

__________________________________________
