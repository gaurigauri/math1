# math1

This repository contains code that can generate a table for any number.

| What you can do | Where is the code |
|---              |--                 |
| Addition        | [code](st_addition.py) |
| Multiplication  | st_multiplication.py|




```mermaid
   graph TD
          subgraph Arithmetic
                Addition -->|canuse| Multiplication
                Multiplication --> |requires| Tables
                Division       --> |requires| Tables
                Counts         --> |requires| Addition
          end

          subgraph Frequency
                Dictionary     --> |stores| Counts
          end
```
