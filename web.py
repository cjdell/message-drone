import os
import bottle
from bottle import route, run, template, static_file, request, response

from smbus import SMBus
import backlight
import screen
import sqlite3

import json
import pickle
from json import dumps, loads

conn = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '/drone.db')

class Display(object):
    backlight = None
    screen = None

    def __init__(self, bus):
        self.backlight = backlight.Backlight(bus, 0x62)
        self.screen    = screen.Screen(bus, 0x3e)

    def write(self, text):
        self.screen.write(text)

    def color(self, r, g, b):
        self.backlight.set_color(r, g, b)

    def move(self, col, row):
        self.screen.setCursor(col, row)

try:
    d = Display(SMBus(1))
except IOError as e:
    print(e)
    print('!!!! Cant access LCD display!')

class Message(object):
    name = ''
    message = ''

    def __init__(self, name, message):
        self.name = name
        self.message = message

class MessageStore(object):
    def get_all(self):
        c = conn.cursor()
        c.execute('SELECT * FROM message')
        rows = c.fetchall()
        return map(lambda row: Message(row[1], row[2]), rows)

    def insert(self, message):
        row = (message.name, message.message)
        c = conn.cursor()
        c.execute('INSERT INTO message (name, message) VALUES (?, ?)', row)
        conn.commit()

messageStore = MessageStore()

bottle.TEMPLATE_PATH.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/templates')

@route('/')
def index():
    return template('index')

@route('/panel')
def panel():
    return template('panel')

@route('/panel/messages')
def messages():
    messages = messageStore.get_all()
    return template('message-list', messages=messages)

@route('/message-form')
def message_form():
    return template('message-form')

@route('/assets/<filepath>')
def asset(filepath):
    return static_file(filepath, root=os.path.dirname(os.path.abspath(__file__)) + '/assets')

@route('/db/messages')
def db_messages_get():
    messages = messageStore.get_all()
    response.content_type = 'application/json'
    return dumps(messages, default=lambda obj: obj.__dict__)

@route('/db/messages', method='POST')
def db_messages_post():
    req = json.load(request.body)
    messageStore.insert(Message(req['name'], req['message']))
    return 'done'

@route('/control/display/<display>')
def control_display(display):
    d.move(0, 0)
    d.write('                ')
    d.move(0, 1)
    d.write('                ')

    d.move(0, 0)
    d.write(display[0:16])
    d.move(0, 1)
    d.write(display[16:32])
    return display

@route('/control/colour/<colour>')
def control_display(colour):
    r = int('0x' + colour[0:2], 0)
    g = int('0x' + colour[2:4], 0)
    b = int('0x' + colour[4:6], 0)
    d.color(r, g, b)
    return 'done'

run(host='0.0.0.0', port=80)

