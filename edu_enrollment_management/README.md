# Educational Enrollment Management

## Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/rquevedo/unam_prueba_tecnica
  ```
2. Navigate to the module directory:
  ```bash
  cd unam_prueba_tecnica/edu_enrollment_management
  ```
3. Install the module:
  ```bash
  odoo -i edu_enrollment_management
  ```

## Configuration

1. Go to the Odoo backend.
2. Navigate to `Apps` and search for `Educational Enrollment Management`.
3. Click `Install`.

## Usage

1. Navigate to the `Educational Enrollment manager` menu.
2. Create a new enrollment by clicking on `Create`.
3. Fill in the required fields and save.

## Models

### Student
- **Purpose**: Represents a student in the system.
- **Fields**: Name, Birthdate, Age.

### Course
- **Purpose**: Represents a course available for enrollment.
- **Fields**: Name, Description, Start Date, etc.

### Enrollment
- **Purpose**: Links students to courses.
- **Fields**: Student, Course, Enrollment Date, Status, etc.

## System Administration

1. **Backup**: Regularly backup the database using Odoo's built-in tools.
2. **Updates**: Keep the module updated by pulling the latest changes from the repository.
  ```bash
  git pull origin main
  ```
3. **Logs**: Monitor Odoo logs for any errors or issues.

## Maintenance

1. **Database Cleanup**: Periodically clean up old or unused data.
2. **Performance Monitoring**: Use Odoo's performance monitoring tools to ensure the system runs smoothly.
3. **User Management**: Regularly review and update user permissions and roles.
