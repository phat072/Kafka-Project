"""RabbitMQ producer module."""
from __future__ import annotations
from dataclasses import dataclass

from typing import Any, Dict

import pika

from ...application.ports import IProducer, IMessage


@dataclass
class RabbitMQMessage(IMessage):
    """RabbitMQMessage class."""

    exchange: str
    topic: str
    body: bytes

 
class Producer(IProducer[IMessage]):
    """Producer class."""

    _user: str
    _password: str
    _host: str
    _port: str
    _vhost: str
    _delivery_mode: str
    _content_type: str
    _content_encoding: str

    def __init__(
        self,
        user: str,
        password: str,
        host: str,
        port: str,
        vhost: str,
        delivery_mode: str = "Persistant",
        content_type: str = "application/json",
        content_encoding: str = "utf-8"
    ) -> None:
        """Class constructor."""
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._vhost = vhost
        self._connection = None
        self._delivery_mode = delivery_mode
        self._content_type = content_type
        self._content_encoding = content_encoding

    def _connect(self) -> None:
        """Connect to RabbitMQ."""
        credentials = pika.PlainCredentials(self._user, self._password)
        parameters = pika.ConnectionParameters(
            host=self._host, port=self._port, virtual_host=self._vhost, credentials=credentials
        )
        self._connection = pika.BlockingConnection(parameters=parameters)

    def __enter__(self) -> Producer:
        """Create and start a connection with rabbitmq when the context manages is started."""
        self._connect()
        self._channel = self._connection.channel()

        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """Stop the connection when the context manager is exited."""
        # Gracefully close the connection
        self._connection.close()

    def publish(self, message: RabbitMQMessage) -> Dict[str, Any]:
        """
        Publish a message to RabbitMQ.

        Args:
            message (RabbitMQMessage): message to publish

        Returns
            Dict[str, Any]: # TBD
        """
        properties = pika.BasicProperties(
            delivery_mode=pika.DeliveryMode[self._delivery_mode],
            content_type=self._content_type,
            content_encoding=self._content_encoding
        )

        self._channel.basic_publish(
            exchange=message.exchange,
            routing_key=message.topic,
            body=message.body,
            properties=properties
        )
        return {}