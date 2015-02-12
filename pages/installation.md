---
layout: default
title: Installation
order: 2
---

We will be using `pip` and `virtualenv` to install `mrjob` so we do not
bother system dependencies.

Python 2.7 is required so run this to see if you get something similar:

{% highlight bash %}
$ python --version
Python 2.7.9
{% endhighlight %}

Setup
-----

Let's install and configure `virtualenv`:

{% highlight bash %}
$ sudo pip install virtualenv
$ virtualenv mrjob_env
...
$ source mrjob_env/bin/activate
(mrjob_env) $ pip install -U pip
...
(mrjob_env) $ pip --version
pip 6.0.8 ...
{% endhighlight %}

For the rest of the workshop, you will need to make sure you are "in" your 
`virtualenv`, so make sure `(mrjob_env)` is always prefixing your prompt.

Install
-------

{% highlight bash %}
(mrjob_env) $ pip install mrjob
...
{% endhighlight %}

