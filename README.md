# Project Advising Checklist

#### By Melissa Hibner

## Description
_This project consists of a template advising checklist_

## User Stories
Admission advisors want to:
- make changes to core and elective *courses* for each degree checklist quickly so they can allocate time to other tasks
- create new certification and *degree* checklists so they can provide quick turnover to department heads and dean/s
- receive an example course planning *guide* that automatically considers prerequisites and regularly scheduled course offerings to increase their bandwidth for other tasks 
- share an example course planning guide for the semester to help their advisees and serve as an aide during advising appointments which will help guide their discussion
- quickly identify if students’ transfer courses are eligible substitutions, upload students’ completed coursework, and receive individualized course plans to help facilitate advising discussions

## Diagrams

This conceptual diagram illustrates the many-to-many relationship between students and courses, and one-to-many relationship between department and courses
![conceptual diagram](advising/img/erd_20231008_conceptual.png)

This logical diagram illustrates a more detailed representation of attributes found in each entity, along with an intermediary weak entity of student_course.
![logical diagram](advising/img/erd_20231008_logical.png)

This physical diagram builds upon the prior diagrams and includes specific data types, such as date, integer, boolean, and string character length.
![physical diagram](advising/img/erd_20231008_physical.png)


## Technologies Used
- Django
- Python
- HTML

## Setup/Installation 
1. Go to github repository 
2. Select "<> Code" button
3. Copy repository url
4. Clone repository url to desktop: `$git clone url`
5. Download project dependencies
6. Apply migrations: `python manage.py migrate`
7. Run server: `python manage.py runserver`

## Known Bugs
_There are no known bugs_

## License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright &copy; 2023, Melissa Hibner