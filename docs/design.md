# Diagrams

## Architecture Diagram

<img width="973" height="722" alt="Diagrama sin título drawio" src="https://github.com/user-attachments/assets/b83f8953-901f-410b-b327-5c8cd3a16f7b" />

## Modelo de Datos

<img width="1251" height="654" alt="Untitled (2)" src="https://github.com/user-attachments/assets/9d05c7d7-298a-41e5-836b-449de62e0221" />



## Component diagram

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



# dsd

https://www.figma.com/make/flrV3EonGBeck7xceHvUca/Furniture-Inventory-Dashboard-Design?fullscreen=1&t=pX2k4jXAPjgFipS5-1&code-node-id=0-6

![alt text](image.png)

![alt text](image-1.png)
![alt text](image-2.png)