#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0035.py
功能: 拟人化的函数式多线程池例子
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016/12/27 08:48:12
"""

from __future__ import print_function
from Queue import Queue as Jobs
from threading import Thread as Worker
from random import randint as assign_job
from time import sleep as work  # the job is spleeping!


def gowork(worker_id, jobs):
    job_count = 0
    while True:
        job_id, job_time = jobs.get()
        print ('worker {} is working with job {}.'.format(worker_id, job_id))
        work(job_time)
        job_count += 1
        print ('worker {} finished job {}.'.format(worker_id, job_id))
        print ('worker {} have done {} jobs.'.format(worker_id, job_count))
        jobs.task_done()


if __name__ == '__main__':
    jobs = Jobs()
    for job_id in range(10):
        job = job_id, assign_job(1, 5)
        jobs.put(job)
    for worker_id in range(3):
        worker = Worker(target=gowork, args=(worker_id, jobs))
        worker.daemon = True
        worker.start()
    jobs.join()
    print ('all jobs is done!')
