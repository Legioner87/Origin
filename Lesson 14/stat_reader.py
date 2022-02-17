import logging
from contextlib import closing
from kombu import Connection
import config
from stat_middleware import StatMiddleware

logger = logging.getLogger(__name__)
def process_entry(entry):
    logger.info("New entry %s", entry)

def process_stat_queue_forever(timeout=None):
    with Connection(config.AMQP_CONNECTION_URL) as conn:
        stats_middleware = StatMiddleware(
            connection=conn,
            queue_name=config.STAT_QUEUE_NAME,
        )
        with closing(stats_middleware):
            while True:
                try:
                    stats_middleware.process_stat(process_entry, timeout=timeout)
                except KeyboardInterrupt:
                    logging.warning("Bye!")
                    return

def main():
    logging.basicConfig(level=logging.INFO)
    logger.warning("Start listening")
    process_stat_queue_forever()
if __name__ == '__main__':
    main()