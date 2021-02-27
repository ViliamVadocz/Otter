# Otter

## Setup

Please run `setup.bat` to install dependencies and hooks.

If your IDE generates a file that is not ignored by the `.gitignore`, feel free to add it.

## Inspirations and Credits

- [Botimus Prime](https://github.com/Darxeal/BotimusPrime) by Darxeal
- [RLUtilities](https://github.com/samuelpmish/RLUtilities) by chip


## TODO

- Rewrite strategy
    - Currently the strategy is a mess
    - Otter never defends and commits to ridiculous shots
- Alignment checks
    - Related to intercept selection
    - Go for later, better shots
    - E.g. if the ball is bouncing in front of next, shoot later to hit the goal instead of the wall
- In strikes, if we have time, do some lining up to get a more accurate shot
    - Just look at how Botimus does it
- Fix and use GroundStrike
    - It will also need a lot of work, because it is currently more like a dribble state
- Fix AerialStrike validation
    - It is really bad, literally just a constant speed estimation
    - The when-in-air simulation-based validaiton is broken, and the bot never goes for double touches
- Clean up repo
    - Separate moves into folders
    - Remove unused or reduntand stuff (e.g. DoubleJump, just use RLU)
- Add pathing
    - Figure out how RLU's Navigator works
    - Use it to get an intercept
    - Use it to follow the path
- Add Defence
    - Add a move
    - Incorporate it into strategy
    - Add shadowing?
- Fix performance drops
    - Figure out why the bot sometimes drops to 10%
    - Fix it
    - Maybe rewrite something in Rust (bonus: bragging rights)
- Fix RLU Bug
    - GameState is incorrectly Inactive when it should be Paused
- Better movement planning / think ahead
    - Do not drive directly at something if it leaves Otter facing the wall
    - Rotate far-side to avoid running into teammates
- Small pad collection
- Add new strikes
    - Mirror-shot
    - Pinch
- Dribbling
    - Add dribbles
    - Add flicks
- Aerial
    - Add Air dribble
    - Add Flip reset
    - Add Ceiling shot
- Drift LUT
- Extra modes support
    - Dropshot
    - Hoops
    - Heatseeker
    - etc.
    - Have a fallback when RLU Field geometry is not available
- Fun
    - Celebrate after goal
    - Spam Otter in league play Twitch chat
