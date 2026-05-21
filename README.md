# 🇩🇪 International Student Transition & Career Intelligence Platform

A production-grade, modular backend and data engineering platform built to navigate the unique complexities of moving to Germany as an international student. This platform streamlines the end-to-end lifecycle—from initial university enrollment and mandatory German bureaucracy tracking to landing corporate *Werkstudent* roles and full-time careers.

This system is built iteratively, evolving from a simple Python Command Line Interface (CLI) executing raw relational database queries into an automated data analytics pipeline and decoupled REST API backend.

---

## 🗺️ System Architecture & Data Workflow Diagram

📥 **[Click here to see the full ERD diagram](./docs/erd_diagram.jpg)** 
📄 **[Click here to see the Master Technology & Learning Roadmap PDF](./docs/International_Student_Platform_Tech_Roadmap.pdf)**

1. **Ingress Layer:** Student demographic records, mandatory documents (Visa, Anmeldung), and job applications enter through a Python CLI.
2. **Business & Validation Layer:** Python checks rules (e.g., age limits, country-specific document requirements, specific corporate deadlines) before passing data to the database.
3. **Storage Engine Layer:** PostgreSQL manages relational integrity, utilizing strict schemas, indexes, and database rules to protect student records.

---

## 🛠️ Modular Project Blueprint (The 1, 2, 3 Strategy)

Every operational module in this system is built using a strict, step-by-step evolution model:
* **Level .0 (Raw Core):** Pure, linear Python script execution using raw SQL statements to make features work immediately.
* **Level .1 (Safety Net):** Upgrading the core logic with tight `try/except` safety blocks to catch database offline or configuration issues.
* **Level .2 (Abstraction):** Wrapping the code into clean, reusable Python functions and building interactive, error-free CLI menus.

### 🗂️ Module A: The Student Layer (Current Module)
* **Goal:** Model student profiles, capture demographics, track dates of birth, and record countries of origin to customize bureaucratic workflows automatically.
* **SQL Focus:** `CREATE TABLE`, basic `INSERT`, and linear `SELECT` statements.

### 📂 Module B: The Document Lookup Directory
* **Goal:** Track complex paperwork types required in Germany (e.g., 'Admission Letter', 'Anmeldung/City Registration', 'Blocked Account Confirmation', 'Health Insurance Proof').
* **SQL Focus:** Text checking and validation constraints (`CHECK` rules) to separate documents into 'University', 'Relocation', and 'Career' categories.

### 🏢 Module C: The Corporate & Job Market Layer
* **Goal:** Build directories tracking companies matching student-friendly profiles and job positions filtering specifically by salary thresholds, location, and language requirements.
* **SQL Focus:** Primary keys, foreign keys, and relational mapping between companies and job IDs.

### 📊 Module D: The Application Junction Matrix
* **Goal:** Connect students directly to their job hunt timelines and document checklists. Track communication dates, interview stages, and upload statuses.
* **SQL Focus:** Junction tables, deep relational `JOIN` operations, and data group processing (`GROUP BY`).

---

## 📈 Long-Term Engineering Evolution Roadmap

### Phase 2: Refactoring & Architecture Professionalization
* Extract repetitive script components into centralized database transaction drivers.
* Establish global existence validators (e.g., preventing duplicate emails or conflicting document uploads).

### Phase 3: Deep Analytical SQL Engines
* Construct complex dashboard queries evaluating student visa timelines, application pass-rates, and market salary metrics.
* Optimize database access patterns using Common Table Expressions (CTEs), Views, and targeted Indexes.

### Phase 4: Pandas Data Engineering Pipeline
* Create extraction, transformation, and loading (ETL) automation pathways.
* Clean historical relocation datasets, evaluate trends using Pandas DataFrames, and sync data seamlessly with PostgreSQL.

### Phase 5: Decoupled REST API Migration
* Port the command-line mechanics over to a scalable FastAPI framework.
* Implement structured request/response security wrappers through Pydantic schemas.

### Phase 6: Containerization & Operations
* Wrap the complete architecture (FastAPI service and PostgreSQL database) into distinct, isolated Docker environments.