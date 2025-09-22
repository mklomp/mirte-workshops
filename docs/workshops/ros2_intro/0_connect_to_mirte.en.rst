:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.1 Connecting to the MIRTE robot
#########################################

From now on we will start working on the MIRTE robot. We first need
to connect to the wifi connection of the robot. Please follow the 
instructions for the `Wireless Acces Point <https://docs.mirte.org/develop/doc/mirte_os/connect_to_mirte.html#wireless-acces-point>`_
to connect to your own MIRTE. The Unique ID is mentioned on
the sticker on the robot.

Note that we are now 'on the MIRTE robot', so everything we type will
be executed on the robot. Moving our workspace to the robot is easy:

As soon as we are connected to the robot, we can 
also connect VS code to the MIRTE robot. In VS code, connect to the MIRTE:

- In VS code press F1
- Type Remote-SSH > Connect to Host...
- Type: 192.168.42.1

In order to type command, you need to open a terminal in VS code
(View > Terminal).

.. admonition:: info

   In this training we will use mirte$ for commands that will run on
   the MIRTE robot.





