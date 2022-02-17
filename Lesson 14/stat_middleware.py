from falcon import Request, Response
from kombu import Connection, Message
class StatMiddleware:
    def __init__(self, connection: Connection,
                 queue_name="queue_name", serializer="json",):
        self.queue = connection.SimpleQueue(queue_name)
        self.serializer = serializer

    def process_request(self, req: Request, resp: Response):
        self.send_req_stat(req)

    def process_response(self, req, resp, resource, req_succeeded):
        self.send_resp_stat(req, resp,req_succeeded)

    def prepare_stat_req_message(self, req: Request) -> dict:
        """
        :param req:
        :return:
        """
        return {
            "message": "new request",
            "path": req.path,
            "headers": req.headers,
            "qs": req.query_string,
            "method": req.method,
            "content_type": req.content_type,
        }

    def send_req_stat(self, req: Request):
        message = self.prepare_stat_req_message(req)
        self.queue.put(
            message=message,
            serializer=self.serializer,
        )
    def prepare_stat_resp_message(self, req: Request, resp: Response,req_succeeded:bool) -> dict:
        message = self.prepare_stat_resp_message(req)
        message.update({
            "message": "result response",
            "status": resp.status,
            "req_succeeded": req_succeeded,
        })
        return message

    def send_resp_stat(self, req: Request, resp: Response, req_succeeded:bool):
        message =self.prepare_stat_resp_message(req, resp, req_succeeded)
        self.queue.put(
            message=message,
            serializer=self.serializer,
        )
    def process_stat(self,callback, n=1, timeout=1):
        for i in range(n):
            message: Message = self.queue.get(block=True, timeout=timeout)
            callback(message.payload)
            message.ack()

    def close(self):
        self.queue.close()