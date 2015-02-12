---
layout: default
title: Introduction
order: 1
---

mapreduce
---------

mapreduce is all about filter and sorting in a distributed fashion (obviously this is not a great definition).

![mapreduce diagram](https://cloud.google.com/appengine/docs/python/images/mapreduce_mapshuffle.png)

With large datasets, the benefit of mapreduce can be seen in performing the operations in a distributed computing environment.

Some example uses of mapreduce:

* Distributed sort
* Counting frequencies
* Graph based analysis (friends of friends)
* Calculating aggregates
* Duplicate detection (similarity detection)

*[http://www.datasalt.com/2012/12/mapreduce-real-use-cases/](http://www.datasalt.com/2012/12/mapreduce-real-use-cases/)*

mrjob
-----

mrjob facilitates writing mapreduce jobs in python and running the jobs in many different ways.

Why mrjob?

* Python!
* Little setup overhead
* Run, test and debug locally
* Local, hadoop and EMR runners with no code changes
* EMR job flow reuse (saves you money)

*[https://pythonhosted.org/mrjob/guides/why-mrjob.html#overview](https://pythonhosted.org/mrjob/guides/why-mrjob.html#overview)*
