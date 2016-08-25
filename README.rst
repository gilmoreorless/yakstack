yakstack
========

A command-line utility to help you stack your yaks.

Err... What?
------------

“Yak Shaving” is a common term in the tech industry. As `originally described`_:

    | You see, yak shaving is what you are doing when you're doing some
    | stupid, fiddly little task that bears no obvious relationship to what
    | you're supposed to be working on, but yet a chain of twelve causal
    | relations links what you're doing to the original meta-task.

In other words, Yak Shaving is the series of distractions and/or necessary tasks you find yourself doing while you were *meant* to be doing something else. Each progressive step is logical, but when you end up doing something completely different from what you intended, it’s easy to lose track of how you got there. When you realise you’re getting further and further away from the primary task, you’re yak shaving.

This phenomenon is so common that it has become the source of meta-jokes about stacks of yaks (where one instance of yak shaving isn’t enough), and more detailed involvement (“I’m not just shaving the yak, I’m grooming it as well”).

This script helps you keep track of your “yak frames”, or context switches. Got distracted from a task? Add it to the yak stack. Got distracted from the new task? Also add it to the yak stack. Once you’ve finished, shave the yak and go back to the previous task. Originally inspired by this usage of the term:

    | yak frame - n. a yak shaving stack frame. ex: "I'm currently 3-4 yak frames deep"
    |
    | — Charlie Somerville (@charliesome) `August 19, 2013 <https://twitter.com/charliesome/status/369371752696012801>`_

``yakstack`` is not a todo list, or a task management solution. It’s simply a way to keep track of your context switches, so you don’t end up thinking “what was I meant to be doing again?”


Installation
------------

``yakstack`` requires **Python 2.7** with `pip <https://pip.pypa.io/en/stable/>`_:

.. code:: sh

    pip install yakstack

Currently only Python 2.7 is supported; Python 3 compatibility is coming soon.


Usage
-----

On first usage, ``yakstack`` will have an empty yak stack. You have no tasks in the list.

.. code:: sh

    $ yakstack
    No yaks to shave right now!

Adding yak frames
~~~~~~~~~~~~~~~~~

Any arguments to ``yakstack`` are added as frames on your yak stack.

.. code:: sh

    $ yakstack "Work on super-important project"
    You are currently 1 yak frame deep

    Work on super-important project

    $ yakstack "Show yak script to a colleague"
    You are currently 2 yak frames deep

    Work on super-important project
     ⤷ Show yak script to a colleague

You can add multiple yak frames in one command.

.. code:: sh

    $ yakstack "Write a README for yakstack" "Argument on Twitter"
    You are currently 4 yak frames deep

    Work on super-important project
     ⤷ Show yak script to a colleague
        ⤷ Write a README for yakstack
           ⤷ Argument on Twitter

Removing yak frames
~~~~~~~~~~~~~~~~~~~

To **remove** an item from the stack, use the ``--shave`` (or ``-s``) option.

.. code:: sh

    $ yakstack --shave
    You are currently 3 yak frames deep

    Work on super-important project
     ⤷ Show yak script to a colleague
        ⤷ Write a README for yakstack

    # THIS ALSO WORKS
    $ yakstack -s

You can also remove multiple yak frames in one command. Use multiple ``--shave`` or ``-s`` options.

.. code:: sh

    $ yakstack --shave --shave
    You are currently 1 yak frame deep

    Work on super-important project

    # THIS ALSO WORKS
    $ yakstack -ss

Managing multiple yak stacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you might have different yak stacks running at the same time, to track distractions from different projects. Perhaps you want to track things separately for your personal projects when you’re not at work.

To switch to a different profile, use the ``--profile`` (or ``-p``) option with a profile name. Once you have more than one profile, ``yakstack`` will always tell you which profile you’re using.

.. code:: sh

    $ yakstack
    You are currently 1 yak frame deep

    Write README for yakstack

    $ yakstack --profile work
    No yaks to shave right now for profile "work"!

The default profile used by ``yakstack`` is called, unsurprisingly, “default”.

You can switch profiles while adding new yak frames.

.. code:: sh

    $ yakstack -p default "Find out latest sports scores"
    You are currently 2 yak frames deep for profile "default"

    Write README for yakstack
     ⤷ Find out latest sports scores


Other notes
-----------

The arguments to ``yakstack`` follow standard Unix command-line patterns. This means that space characters separate multiple arguments (and therefore multiple yak frames). To add a sentence containing spaces to your yak stack it must be surrounded by quotes.

.. code:: sh

    # With quotes
    $ yakstack 'A single sentence with quotes' "And another one"
    You are currently 2 yak frames deep

    A single sentence with quotes
     ⤷ And another one

    # Without quotes
    $ yakstack This adds a whole bunch of frames
    You are currently 9 yak frames deep

    A single sentence with quotes
     ⤷ And another one
        ⤷ This
           ⤷ adds
              ⤷ a
                 ⤷ whole
                    ⤷ bunch
                       ⤷ of
                          ⤷ frames

Oh, and one more thing:

.. code:: sh

    $ yakstack --sax

You’re welcome.


.. _originally described: http://projects.csail.mit.edu/gsb/old-archive/gsb-archive/gsb2000-02-11.html
