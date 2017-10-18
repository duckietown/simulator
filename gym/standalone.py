#!/usr/bin/env python3

from __future__ import division, print_function

import gym
import gym_duckietown
import pyglet

def main():

    env = gym.make('Duckietown-v0')
    env.reset()

    env.render()
    @env.window.event
    def on_key_press(symbol, modifiers):
        from pyglet.window import key

        action = None
        if symbol == key.LEFT:
            print('left')
            action = 0
        elif symbol == key.RIGHT:
            print('right')
            action = 1
        elif symbol == key.UP:
            print('forward')
            action = 2
        elif symbol == key.DOWN:
            print('back')
            action = 3

        obs, reward, done, info = env.step(action)

        print(reward)

        env.render()

        if done:
            print('done!')
            env.reset()

    # Enter main event loop
    pyglet.app.run()

if __name__ == "__main__":
    main()
