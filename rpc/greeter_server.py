from concurrent import futures
import time

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(helloworld_pb2_grpc.GreeterServicer):

  def SayHello(self, request, context):
    return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)
  def SayBye(self, request, context):
    return helloworld_pb2.HelloReply(message='TCHAAAAAAAU , %s!' % request.name)
  def soma(self, request, context):
    aa = int(request.a)
    bb = int(request.b)
    aa = aa-bb
    val = str(aa)
    return helloworld_pb2.HelloReply(message='RESP+ : %s!' % str(int(request.a)+int(request.b)))
  def sub(self, request, context):
    aa = int(request.a)
    bb = int(request.b)
    aa = aa-bb
    val = str(aa)
    return helloworld_pb2.HelloReply(message='RESP- : %s!' % val)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
