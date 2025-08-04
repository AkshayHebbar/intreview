# Backend
Python version: 3.9 - 3.13.5  
Poetry version: 2.0.0 - 2.1.3  

### Create a virtual environment
`python3 -m venv path/to/venv`\
`source path/to/venv/bin/activate`

### Install libraries
`cd BE`\
~~`pip install -r requirements.txt`~~\
~~If the above command gives error the try the below command.~~\
`pip install -U poetry`

### Version check
`python --version`\
`poetry --version`

### Poetry Installation
`cd app`
`poetry install`

## Python In-Memory SQLite Backend

This backend uses Python’s built-in `sqlite3` module to create an in-memory database for storing interview data.

### How to Run
2. Navigate to the `BE` folder:
   ```
   cd BE
   ```
3. Run the connection manager script:
   ```
   python connection_manager.py
   ```
4. You should see output similar to:
   ```
   [(1, 'Alice Johnson', '2025-08-03', 'Strong communication skills. Needs to improve technical depth.')]
   ```

### Notes

- The database is in-memory, so all data will be lost when the script ends.

> ___Continue with the README under app folder___