from concurrent import futures
import grpc
import ex1_pb2
import ex1_pb2_grpc
import time

class EX1(ex1_pb2_grpc.greeterServicer):
    def sayhello(self,request,context):
        return ex1_pb2.hello_reply(message='hello,%s' % request.name)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ex1_pb2_grpc.add_greeterServicer_to_server(EX1(),server)
    server.add_insecure_port('[::]:40000')
    server.start()
    try:
        while True:
            time.sleep(6000)
    except KeyboardInterrupt:
        server.stop(0)