# Sprint Summaries & Final Project Report

## 0. Requirements Gathering (Sep 11 – 18)
Team lead: Skyler

### Sprint Summary
This sprint we created user stories and UML diagrams to better understand how our users would interact with our program and to determine their needs.

Boston - Set up git lab repo and worked on the manager section.

Benjamin - Compiled every teams user stories and diagrams as well as set up the group discord channel. He also worked with Emma on the customer section of the requirements.

Evan - Worked on the manager section of the requirements.

Emma - Worked with Ben on the customer section of the requirements. Helped Skyler proofread the final requirements mark down.

Jack - Worked with Skyler on the admin section of the requirements. Wrote a lot of user stories.

Skyler - Team lead, planned meetings, organized everyone into smaller teams for each section, got the requirements all put together and pushed to the repo.

### Deliverables

[Main documentation](requirements/requirements.md)

[All documents/work](requirements)


## 1. Design (Sep 18 – Oct 2)
Team lead: Evan

### Sprint Summary

The first half of this sprint we created the high level design document, consisting of 6 systems. The second half of this sprint we split into frontend and backend teams and created the low level design document from those perspectives.

Boston - Worked on customer support section of the high level design, and worked on the backend low level design.

Benjamin - Designed the finance system in the high level design doc, and did a great job finding a platform for designing the UI and kicked off the UI. Worked on the admin part of the frontend low level design.

Evan - Team lead, organized team into sub-teams, and helped coordinate both teams to make sure we were on the same page. Worked on drone system in the high level design doc, and the drone owner section of the frontend side of the low level doc.

Emma - Worked on the account section of the high level design doc, and the customer part of the frontend low level design.

Jack - Worked on ordering system in the high level design, and worked on the backend low level design.

Skyler - Worked on the inventory management system for the high level design, worked on the backend low level design.


### Deliverables

[High level design - main documentation](high%20level%20design/High%20Level%20Design%20Doc.md)

[High level design - all documents/work](high%20level%20design)

[Low level design - main documentation](low%20level%20design/Low%20Level%20Design%20Doc.md)

[High level design - all documents/work](low%20level%20design)

