# SmartStock: Inventory Management System

**Author:** Delos Reyes, Kyle Kevin  
**Section:** A  
**Language/Platform:** Python 3 (Command Line Interface)  
**Storage Format:** Local Flat-File System (`.txt`)

---

## 📝 Project Description
**SmartStock** is a lightweight, backend-focused Command Line Interface (CLI) application designed using Object-Oriented Programming (OOP) principles in Python 3. Built as a streamlined solution for small businesses or retail tracking, the system automates inventory tracking, product cataloging, and stock management without requiring complex database systems.

The application utilizes a clean code structure that decouples the functional business logic (`src/`) from the local storage files (`data/`). This ensures that the code remains maintainable, scalable, and fully optimized for version control tracking on platforms like GitHub.

---

## ✨ Core Features

* **Automated Data Persistence:** SmartStock protects your inventory data against unexpected system shutdowns. Using Python's file I/O operations, every transaction dynamically writes to a local text file (`data/inventory.txt`), ensuring instant data recovery upon application initialization.
* **Granular Product Control:** Features a dedicated `Product` data blueprint to encapsulate essential retail metrics, allowing administrators to seamlessly bind individual items to a unique Product ID (`pid`), Name, Quantity, and Price.
* **Dynamic Stock Modifier:** Provides a fast execution routine (`update_stock`) to alter active stock amounts. Instead of rewriting or re-entering data completely, it safely adjusts the current quantities on the fly using key lookup constraints.
* **Case-Insensitive Query Engine:** Includes a search tool that normalizes both database strings and user input into lowercase format. This ensures accurate product matching regardless of how capital letters are typed (e.g., searching *"apple"*, *"Apple"*, or *"APPLE"* returns the exact same record matrix).
* **Defensive Exception Handling:** Armed with smart error handling (`try-except` blocks) during file reading. This allows the application to initialize smoothly on its very first run by gracefully handling missing database file conditions without crashing the system terminal.
----
DelosReyes_KyleKevin_FinalProject/

│

├── data/

│   └── inventory.txt             # Local flat-file text database for item retention

│

├── src/

│   └── main.py                   # Contains OOP Blueprints (Product & Inventory classes) 

│                                 # and the main terminal loop controller

└── README.md                     # Technical documentation and deployment guide


-----
## SIMPLE CLI USAGE
<img width="379" height="547" alt="Screenshot 2026-05-16 220211" src="https://github.com/user-attachments/assets/f92a86fb-d22e-4674-934f-08815c0e7df8" />


<img width="356" height="233" alt="Screenshot 2026-05-16 220255" src="https://github.com/user-attachments/assets/d1ed59c0-ca0a-49a9-91fc-714587015ba3" />



---


## 🎥 Video Demonstration
For a full demonstration, check out this video link:  
👉 [Watch the SmartStock Demo on YouTube](https://youtu.be/xzMlQG5sZ2E?si=W8-hLrtMI4pF_L_K)
