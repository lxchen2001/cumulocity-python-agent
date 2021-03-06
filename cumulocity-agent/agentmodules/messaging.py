#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging, time
from framework.modulebase import Listener
from framework.smartrest import SmartRESTMessage

class Messenger(Listener):
  xid = 'c8y-python-v0.1'

  def handleOperation(self, message):
    if self.xid in message.topic and message.messageId == 'MSG':
      executing = SmartRESTMessage('s/us', '501', ['c8y_Message'])
      self.agent.publishMessage(executing)
      time.sleep(5)
      logging.info('Hey there was a message: ' + message.values[1])
      success = SmartRESTMessage('s/us', '503', ['c8y_Message'])
      self.agent.publishMessage(success)

  def getSupportedOperations(self):
    return ['c8y_Message']

  def getSupportedTemplates(self):
    return [self.xid]
