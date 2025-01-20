from config import LuneConfig
from domain.rag.storage import storage
from concurrent import futures


import logging
import grpc
import v1.grpc.extractor_pb2 as extractor_pb2
import v1.grpc.extractor_pb2_grpc as extractor_pb2_grpc


def create_app():
    init_log()
    init_storage()


def init_log():
    logging.basicConfig(
        level="INFO", format="%(asctime)s.%(msecs)03d %(levelname)s [%(threadName)s] [%(filename)s:%(lineno)d] - %(message)s")


def init_storage():
    # storage
    storage.init_app()


class Greeter(extractor_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return extractor_pb2.HelloReply(message="Hello, %s!" % request.name)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    extractor_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


def run():
    create_app()
    serve()


if __name__ == "__main__":
    run()
