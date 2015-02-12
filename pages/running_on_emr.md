---
layout: default
title: Running on EMR
order: 10
---

AWS EMR is a saas version of mapreduce and apache hadoop. It handles setting up hadoop
and running all software needed for mapreduce jobs.

mrjob on EMR performs these steps for you:

1. setting up an EMR cluster
2. copying data to an S3 bucket (optionally)
3. running mapreduce jobs
4. collecting stats
5. streaming the results to you or into S3
6. cleanup or terminiation of EMR clusters

For this section, we are going to setup EMR configuration and run some jobs on EMR.

Setup
-----

First, create a file called `~/.mrjob.conf` (in your home directory):

{% highlight text %}
{% include running_on_emr/mrjob.conf %}
{% endhighlight %}

You will need to replace `<key>` and `<secret>` with workshop provided ones.

When you run with the `-r emr` runner, by default, an EMR stack will be created
for you. This process takes quite a while, so instead of that, lets use one of the most powerful
features of mrjob, reusing emr job flows.

Next lets start one of our old jobs.

Replace `<CHANGE ME>` with the job flow id provided:

{% highlight bash %}
$ {% include running_on_emr/run.sh %}
{% endhighlight %}

If the job starts successfully, navigate to [http://localhost:40098/jobdetails.jsp](http://localhost:40098/jobdetails.jsp) to view the status and statistics.

Exercises
---------

 * Find some larger text and try to run wordcount.py with it on EMR.
