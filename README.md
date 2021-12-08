# Development Operations - Team 3
This following README file give you more insight into our development and processes carried out for the development of the game 'Simp City'.

---
## Our Team

**Team Members:** Linus Tay, James Yu, Keith Ang, Gerald Tan, Zhen An

Team Roles:
1. Scrum Master - Linus Tay
2. Technical Lead - James Yu
3. QA - Keith Ang
4. Developers - Gerald Tan, Zhen An

---
## Project Background
> The project is essentially a city-building strategy game is played over 16 turns. In each turn, you will build one of two randomly-selected buildings in your 4x4 city. In the first turn, you can build anywhere in the city. In subsequent turns, you can only build on squares that are connected to existing buildings. The other building that you did not build is discarded.

> Each building scores in a different way and the objective of the game is to build a city that scores you as many points as possible.

---
## Chosen Software Development Life Cycle (SDLC)

---
## User Stories

---
## Test Cases

---
## SDLC Considerations

We aim to cover some of the different methodologies that could possibly be used for our project on the city-building strategy game called “Simp City”. Within this case study, we were given the background, scope and project requirements for the game. Therefore, with the afore-mentioned information, we have decided to discuss and analyze 5 different Software Development Life Cycles (SDLCs) so that we can decide on which might be the most suitable or viable for the development of Simp City. 

These 5 SDLCs include: Incremental, Iterative, V-Shaped, Waterfall, and Agile.

### Incremental 
#### General Information 
Incremental Model is a process of software development where requirements are broken down into multiple, simpler standalone modules of software development cycle. The development of incremental models is done in steps from analysis design, implementation, testing/verification, maintenance. For each increment, it passes through the requirements, design, coding and testing phases. Moreover, each subsequent release of the system adds function to the previous release until all designed functionality has been implemented.


**Requirement analysis:** In the first phase, expertise identifies the requirements. Additionally, the system functional requirements are understood by the requirement analysis team. Thus, to develop the software to undergo the incremental model, this phase performs a crucial role.

**Design & Development:** In this phase of the Incremental model, the design of the system functionality as well as the development method are finished without failure. When software develops new practicality, the incremental model uses style and development phase.

**Testing:**  The testing phase checks the performance of each existing function as well as additional functions. In the testing phase, the various methods are used to test the behaviors of each task.

**Implementation:** This phase enables the coding phase of the development system. It involves the final coding of the design in the designing and development phase and tests the functionality from the testing phase. After completion of this phase, the number of the product working is enhanced and upgraded up to the final system product, which would then be incremented. 

 
#### When to use Incremental model?
The incremental methodology is usually used when:
* the requirements of the system are clearly understood.

* demand for an early release of a product arises.

* the engineering team are not very skilled or trained.

* high-risk features and goals are involved.

* the project comprises of a web application or the company is product-based.

**Advantages**
* Throughout the development stages changes can be done.

* Errors are easy to be identified.

* It is easier to test and debug during a smaller iteration.

**Disadvantages**
* Incremental models need good planning and design.

* Needs a clear definition of the whole system before it can be broken down and built incrementally.

**Fit to our Project**
As stated above on when to use incremental models, it shows how this SDLC could be an option for our case study. This is because the requirements for the project are well understood and laid out. There are also guides on how the design of our program should work. In addition, making use of this SDLC would help ensure the quality of the Simp City game through the testing phase of each increment. 

However, splitting up the Simp City game releases into different increments might not make sense. This is because the game seems to rely on all features to be developed and accomplished in order to have a complete and functional game. Moreover, it had not been determined by the customer that the game should be developed incrementally. 

---
### Iterative 
#### General Information 
In the Iterative model, the process starts with simple soft requirements and implementation which will then be iteratively enhanced through every evolution until the complete system is fully implemented and ready to be deployed.

Iterative and incremental development is any combination of both iterative design and incremental build model for development.

* Iterative design – It is a methodology based on cycle of prototyping, testing, analyzing, and refining a product/process. Any modification or refinements made are usually based on the results of testing the most recent iteration of a design. The process of this is intended to ultimately improve the quality and functionality of the design.

* Incremental build model – the whole requirement is sliced into increments(portions). During each increment, a slice of the functionality is delivered through the method phases, from requirement phase till review phase.

![This is an image](/images/iterative.png)

#### Iterative Methodology Phases

1. Requirement Phases – requirements can be a new requirement or an extension from the previous build requirement
2. Design Phase – proper design is implemented after requirements are being gathered.
3. Implement/Development Phase – finalized design will then be implemented with decided coding
4. Testing – testing phase is required to identify errors so that it could be reported back to the developers.
5. Review – The development requirement will be reviewed to meet the standards as per the decided requirements. A further requirement plan as part of the next iteration will be drafted basing on the review.

**Advantages** 
* Early testing and review can identify error in the early stages and is highly reliable
* Testing and debugging during each portion make it easier and effectively as compared to testing the complete requirement
* Issues/challenges detected from each increment can be utilized to the next increment
* Adaptability (changes of requirements requested can be easily implemented at each stage)
* Best suited for large projects
* Software developed in early cycle can help to gather customer evaluation and feedbacks

**Disadvantages**
* There is an increased pressure on user engagement - Unlike other models which emphasizes on nearly mostly client/user engagement, the iterative model often requires user engagement throughout the entirety of the process. This is done so as each new iteration will likely require testing and feedback from users to properly evaluate any necessary changes.
* Not suitable for smaller projects
* It is possible that an unforeseen issue in design or the underlying architecture may arise into the project. Resolving this may be costly and create devastating effect on the time frame of the project, requiring a great deal of future iterations just to resolve that issue.

#### Fit to our Project
**Why should we use iterative methodology?**
* Adaptable (easy to ad-here to any changes required in the early stages)
* Testing and debugging during each portion can helps to progress easier and effectively
* Can be adopt with other methodology

**Why should we not use iterative methodology?**
* We already have a set of requirements defined and given. The Software is not to be built based on customer evaluation and feedbacks 
* Usually, best suited for bigger projects with big set of requirements so that it can be broken down into portions.

---
## Extras

---
### Connecting Jira to GitHub