# Room-Cleaning-Robot (Dynamic Control Task)
Problem Statement: Consider a Room Cleaner Robot which cleans a room containing dirt. A room can be treated as a  𝑚×𝑛 grid with walls on all sides.
(a) Implement an environment which takes as inputs the values  𝑚 and 𝑛. Initially, 10 random cells in the grid contain dirt. The list  𝑑𝑡 with dimensions  𝑚×𝑛 contains the information on the amount of dirt in each cell of the grid. At any point of time, a unit dirt is added at a random location, i.e., a location  (𝑥,𝑦) is picked uniformly at random and  𝑑𝑡(𝑥,𝑦) is updated to  𝑑𝑡(𝑥,𝑦)+1 .

(b) Implement an agent which at each time instant 𝑡 observes its position  a𝑡=(𝑥𝑡,𝑦𝑡) (but not the dirt information in this location) and performs a random action  𝑎𝑡∈{𝑢𝑝,𝑑𝑜𝑤𝑛,𝑟𝑖𝑔ℎ𝑡,𝑙𝑒𝑓𝑡,𝑝𝑖𝑐𝑘𝐷𝑖𝑟𝑡}. On hitting a wall or picking dirt from the current location  (𝑥𝑡,𝑦𝑡), the agent stays in the same position  (𝑥𝑡,𝑦𝑡), otherwise, its position changes according to the action. Every action is associated with a reward (or penalty) defined as follows.
rt = R((xt, yt), at) = (Reward)
    −1, if the agent tries to pick dirt and (xt, yt) is a clean cell
    −10, if the agent hits a wall 
    d, if (xt, yt) has d units of dirt and the agent picks it
    0, otherwise

(c) Print out the activity at each time instant t for t = 1, . . . , 1000. That is, for each t, display the grid (with dirt values in each cell), the location of the agent, the action of the agent and the reward obtained.
