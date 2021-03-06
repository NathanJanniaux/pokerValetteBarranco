# Leduc Push and Fold

Our first step was to implement Push or Fold Leduc Hold'em.

## Game rules

### Init

There are two players with the same stacksize. At the begining of the game, both players spend a blind (1 unit) in the pot.

### First Step

Then, the firstplayer will decide either to Push or Fold based on its card.

### Second Step

Now, the secondplayer will decide either to Push or Fold based on its card and the firstplayer action.

## Action space

- Push
- Fold

## State space

- Our hand : J, Q, K
- Opponent action : Unknown or Push

For a total of 3 * 2 = 6 states.

## QTable Structure
<img src="qtable.png"></img>
## Results
### Random Agent
We know the optimal policy of this game against a random agent : Fold when we have a J, Push when we have a K, and 50/50 when we have a Q (here, we aren't considering the opponent action because it's a random agent).

Here is the code :
```python
randAgent=RandAgent()

env=Environment(randAgent)
qagent=QAgent()

for i in range(epochs_number): 

    env.reset()
    qagent.set_state(env.get_state())
    qagent_action=qagent.explore_action()
    reward=env.reward(qagent_action,env.get_state())
    qagent.update(qagent_action,reward)
    
print("QTable=",qagent.qtable)
```
And here are the results :

```bash
QTable=
[[-0.99982304 -0.16148437]
 [-0.99973028  2.14646803]
 [-0.99996356  2.51629552]
 [-0.98669721 -1.23603417]
 [-0.9962429   1.87547468]
 [-0.9835768   6.58635557]]
 ```

### Naive Agent
To force our agent to consider the opponent action, we should change the opponent policy. In that case, the naive agent will always Fold when it has a Q or a K, else it pushes.

Here, our new agent optimal policy will to always Push, no matter its hand.

Here is the code :
```python
naiveAgent=NaiveAgent()

env=Environment(naiveAgent)
envTest=Environment(naiveAgent)
qagent=QAgent()

for i in range(epochs_number): 

    env.reset()
    qagent.set_state(env.get_state())
    qagent_action=qagent.explore_action()
    reward=env.reward(qagent_action,env.get_state())
    qagent.update(qagent_action,reward)
    
print("QTable=",qagent.qtable)
```
And here are the results :

```bash
QTable=
[[-0.9999383   0.92845981]
 [-0.999045    1.83832357]
 [-0.99987099  2.11402158]
 [-0.81469798  0.        ]
 [-0.94185026  5.54625505]
 [-0.93538918  2.89580639]]
 ```
 
 We clearly see that our agent will always push.
 
