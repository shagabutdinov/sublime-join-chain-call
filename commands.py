import sublime
import sublime_plugin

from JoinChainCall import join_chain_call

class ToggleChainCallJoining(sublime_plugin.TextCommand):
  def run(self, edit):
    for selection in self.view.sel():
      join_chain_call.toggle(self.view, edit, selection)

class JoinChainCall(sublime_plugin.TextCommand):
  def run(self, edit):
    for selection in self.view.sel():
      join_chain_call.join(self.view, edit, selection)

class UnjoinChainCall(sublime_plugin.TextCommand):
  def run(self, edit):
    for selection in self.view.sel():
      join_chain_call.unjoin(self.view, edit, selection)