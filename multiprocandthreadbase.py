# Multiprocessing/Threading demo script. 
# remember python allows for passing of objects into functions :)
# You can use this as a base for the construction of webserver/site service probes and more often application hammer(s)
# the more cores you have the faster you can do damage...
import concurrent.futures
import time
start = time.perf_counter()
def performTheseActions():
   return 1+1/1*3000
def main():
   # to utilize threading ProcessPoolExecutor() should be changed to ThreadPoolExecutor()
   with concurrent.futures.ProcessPoolExecutor() as performActivities:
       results = [performActivities.submit(performTheseActions) for _ in range(10)]
       for individualTaskRequest in concurrent.futures.as_completed(results):
           print(individualTaskRequest.result())
if __name__ == '__main__':
   main()
   endtime = time.perf_counter()
   print(f'begin time: {start} second(s)')
   print(f'End time: {endtime} second(s)') 