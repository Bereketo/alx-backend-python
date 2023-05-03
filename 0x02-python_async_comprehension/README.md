# 0x02. Python - Async Comprehension
## Learning Objectives
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
  * How to write an asynchronous generator
  * How to use async comprehensions
  * How to type-annotate generators
## Tasks
* <font size=2> **0. Async Generator** </font>
  * Write a coroutine called async`_`generator that takes no arguments.
  * The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.
* <font size=2> **1. Async Comprehensions** </font>
  * Import async`_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.
  * The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.`
* <font size=2> **2. Run time for four parallel comprehensions** </font>
  * Import async`_comprehension from the previous file and write a measure_runtime coroutine 
  that will execute async_comprehension four times in parallel using asyncio.gather.

  * measure_runtime should measure the total runtime and return it.`



