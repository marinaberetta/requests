from __future__ import print_function

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)
def run2():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  response = stub.SayBye(helloworld_pb2.HelloRequest(name='FALA TCHAU PRA MIM (DADO DO CLIENTE)'))
  print("Greeter client received: " + response.message)
def run3():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  response = stub.soma(helloworld_pb2.HelloRequest(a="5",b="3"))
  print("Greeter client received: " + response.message)
def run4():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  response = stub.sub(helloworld_pb2.HelloRequest(a="5",b="3"))
  print("Greeter client received: " + response.message)


if __name__ == '__main__':
  run()
  run2()
  run3()
  run4()
