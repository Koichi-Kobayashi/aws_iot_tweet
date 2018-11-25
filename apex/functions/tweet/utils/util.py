# -*- coding: utf-8 -*-

from datetime import datetime
import pytz


# 文字列 -> datetime
def iso_to_jstdt(iso_str):
    dt = None
    try:
        dt = datetime.strptime(iso_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        dt = pytz.utc.localize(dt).astimezone(pytz.timezone("Asia/Tokyo"))
    except ValueError:
        try:
            dt = datetime.strptime(iso_str, '%Y-%m-%dT%H:%M:%S.%f%z')
            dt = dt.astimezone(pytz.timezone("Asia/Tokyo"))
        except ValueError:
            pass
    return dt


# datetime -> 表示用文字列
def dt_to_str(dt):
    if dt is None:
        return ''
    return dt.strftime('%Y/%m/%d %H:%M:%S')


# datetime -> ISO文字列
def dt_to_isostr(dt):
    if dt is None:
        return ''
    return dt.isoformat()


def now():
    now = datetime.now()
    return pytz.utc.localize(now).astimezone(pytz.timezone("Asia/Tokyo"))

