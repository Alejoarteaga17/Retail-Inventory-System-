# Component Diagram

High-level component view of the Retail Inventory Management System for
Cornerline Home Goods.

Derived from [`statement-of-work-01.md`](../proposals/statement-of-work-01.md)
and [`discovery-and-scoping.md`](../discovery-and-scoping.md).

Components are grouped by **capability**, not by technology or by module: the
stack, the data model and several business rules are still open, so this view is
deliberately coarse and should survive those decisions. Components talk only
through interfaces — lollipop = provided, dashed arrow = required.

---

## 1. Notation

```mermaid
flowchart LR
    c["«component»<br/>Component"]
    i((IProvided))
    d["«component»<br/>Consumer"]
    f["Planned<br/>extension"]

    i --- c
    d -. "operation used" .-> i
    f -. "operation used" .-> i

    classDef iface fill:#ffffff,stroke:#555555,stroke-width:1px,color:#333333;
    classDef future fill:#ffffff,stroke:#999999,stroke-width:1px,stroke-dasharray:5 4,color:#666666;
    class i iface;
    class f future;
```

| Symbol | Meaning |
| --- | --- |
| `«component»` box | A capability of the system that can be built and replaced on its own |
| Circle | **Provided interface** — the contract the component exposes |
| Solid line circle—component | The component realizes that interface |
| Dashed arrow → circle | **Required interface** — a `«use»` dependency |
| Label on an arrow | The operation the consumer invokes, in short form |
| Dashed grey box | Out of MVP scope, planned for later |
| Cylinder | Persistent data store |

Realization lines carry no label: they say *"this component implements this
contract"*, not *"this component calls something"*.

---

## 2. Component diagram

```mermaid
flowchart TB
    staff["«actor»<br/>Store Staff"]
    mgr["«actor»<br/>Store Manager"]
    owner["«actor»<br/>Owner"]

    subgraph client["Client"]
        app["«component»<br/>Inventory Web App"]
    end

    subgraph services["Application services"]
        iapi((IInventoryApi))
        gateway["«component»<br/>API Gateway<br/><i>entry point + access enforcement</i>"]

        iinsights((IInsights))
        insights["«component»<br/>Inventory Insights<br/><i>low-stock alerts, dashboard, reports</i>"]

        icatalog((ICatalog))
        catalog["«component»<br/>Item Catalog<br/><i>items + reorder thresholds</i>"]

        istock((IStock))
        stock["«component»<br/>Stock Operations<br/><i>movements, quantities, history</i>"]

        iaccess((IAccessControl))
        access["«component»<br/>Access Control<br/><i>identity + RBAC</i>"]
    end

    subgraph data["Data"]
        istore((IInventoryStore))
        db[("Inventory Database")]
    end

    %% realization — written interface --- component so the layout
    %% ranks consumer -> interface -> provider from top to bottom
    iapi --- gateway
    iinsights --- insights
    icatalog --- catalog
    istock --- stock
    iaccess --- access
    istore --- db

    %% people
    staff -- "record stock" --> app
    mgr -- "review / approve" --> app
    owner -- "monitor" --> app

    %% dependencies — the label is the operation the consumer uses
    app -. "request" .-> iapi

    gateway -. "authorize" .-> iaccess
    gateway -. "get metrics" .-> iinsights
    gateway -. "get / edit items" .-> icatalog
    gateway -. "record / get movements" .-> istock

    insights -. "get thresholds" .-> icatalog
    insights -. "get quantities" .-> istock

    access -. "get users" .-> istore
    catalog -. "save items" .-> istore
    stock -. "save movements" .-> istore

    classDef iface fill:#ffffff,stroke:#555555,stroke-width:1px,color:#333333;
    class iapi,iinsights,icatalog,istock,iaccess,istore iface;
```

---

## 3. Interfaces

| Interface | Provided by | Contract |
| --- | --- | --- |
| `IInventoryApi` | API Gateway | Every operation the client can invoke |
| `IAccessControl` | Access Control | Authenticate a user; authorize an action for Store Staff / Store Manager / Owner |
| `ICatalog` | Item Catalog | Read and maintain items and their reorder thresholds |
| `IStock` | Stock Operations | Record a movement, read current quantities, read movement history |
| `IInsights` | Inventory Insights | Items below threshold, dashboard figures, low-stock report |
| `IInventoryStore` | Inventory Database | Transactional persistence |

---

## 4. Planned extensions

The SOW requires the architecture to accommodate work that is explicitly out of
MVP scope. Each of these attaches to an existing interface rather than forcing a
change to the components above — that is what the interfaces are protecting.

```mermaid
flowchart LR
    subgraph mvp["MVP"]
        icatalog((ICatalog))
        istock((IStock))
        iinsights((IInsights))
    end

    subgraph later["Planned for later"]
        barcode["Barcode scanning"]
        suppliers["Supplier management<br/>+ purchase orders"]
        accounting["Accounting integration"]
        notify["Email / SMS<br/>notifications"]
    end

    barcode -. "find item" .-> icatalog
    barcode -. "record movement" .-> istock
    suppliers -. "get items" .-> icatalog
    suppliers -. "get low stock" .-> iinsights
    accounting -. "export movements" .-> istock
    notify -. "get alerts" .-> iinsights

    classDef iface fill:#ffffff,stroke:#555555,stroke-width:1px,color:#333333;
    classDef future fill:#ffffff,stroke:#999999,stroke-width:1px,stroke-dasharray:5 4,color:#666666;
    class icatalog,istock,iinsights iface;
    class barcode,suppliers,accounting,notify future;
```

---

## 5. Notes

**Access is enforced once, at the gateway.** The SOW requires RBAC on *all*
inventory operations. Checking at the single entry point satisfies that without
making every capability depend on the security model.

**Stock Operations owns quantities; Item Catalog owns thresholds.** A quantity
may only change as the result of a recorded movement, which is what produces the
complete movement history and the negative-stock prevention the SOW requires.

**Insights reads, it does not write.** Alerts, dashboard and reports are derived
from `ICatalog` and `IStock`, so the dependency graph stays acyclic and a change
to the data model does not ripple into reporting.

**Open decisions that this view survives.** Whether the store and the storage
room track inventory separately, how thresholds are defined, and the exact
permissions per role all change the *inside* of a component — not the set of
components or the interfaces between them.

**Not shown.** The one-time migration of existing records is performed by
Cornerline Home Goods staff and is an activity, not a component. Deployment
topology (processes, hosts, protocols) belongs in a separate deployment diagram
once the stack is chosen in Phase 2.

---

## 6. Why `flowchart` and not `C4Component`

Mermaid's `C4Component` is documented as experimental, and GitHub's bundled
renderer does not include the C4 extension — such a block renders as raw text in
this repository. `architecture-beta` has the same problem. `flowchart` with
`subgraph` renders anywhere Mermaid is supported.

[UML component diagrams](https://www.uml-diagrams.org/component-diagrams-reference.html) ·
[Mermaid C4 (experimental)](https://mermaid.js.org/syntax/c4.html) ·
[GitHub C4 rendering discussion](https://github.com/orgs/community/discussions/197898)