[Figma wireframes](https://www.figma.com/file/kuxGFMhTcyI4Y4n39xwAdq/DroneCones_UX_Blueprint?type=design&node-id=0%3A1&mode=design&t=ioyr94quhipTfDVW-1)


## 3. Development Part 1 (Oct 2 –Oct 16)
Team lead: Emma

### Sprint Summary

As a reminder:
- Frontend team: Evan, Ben, Emma
- Backend team: Jack, Boston, Skyler

Our goals for this sprint were:
- Create the structure for all the pages (frontend)
    - Including HTML, CSS
    - Not including much functionality
    - Not including connection to the backend
    - Customer pages (Emma)
    - Drone owner pages (Evan)
    - Admin pages (Ben)
    - Other account pages, etc (Everyone on frontend team - see issue assignments)
- Define tables (backend - everyone on backend team)
    - Inventory
    - User
    - Drone info
    - Order
    - Permissions change request
- Set up Vue server (frontend - Emma)
- Set up Django server (backend - Skyler)
- Write endpoints and functionality for login (backend - everyone on backend team)

We got a good amount of this done, but ran into some issues/complication along the way:
- The backend team decided we should use the Django REST framework about halfway through the sprint, which meant they had to change directions a bit
- CSS page design got a little more complicated than we envisioned - especially when we remembered that screens can come in different sizes

Overall, what we ended up getting done:
- Most of the set-up of the customer pages
    - The menu page’s CSS got very complex quickly - it’s getting close to done but there wasn’t enough time to finish it this sprint
    - The order history page also has ended up being complex - that will be done next sprint also
    - With a caveat that screen resizing still needs to be worked on
- The set-up of the drone owner pages
    - With a caveat that screen resizing still needs to be worked on
- The set-up of the admin pages
    - With a caveat that screen resizing still needs to be worked on
- The set-up of the other account pages
    - With a caveat that screen resizing still needs to be worked on
- Defining the tables
- Setting up Vue server
- Setting up Django server
- Adding Django REST framework to project

What we didn’t get done:
- Finishing menu page
- Finishing order history page
- Fixing screen resize issues for most pages
- Image attribution
- Write endpoints and functionality for login

Overall, I think things went well this sprint and that the team worked together well. We ran into a few issues with our implementation, but really that’s to be expected. I think we are in a good place moving into the next sprint, and are on a good track to finish in time with the quality of product we have set as our goal.

### Deliverables
[In progress source code - frontend](frontend)

[In progress source code - backend](backend/api)


## 3. Development Part 2 (Oct 16 –Oct 30)
Team lead: Jack

### Sprint Summary

This sprint was spent working towards a working API on the backend, and towards linking pages together on the frontend. Important milestones were reached on the backend with a minimal working API, and on the frontend completing several pages and using mock data for testing.

#### Backend Tasks

**Mock Data (Boston)**

We made mock data that looked like data that would be served by our API so that the frontend team could use it to test.

**Django REST Framework**

**Discussion (Jack, Boston, Skylar)**

We found this framework last sprint and it interested us a lot. However, there were some differing opinions as to whether
We should use it or not. We met and weighed the pros and cons, and decided it was the way to go.

**Learning (Jack)**

I spent about 6 hours over a few days reading documentation and going through tutorials to understand the different parts of the framework.

**Build an api for the inventory (Jack)**

After all the reading, this took a relatively small amount of time. We can now successfully make a get request, and there is limited functionality for post requests.

**Table Adjustments (Boston)**

There were some data fields that the frontend team realized they would like, so Boston quickly added those.

#### Frontend Tasks

**Continued Layout adjustment (Emma, Ben, Evan)**

The frontend team continued to polish the pages to make them user-friendly and to work across screen sizes.

**Mock Data (Ben, Emma)**

The mock data opened up a lot of debugging and testing opportunities. The menu page, in particular, is proving to be challenging.

**Menu Page (Emma)**

The menu page needs to communicate a lot of information, and the design they came up with is proving difficult to implement.

**Page Routing (Ben, Evan, Emma)**

The team had some meetings about routing HTTP requests to the right places. Now, the HTTP request on the admin pages and the drone pages call the correct functions.

### Deliverables
[In progress source code - frontend](frontend)

[In progress source code - backend](backend/api)


## 4. Development Part 3 (Oct 30 – Nov 13)
Team lead: Ben

### Sprint Summary

#### Summary

This sprint was primarily spent on integrating the backend API to the frontend pages.  In addition, any frontend elements and needed functionalities needing refinement or being finished were worked on.

#### Goals for the Sprint

**Frontend Goals**

1 - Integrate the user account system to frontend (i.e. login, registration, logout, etc.)
2 - Integrate all admin, customer, and drone pages to backend API.
3 - Finishing remaining frontend pages' functionality and routing.
4 - Fix any CSS issues related to resizing or general display of the pages.

**Backend Goals**

1 - Allow for both GET and POST operations for the backend API.
2 - Help team members with the setup of necessary servers and dependencies to run backend API.
3 - Finishing remaining backend table APIs and necessary functionality.

#### Results

Overall, this sprint was able to achieve a big chunk of our goals or be close to achieving our goals.  Here are the goals in detail:

**Integrate the user account system to frontend**

This goal was completed for the most part.  The login page is able to use the backend API to authenticate the user credentials and transfer the frontend to the user account page upon successful login.  Any invalid credentials are caught and the frontend displays an error message to notify the user of an invalid attempt to login.  The registration page successfully integrates the backend API to add new user accounts and automatically routes the user to the account page upon successful registration.  The header element of each page will use the user token from the backend API to determine whether to display the 'Login' option or 'Logout' option for if the user is logged out and logged in respectively.

**Integrate all admin, customer, and drone pages to backend API**

This goal is about 70% done.  As of the writing of the summary, the customer pages are fully integrated with the backend API.  The admin pages are mostly integrated, with certain pages needing further development of the backend API to allow the possibility of integration.  Namely, the 'Pay Leases', 'Manage User Accounts', and 'Financial Records' pages have data pieces and functionality that have no corresponding functionality from the backend API.  The drone pages are currently in the process of adding integration from the backend API.

**Finishing remaining frontend pages' functionality and routing**

This goal is about 90% done.  As of the writing of the summary, the customer pages are fully integrated with the backend API.  The admin pages are mostly integrated, with certain pages needing further development of the backend API to allow the possibility of integration.  Namely, the 'Pay Leases', 'Manage User Accounts', and 'Financial Records' pages have data pieces and functionality that have no corresponding functionality from the backend API.  The drone pages are currently in the process of adding integration from the backend API.

**Fix any CSS issues related to resizing or general display of the pages**

This goal is complete for the most part.  Each frontend page has proper display and descent resizability capabilities.  No obvious issues are present in any of the frontend pages.

**Allow for both GET and POST operations for the backend API**

This goal has been completed.  The backend API has implemented functions that allow for the retrieval and sending of data for users, inventory, customer, and drone data.  While some additional functions may need be needed as the project continues, the backend team is at a point that can easily add, remove, or modify their API without impacting the project's existing codebase too much.

**Help team members with the setup of necessary servers and dependencies to run backend API**

This goal has been completed.  The setup of the backend servers and dependencies (postgreSQL, running Django backend, etc.) was executed very well on multiple in-person meetings, as well as over Discord.  Any necessary changes on the backend API setup and dependencies were quickly and clearly explained to the frontend team.  In addition, any troubleshooting needed from the backend team was provided generously and in a timely manner.

**Finishing remaining backend table APIs and necessary functionality**

This goal is ongoing, but very close to completion.  While a big chunk of the inventory, customer, user, and drone backend API functions and models are complete, ongoing efforts to accommodate emerging frontend and other backend functionality is continually being made.

#### Issues

Some of the issues hindering progress on the project include:

1 - Many technical difficulties from postgreSQL, particularly the pgAdmin application, when attempting to make changes to the fundamental structure of the backend API.  In addition, pgAdmin would not connect to a server on Windows from time to time, requiring to use task manager's services tab to start the necessary service to allow pgAdmin to work properly.

2 - Changing implementation needs to backend API to accommodate new changes from both frontend and backend teams does introduce overhead in achieving the sprint goals.  However, this issue had minor impact to the progress of the project overall.

#### Individual Contributions

**Frontend Team**

Ben - Work on user account backend API integration to frontend and admin page integration to backend API.  Team Lead for Development Sprint 4.
Emma - Work on menu pages for customer, integrating customer pages to backend API, and improving screen resizing for customer pages.
Evan - Work on learning and research on how to integrate backend API to the drone operator pages.

**Backend Team**

Skyler - Work on building all the Order and Inventory API functions and models.
Boston - Work on finishing and deploying the User table.  Implemented session token authentication for users.  Aided with backend setup on local machines for team members.
Jack - Work on building the Drone API and working on the algorithm to assign drones to deliveries.

#### Conclusion

Overall, the development sprint was very productive and every team member contributed meaningfully to the project.  The majority of the goals of the sprint were able to be achieved or be close to completion.


### Deliverables
[In progress source code - frontend](frontend)

[In progress source code - backend](backend/api)


## 5.Testing & Deployment (Nov 13 – Dec 4)
Team lead: Boston

### Sprint Summary

This sprint we focused primarily on integrating unit tests and finishing critical features. The backend team mostly worked on the unit tests and creating docs like

### Sprint Goals
#### Frontend Goals
* Manually test basic tasks focusing on the demo tasks
* Update user manual with accurate screenshots
* Incorporate guest functionality
* Complete financial page including revenue for the company and drone owners

#### Backend Goals
* Create unit tests for every function
* Create test design doc
* Create guest functions
* Fix any issues reported by the frontend team
* Fix issues with drone operator functions

### Completed Tasks
#### Ben
- Finished Financial Records page and integration
- Polished CSS in admin pages, login page, web header
- Integrated guest login functionality
- User deletion functionality integration for admin
- Quality of life features for admin and login (things like error messages for invalid input, edge cases, etc.)
#### Evan
- Finished drone earnings page
- Worked on drone registration
- Simplified new drone page
- Fixed small bugs
- Manual frontend testing
#### Emma
* Updated design docs
* Wrote/edited user manual for customer-focused use cases
* Bug fix: screen resize layout issues
* Bug fix: inventory checking not looking at quantity
* Improved the ways prices are calculated
* Bug fix: assigned the correct drone to a new order
* Wrote script to populate/restock needed inventory items (for complete menu)
* Added allowing removal of items from cart
* Bug fix: applied better restriction of dashboard pages by role
* Frontend testing
#### Jack
- Implemented assigning drones to orders algorithm
- Updated our old design documentation.
#### Skyler
* Wrote order tests
* Wrote inventory tests
* Wrote the user manual
* Wrote the testing doc
* Added a restock table
* Added finance functionality to the backend
#### Boston
- General team lead things, such as coordinating/assigning tasks
- Reviewed merge requests and gave feedback
- Wrote drone operator tests
- Wrote user operator tests
- Created guest functionality for the backend
- Refactored drone operator functions
- Updated README on how to set up the project

### Results

Overall I was happy with how the team performed this sprint. Everyone was very active on our Discord chat, so whenever problems arose we were able to handle them quickly.

### Deliverables

[User's Manual](https://gitlab.cs.usu.edu/drone-cones/project-cone-by-drone/-/blob/master/user-manual.md)

[Test Design Report](https://gitlab.cs.usu.edu/drone-cones/project-cone-by-drone/-/blob/master/test-design.md?plain=0)


## 6. Maintenance (Dec 4 – Dec 11)

### Sprint Summary

* As a team, we decided on the use cases we wanted to demonstrate.
* Ben prepped sample data/accounts for the demo on his computer.
* Jack made sure design/other documentation is still up-to-date.
* Emma combined sprint summaries and deliverables into Sprint Summary and Final Project Report document, as
well as writing the final sprint summary report.

### Deliverables

Sprint Summaries and Final Project Report - this document!!
* Links to final drafts of
  * Requirements document
  * High-level design document
  * Low-level design document
  * Test design document
  * User's Manual
  
included in the summaries of their respective sprints.


