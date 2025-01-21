from concurrent import futures
import app_factory
import grpc
import v1.grpc.extractor_pb2 as extractor_pb2
import v1.grpc.extractor_pb2_grpc as extractor_pb2_grpc


def create_app():
    app_factory.init_log()
    app_factory.init_storage()
    app_factory.init_database()


class Greeter(extractor_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return extractor_pb2.HelloReply(message="Hello, %s!" % request.name)


def serve():
    port = "30001"
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
