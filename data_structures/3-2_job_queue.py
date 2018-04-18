# python3
import queue

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs_naive(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        priorityQ = queue.PriorityQueue()

        # put all threads into priority queue
        for i in range(self.num_workers):
            priorityQ.put(self.Worker(i))

        # for every job
        # get an idle thread
        for i in range(len(self.jobs)):
            idle_thread = priorityQ.get()

            self.assigned_workers[i] = idle_thread.id
            self.start_times[i] = idle_thread.busy_time

            idle_thread.busy_time += self.jobs[i]
            priorityQ.put(idle_thread);

    class Worker(object):
        def __init__(self, id):
            self.id = id
            self.busy_time = 0

        def __lt__(self, other):
            # if busy time is the same, then the thread with the lower id is lower than the thread with the higher id
            if self.busy_time == other.busy_time:
                if self.id < other.id:
                    return True
                else:
                    return False

            if self.busy_time < other.busy_time:
                return True
            else:
                return False

        def __gt__(self, other):
            # if busy time is the same, then the thread with the higher id is higher than the thread with the lower id
            if self.busy_time == other.busy_time:
                if self.id < other.id:
                    return False
                else:
                    return True

            if self.busy_time > other.busy_time:
                return True
            else:
                return False


    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

