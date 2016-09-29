import sublime
import sublime_plugin

import re

try:
  from Statement import statement
  from Expression import expression
except ImportError as error:
  sublime.error_message("Dependency import failed; please read readme for " +
   "JoinChainCall plugin for installation instructions; to disable this " +
   "message remove this plugin; message: " + str(error))
  raise error

def _get_token(view, selection):
  if not selection.empty():
    container = [selection.begin(), selection.end()]
  else:
    container = statement.get_root_statement(view, selection.b)

  tokens = container and statement.get_tokens(view, selection.b, container)

  _, token = tokens and statement.get_token(view, selection.b, tokens)
  return token

def join(view, edit, selection):
  token = _get_token(view, selection)
  if token == None:
    return

  delimeters = expression.find_matches(view, token[0], r'(\.|->)\s+',
    {'range': token})

  for delimeter in reversed(delimeters):
    region = sublime.Region(
      token[0] + delimeter.start(0),
      token[0] + delimeter.end(0)
    )

    view.replace(edit, region, delimeter.group(1))

def unjoin(view, edit, selection):
  token = _get_token(view, selection)
  if token == None:
    return

  line = view.substr(view.line(token[0]))
  indent = re.search(r'^(\s*)', line).group(1)
  delimeters = expression.find_matches(
    view,
    token[0],
    r'(\.|->)',
    {'range': token}
  )

  for delimeter in reversed(delimeters):
    region = sublime.Region(
      token[0] + delimeter.start(0),
      token[0] + delimeter.end(0)
    )

    view.replace(edit, region, "\n" + indent + "\t" + delimeter.group(1))

def toggle(view, edit, selection):
  token = _get_token(view, selection)
  if token == None:
    return

  delimeter = expression.find_match(view, token[0], r'(?:\.|->)\s*',
    {'range': token})

  if delimeter == None:
    return

  if "\n" in delimeter.group(0):
    join(view, edit, selection)
  else:
    unjoin(view, edit, selection)