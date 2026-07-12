# Databricks Unity Catalog: Data Governance & PII Managed

This repository contains a hands-on exercise demonstrating advanced data governance, dynamic data masking, and cryptographic implementations within **Databricks Unity Catalog**. It simulates a healthcare data scenario to practice protecting sensitive PII data at the data layer.

> **Scope Note:** This exercise focuses entirely on **Data-Layer Security and Governance inside Unity Catalog** (such as Row-Level Filtering and Column Masking).

## 📘 Structure
```text
databricks-uc-data-governance/
├── 📄 .gitignore
├── 📘 README.md
└── 📂 notebooks/
    ├── ⚙️ _ddl.py
    ├── 🔢 1_catalog_sql_function.py
    ├── 🔑 2_catalog_cryptography_key.py
    ├── 🛡️ 3_catalog_column_masking_rlf.py
    └── 🏢 4_real_world_use.py
```

## 📁 Exercise Structure

* `notebooks/_ddl.py` - Sets up the base mock dataset for patient billing records (using simulated non-real PII data).
* `notebooks/1_catalog_sql_function.py` - Practices centralizing business logic using User-Defined Scalar and Table Functions in Unity Catalog.
* `notebooks/2_catalog_cryptography_key.py` - Exercises data hashing (SHA-256) and secure AES encryption using the Databricks Secrets SDK and ACL permissions.
* `notebooks/3_catalog_column_masking_rlf.py` - Implements dynamic column masking and Row-Level Filtering (RLF) natively attached to tables based on user context (`current_user()`, `is_member()`).
* `notebooks/4_real_world_use.py` - Simulates an real-world use case of automatic PII decryption for privileged admin groups using dynamic masks.

## 🚀 Technical Skills Practiced

* **Data Governance & Fine-Grained Access Control:** Implementing row and column-level inside Unity Catalog.
* **Dynamic Data Masking:** Writing reusable SQL masking policies linked to Databricks group memberships.
* **Row-Level Security :** Restricting data visibility dynamically so users can only view rows matching their identity contextualized by `current_user()`.
* **Secret Management:** Utilizing the `databricks.sdk` (WorkspaceClient) to create secret scopes, store cryptographic keys.
* **Distributed Cryptography:** Applying `aes_encrypt` and `aes_decrypt` alongside hashing functions (SHA-256, xxhash) within PySpark/SQL.
