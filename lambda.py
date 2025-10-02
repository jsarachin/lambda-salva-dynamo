import json
import boto3
import os
import uuid

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Lambda iniciada com sucesso!")
    logger.info(event)

    body = json.loads(event.get("body"))

    logger.info(body)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("pratica-aula-7")
    
    item = {
        "IdCliente": str(uuid.uuid4()),
        "Nome": body.get("nome"),
        "Idade": body.get("idade")
    }

    table.put_item(Item=item)

    return "Item salvo com sucesso!"