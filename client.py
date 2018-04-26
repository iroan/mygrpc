from __future__ import print_function
import grpc
import ex1_pb2
import ex1_pb2_grpc

if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:40000')
    stub = ex1_pb2_grpc.greeterStub(channel)
    response = stub.sayhello(ex1_pb2.hello_request(name='wangkaixuan'))
    print('recvive from sever:',response)