# State of Emergency

An outline for a *text adventure*, made with [Pygame-ce](https://pyga.me/docs/).

## Purpose

This is the first game (or outline of a game) I have ever written. I started it
to fulfill the first personal project requirement for Boot.dev's backend developer
courses. I wanted to be more familiar with Pygame than then Asteroids project
had made me, so I started watching more tutorials and experimenting more with the
Pygame-ce documentation.

I thought a text adventure would be a short and relatively easy project, and it
might have been had I stuck to using the terminal, but instead I opted to create
my own user interface, which includes a makeshift map, an inventory window, a
terminal that renders text, and the requisite input system, which also uses
rendered text.

What I have now is a functional, but messy knot of classes, methods, functions,
and repeated code that could probably be a lot tighter and easier to read. But
it's my first attempt at a game and it works, and I'm proud of that.

As of 8/2/2026, it's nearly complete. I hope to have multiple endings and a couple
of different "win" conditions in place before the end of the month.

## Inspiration

- Björk Guðmundsdóttir. Specifically, ["Jóga"](https://www.youtube.com/watch?v=loB0kmz_0MM) from the *Homogenic* album.
- David Lynch
- Text adventure games like *The Hitchhiker's Guide to the Galaxy*
- *Undertale*
- Wanting to make a game since I was a boy.

[DaFluffyPotato](https://www.youtube.com/@DaFluffyPotato) and [Clear Code](https://www.youtube.com/@ClearCode) helped a ton.

## Install/run

This thing isn't even close to finished, but if you want to see the mess I have
made in action, use [uv](https://docs.astral.sh/uv/).

- Download and install uv.
- Download this repository.
- Navigate to the program's directory.
- Run `uv sync`.
- Run `uv run code/main.py`

## How to play

It's fairly simple. Use the tab key to start entering text. Objects, scenes, and
details of interest appear in ALL CAPS. You can then:

- `look at` SOMETHING
- `investigate` SOMETHING
- occasionally, you can `get` or `pick up` SOMETHING
- `move` north, south, east, or west
- or simply enter `w`, `e`, etc. to move in that direction
- `observe` will repeat the text in each room, with slight differences
- `history` or `review` will allow you to see everything printed to the screen so far

## Still missing

- an end game
- a startup screen
- an instructions screen
- and some important functionality that is nearly done, like using objects together
