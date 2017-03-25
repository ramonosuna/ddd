#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import string
import codecs

form="""
	<html>
	  <head>
		<title>Unit 2 Rot 13</title>
	  </head>

	  <body>
		<h2>Enter some text to ROT13:</h2>
		<form method="post">
		  <textarea name="text"
					style="height: 100px; width: 400px;">%(rot)s</textarea>
		  <br>
		  <input type="submit">
		</form>
	  </body>

	</html>
"""

class MainHandler(webapp2.RequestHandler):
	def rot13(self,n):
		chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
		trans = chars[26:]+chars[:26]
		rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
		return ''.join( rot_char(c) for c in n )

	def escape_html(self,s):
		for(i, o) in (("&", "&amp;"),
					  (">", "&gt;"),
					  ("<", "&lt;"),
					  ('"', "&quot;")):
			s = s.replace(i,o)
		return s
		

	def get(self):
				self.response.out.write(form)

	def post(self):
			rot13 = self.request.get('text')

			rot13_1 = self.rot13(rot13)

			rot13_2 = self.escape_html(rot13_1)

			self.response.out.write(form % {"rot": rot13_2})
		

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
