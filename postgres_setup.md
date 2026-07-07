# PostgreSQL Setup

1. Install PostgreSQL.
2. Create a database:

```sql
CREATE DATABASE buynothing;
```

3. Install driver:

```bash
pip install psycopg2-binary
```

4. Update Django settings.py.
5. Run:

```bash
python manage.py migrate
```
