# Project Advising Checklist

#### By Melissa Hibner

## Description
_This project consists of a template advising checklist_

## User Stories
Admission advisors want to:
- view *degree* checklists quickly so they can respond to impromptu advising inquiries
- make changes to requirements, as well as core and elective *courses* for each degree checklist quickly so they can allocate time to other tasks
- create new certification and *degree* checklists so they can provide quick turnover to department heads and dean/s
- receive an example course planning *guide* that automatically considers prerequisites and regularly scheduled course offerings to increase their bandwidth for other tasks 
- share an example course planning guide for the semester to help their advisees and serve as an aide during advising appointments which will help guide their discussion
- quickly identify if students’ transfer courses are eligible substitutions, receive uploads of students’ completed coursework, and create individualized course plans to help facilitate advising discussions

## Diagrams

This conceptual diagram illustrates the relations between degree, requirement, programcourses, course, and prerequisite.
![conceptual diagram](/img/erd_20231015_conceptual.jpg)

This logical diagram illustrates a more detailed representation of attributes found in each entity.
![logical diagram](/img/erd_20231015_logical.jpg)

This physical diagram builds upon the prior diagrams and includes specific data types, such as date, integer, boolean, and string character length.
![physical diagram](/img/erd_20231015_physical.jpg)

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