# Uses python3
import argparse
import sys
import datetime

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    # return True if buffer is empty
    # return False is buffer is not empty
    def isEmpty(self):
        #print('buffer is ' + str(len(self.finish_time)))
        if len(self.finish_time) == 0:
            return True
        return False

    # return True if buffer is full
    # return False if buffer is not full
    def isFull(self):
        #print('is full')
        if len(self.finish_time) == self.size:
            return True
        return False

    # remove the processes that have a finish time before the arrival of the current request
    def removeProcessedRequests(self, request):
        #print('     purging')

        #print('     length before: ' + str(len(self.finish_time)))

        while self.finish_time:

            if self.finish_time[0] <= request.arrival_time:
                self.finish_time.pop(0)
            else:
                break

        #print('     length after: ' + str(len(self.finish_time)))


    #
    def process(self, request):
        # write your code here
        self.removeProcessedRequests(request)

        if self.isFull():
            return Response(True, -1)

        # if buffer empty, append request to finish_time
        if self.isEmpty():
            #print('     empty buffer')
            self.finish_time.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)

        # if there is something in the buffer
        # process the earlier packages first 
        resp = Response(False, self.finish_time[-1])

        # and append the new request to the queue
        self.finish_time.append(self.finish_time[-1] + request.process_time)

        # return response
        return resp





        return Response(False, -1)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)


if __name__ == "__main__":

    version = '0.1'
    date = '2018-04-11'

    parser = argparse.ArgumentParser(description='network packet processing simulation',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)

    args = parser.parse_args()
   
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
