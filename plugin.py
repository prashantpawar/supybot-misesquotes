###
# Copyright (c) 2010, Prashant Singh Pawar
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import httplib
import re


class MisesQuotes(callbacks.Plugin):
    """
    This plug fetches page from http://mises.org/quote.aspx and 
    parses the text stripping HTML tags and displays the text.
    """
    threaded = True
    def __init__(self,irc):
        self.__parent = super(MisesQuotes, self)
        self.__parent.__init__(irc)
        
    def mises(self, irc, msg, args):
        """
        Takes no argument and returns a quote from the mises.org.
        """
        self.conn=httplib.HTTPConnection("mises.org")
        self.conn.request("GET","/quote.aspx")
        r1=self.conn.getresponse()
        quote=r1.read()
        self.conn.close()
        reobj = re.compile(r"<(style|script)[^<>]*>.*?</\1>|</?[a-z][a-z0-9]*[^<>]*>|<!--.*?-->", re.DOTALL | re.IGNORECASE)
        quote = reobj.sub("", quote)
        irc.reply(quote)
    mises = wrap(mises)

Class = MisesQuotes


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
