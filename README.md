# Asynchronous-Computation-in-a-Synchronous-Control

This project was developed as part of my Masters course study in Computer Organization and Architecture II.

Authors: Prudhviraj Sheela, Aman Masipeddi, Hai Huynh

Programming Language Used: Python 3.7

IDE Used for Development: Jupyter Notebook

The purpose of this project is to implement an asynchronous computation in a synchronous control. The computation process consists of two phases which are to be implemented.

The synchronous control baselined is described as follows:

i)There is a stream of transactions queueing and processed into a block.

ii) Each block is considered to be comprised of equal set of slots.

iii) A bulk of transactions is processed in a batch such that a batch of transactions is to be processed as soon as total 'n' number of slots from a certain number of transactions together are queued into a block, which is, namely the synchronous control of concern in this assignment.

iv) Note that for simplicity it is assumed that any transaction that is in execissive size in slots to overflow the capacity of a block, is to be cut to be accommodated just to fit 'n'.

Phase-I: Find the probability, P(i) of the synchronous control to have 'i' number of slots in the block at equillibrium and plot their appropriate graphs such that the some of the probability converges to '1'.

Phase-II:

A) Based on the probability P(i) in Phase-I, find P(i) when the size of the block is adaptive (or) find the normalized P(i) to track the adaptive block size and plot their appropriate graphs such that the some of the probability converges to '1'.

B) Find P(i) that can compute towards a pseudo asynchronous block processing which means each transaction will be posted as soon as posted than just processing the whole block at once. Also we plot their appropriate graphs such that the some of the probability converges to '1'.

As a solution for processing this project we had referenced different queueing models for developing a asynchronous computation in a synchronous control. There are two reports for the Phase-I and Phase-II problems which describe how the end result is obtained and how do the sum of probabilities converge to the value of '1'.
