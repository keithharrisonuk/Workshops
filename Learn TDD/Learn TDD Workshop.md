What are we learning
 - TDD
 - Dependency Injection
 - Refactoring


Scenario
 - You are a developer for a global financial institution. You work in the retail stockbroking lob helping customers invest in stocks and funds.
 - You are aiming for promotion. To get promotion you need to achieve your end of year goals
    - Deliver you software to a high quality
    - Achive your business goals

Lession 1 Learn TDD Basics
 - Write a test 
 - Write a solution
 - Refactor

 The business need to keep track of how many shares each customers owns
 Excercise
   - Add a sell share function 
   - Refactor
   - Add erorr handing when a user tries to sell shares that dont exist

  Refactor suggestion
    - Can you remove duplications in the tests?
    - Could the names in Share Service be improved and made more consistant?
    - Is 'items' the best name for the data structure contining the shares? 

Lession 2 - Mocking Dependencies
The business want to take payments for the shares they want to be able to easily change payment provider in the future.

- Create a PaymentService which calls the payment provider.
- Call the paymentService on buy and sell

Lession 3 - Adding a new payment provider
The business has found a new payment provider with cheaper fees if the tranasction is over $100 and wants you to switch to use them when the buy/sell is over $100. 
 -- Add an interface 
 -- Implement the interface for each provider
 -- Switch between provider

Refactor the code
  - 

Lession 4 - 
