import os
import time
from datetime import datetime

def backup_mysql_database(host, user, password, db_name, backup_dir):
    # Create backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Construct the backup file path
    backup_file = os.path.join(backup_dir, f"{db_name}_backup_{timestamp}.sql")
    
    # Construct the mysqldump command
    dump_command = f"mysqldump -h {host} -u {user} -p{password} {db_name} > {backup_file}"
    
    # Run the command
    os.system(dump_command)
    
    print(f"Backup created at {backup_file}")

if __name__ == "__main__":
    # Database connection details
    db_host = "localhost"  # Change if necessary
    db_user = "root"
    db_password = "your_password"
    db_name = "your_database"
    
    # Backup directory
    backup_directory = "/path/to/backup/directory"
    
    # Take a snapshot of the database
    backup_mysql_database(db_host, db_user, db_password, db_name, backup_directory)
