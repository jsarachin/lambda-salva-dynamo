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

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("pratica-aula-7")
    
    item = {
        "IdCliente": str(uuid.uuid4()),
        "Nome": event.get("nome"),
        "Idade": event.get("idade")
    }

    table.put_item(Item=item)

    return "Item salvo com sucesso!"