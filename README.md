Pmdr - CLI pomodoro timer.

The following command:

```
pmdr start
```

Will give you a classic Pomodoro timer with 4 Pomodoros(25min of Focus followed by a 5 min break), and after 4, you shall get a Longer break of 30min.

With the following command:

```cmd
pmdr start -bs --breaks
```

You can set the number of long breaks needed to complete your tasks!

The following Command:

```cmd
pmdr custom
```

Can be used to build out your own timer how you see fit.
The following flags can be used to build your own custom pomodoro timer setup.

```python
-f --focus # Focus time, default 25min
-s --short # Break time after every Focus time, default 5min
-l --long # Long break, default 25min
-bs --breaks # Number of long breaks to take, default 4
```

Pmdr also comes with a few quick timers for ease of use:

```python
pmdr hour # minute timer

pmdr half # 30 minute timer
```

You can also set a custom timer with the following command:

```cmd
pmdr timer -m --minutes
```

Create your own CLI tools: [Tutorial](https://medium.com/nerd-for-tech/how-to-build-and-distribute-a-cli-tool-with-python-537ae41d9d78)
