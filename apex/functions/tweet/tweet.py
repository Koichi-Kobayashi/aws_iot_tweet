# -*- coding: utf-8 -*-

import emoji
from requests_oauthlib import OAuth1Session
from utils import util
import boto3
import conf


def create_tweet(button_event):
    status = ''

    # https://www.webpagefx.com/tools/emoji-cheat-sheet/
    if button_event['clickType'] == 'SINGLE':
        # コーヒー我慢☺☕
        status = emoji.emojize(conf.clickType_single, use_aliases=True)
    elif button_event['clickType'] == 'DOUBLE':
        # 食べ過ぎ我慢🍚🍖👍
        status = emoji.emojize(conf.clickType_double, use_aliases=True)
    else:
        # 食べちゃった😫
        status = emoji.emojize(conf.clickType_long, use_aliases=True)

    status = status + \
        '\n' + \
        str(get_time(button_event['reportedTime'])) + \
        '\n'
#        '#SORACOM LTE-M Button powered by #AWS'

    return status


def get_time(reportedTime):
    return util.now()


def dynamo(button_event):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('button_event')

    table.put_item(
        Item={
            "date_time": button_event['reportedTime'],
            "click_type": button_event['clickType']
        }
    )


def _tweet(text):
    params = {"status": text}
    twitter = OAuth1Session(conf.ConsumerKey, conf.ConsumerSecret, conf.AccessToken, conf.AccesssTokenSecert)
    req = twitter.post(conf.UPDATE_URL, params=params)

    if req.status_code == 200:
        return text
    else:
        return req.status_code


def lambda_handler(event, context):
    button_event = event['deviceEvent']['buttonClicked']
    dynamo(button_event)
    _tweet(create_tweet(button_event))

