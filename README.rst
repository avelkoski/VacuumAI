VacuumAI
========
An implementation of an "intelligent" agent.

.. image:: /static/images/simulation0.gif?raw=true
     :align: center

Basic usage
-----------
::

    python main.py 5 15 0


Output
------
::

    Average Reward: 921.0
    Average Cells Cleaned: 9.6

Issues & Enhancements
~~~~~~~~~~~~~~~~~~~~~
There are several issues that need to be addressed. Contributions are welcome.

* **Environments**

  * Fixed nxn space
  * No obstacles
  * Dirt distribution

* **Agents**

  * Most importantly more learning, fewer rules
  * Perhaps split into distinct agents with varying degrees of capability (simple reflex, model-based reflex, goal-based, utility-based, and complex learning agents)

* **Plots**

  * PNGs are temporarily stored in a directory to create GIFs
  * A contour plot is better suited for plotting 3 dimensional surfaces

License
-------

The MIT License (MIT)

Copyright (c) 2017 Aleksandar Velkoski avelkoski@realtors.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Affiliation
-----------

The author is affiliated with the Data Science division of
the National Association of REALTORS®.
