## About
- In this package, there are three python scripts, and they execute the same logic,
which is to download images from [unsplash](https://unsplash.com/).
- The purpose is to have a better understanding and to make comparison among the options of using multiprocessing, 
multithreading, and without using any. 

## Command
```
$ pip install -r requirements.txt
$ python withoutThreading.py
$ python multiThreading.py
$ python multiProcessing.py
```

## Logic
1. The key difference between multiprocessing and multithreading is that
**multiprocessing** allow a system to **have more than two CPUs added to the system**,
whereas **multithreading** let a **process generate multiple threads** to increase the computing 
speed of a system.
2. Multiprocessing system = multiple processes
3. Multithreading system = multiple threads
4. Creating a process can **consume time** and **even exhaust** the system resources.
5. However creating threads is **economical** as threads belonging to the same process share the resources
of that process.
6. Therefore, comparatively multiple threading is preferred because it is **cost effective and creating
threads takes less time**.

<img src="https://miro.medium.com/max/763/1*F8ckVaR__PlBssnf-mn76A.png" alt="detail">

## Result
```
# withoutThreading.py
art_1.jpg was downloaded!
art_2.jpg was downloaded!
art_3.jpg was downloaded!
art_4.jpg was downloaded!
art_5.jpg was downloaded!
Finished in 24.17 secs

# multiThreading.py
448c3453bd30.jpg was downloaded!
b9d2bc813a63.jpg was downloaded!
62dd94fd0578.jpg was downloaded!
894d61486a9d.jpg was downloaded!
465ffa134781.jpg was downloaded!
Finished in 10.30 secs

# multiProcessing.py
0f9dfce30846.jpg was downloaded!
7c9f3577a63e.jpg was downloaded!
a3cf4ce0a4a6.jpg was downloaded!
7ad5b0ea2caa.jpg was downloaded!
b447980c73bc.jpg was downloaded!
Finished in 11.91 secs
```