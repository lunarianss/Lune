import app_factory
import grpc
import logging
from v1.grpc.service.service import ExtractorService
import v1.grpc.extractor.extractor_pb2_grpc as extractor_pb2_grpc
from concurrent import futures


logger = logging.getLogger(__name__)


def create_app():
    app_factory.init_log()
    app_factory.init_storage()
    app_factory.init_database()


def serve():
    port = "30001"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    extractor_pb2_grpc.add_ExtractorServicer_to_server(
        ExtractorService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


def run():
    create_app()
    serve()


if __name__ == "__main__":
    run()
